import os
import xlrd
import datetime
from xlutils.copy import copy
from xlwt import easyxf
from ct import writeToFile

def readTxtResultsFile(logPatch):
    plikTxt = open(logPatch+"\\Results.txt")
    resultTab = []
    for line in plikTxt:
        line = line.split(",")
        for i in range(len(line)):
            line[i] = line[i].strip()
        line.remove('')
        if line[1] == 'none':
            line[1] = ''
        if line[0] != 'Test':
            resultTab.append(line)

    return resultTab

def searchTcInExcel(pathXlsFile, logPatch, testRunType, moduleNumber, excelSheetName, location):
    resultTab = readTxtResultsFile(logPatch=logPatch)
    # location = checkLocation(excelSheetName)
    excelStyle = excelSheetStyle(testRunType=testRunType)

    wb = xlrd.open_workbook(pathXlsFile, formatting_info=True, on_demand=True)
    sheet = wb.sheet_by_name(excelSheetName)
    rb = copy(wb)

    rb_sheet = rb.get_sheet(excelSheetName)

    # Wpisywanie w excel`u formuł (Do naprawy !!!)
    # if excelSheetName == '2G' or excelSheetName == '3G':
    #     sheetFunctions(excelSheetName,sheet=sheet, rb_sheet=rb_sheet)

    # Dla każdego elementu listy resultTab
    for tcList in resultTab:
        # Dla każdego indeksu od 0 do sheet.nrows
        for item in range(sheet.nrows):
            # Sprawdź czy nazwy TC są takie same
            if str(sheet.cell_value(item, 0)) == tcList[0]:
                # Jeżeli TC jest takie same sprawdź czy parametr jest taki sam
                help_tryexc = None
                try:
                    if str(int(sheet.cell_value(item, 1))) == tcList[1]:
                        help_tryexc = 'First'
                    elif sheet.cell_value(item, 1) == '-' and sheet.cell_value(item + 1, 1) != '':
                        help_tryexc = 'Second'
                    else:
                        help_tryexc = 'Third'
                except ValueError:
                    if str(sheet.cell_value(item, 1)) == tcList[1]:
                        help_tryexc = 'First'
                    elif sheet.cell_value(item, 1) == '-' and sheet.cell_value(item + 1, 1) != '':
                        help_tryexc = 'Second'
                    else:
                        help_tryexc = 'Third'

                if help_tryexc == 'First':
                    # Jeżeli TC i parametr jest taki sam sprawdź czy pole wyniku i czasu jest puste
                    if sheet.cell_value(item, 8) == '' and sheet.cell_value(item, 9) == '':
                        # Jeżeli są puste wprowadź wyniki do excel`a
                        writeToExcel(rb_sheet=rb_sheet, item=item, tcList=tcList,
                                     moduleNumber=moduleNumber, excelStyle=excelStyle, location=location)
                    # Jeżeli TC i parametr jest taki sam sprawdź czy pole wyniku i czasu NIE jest puste
                    elif sheet.cell_value(item, 8) != '' and sheet.cell_value(item, 9) != '':
                            # Jeżeli NIE są puste wprowadź log do pliku Results_alredy_exist_in_excel.txt
                            excelResults = [sheet.cell_value(item, 0), sheet.cell_value(item, 1), sheet.cell_value(item, 8)]
                            if excelResults[2] == 'P':
                                excelResults[2] = 'PASS'
                            elif excelResults[2] == 'F':
                                excelResults[2] = 'FAIL'
                            writeToFile(tab=tcList, excelResult=excelResults, param='TC_added')

                    # W przypadku gdy TC jest taki sam ale parametr się nie zgadza
                elif help_tryexc == 'Second':
                    # Jeżeli TC i parametr się zgadzają sprawdź czy pole wyniku i czasu jest puste
                    if sheet.cell_value(item, 8) == '' and sheet.cell_value(item, 9) == '':
                        # Jeżeli są puste wprowadź wyniki do excel`a
                        writeToExcel(rb_sheet=rb_sheet, item=item, tcList=tcList,
                                     moduleNumber=moduleNumber, excelStyle=excelStyle, location=location)

                    # Jeżeli TC i parametr jest taki sam sprawdź czy pole wyniku i czasu NIE jest puste
                    elif sheet.cell_value(item, 8) != '' and sheet.cell_value(item, 9) != '':
                        # Jeżeli NIE są puste wprowadź log do pliku Results_alredy_exist_in_excel.txt
                        excelResults = [sheet.cell_value(item, 0), sheet.cell_value(item, 1), sheet.cell_value(item, 8)]
                        if excelResults[2] == 'P':
                            excelResults[2] = 'PASS'
                        elif excelResults[2] == 'F':
                            excelResults[2] = 'FAIL'
                        writeToFile(tab=tcList, excelResult=excelResults, param='TC_added')
                elif help_tryexc == 'Third':
                    # Dla każdego elementu od 0 do 100
                    for i in range(100):
                        flag = None
                        # Sprawdź czy kolejne wiersze w excelu posiadają taką samą wartość pola parametr
                        try:
                            if str(int(sheet.cell_value(item + i, 1))) == tcList[1]:
                                flag = True
                        except ValueError:
                            if sheet.cell_value(item + i, 1) == tcList[1]:
                                flag = True
                        if flag:
                            # Jeżeli pola parametr są takie same sprawdź czy pole wyniku i czasu jest puste
                            if sheet.cell_value(item+i, 8) == '' and sheet.cell_value(item+i, 9) == '':
                                # Jeżeli są puste wprowadź wyniki do excel`a
                                writeToExcel(rb_sheet=rb_sheet, item=item+i, tcList=tcList,
                                             moduleNumber=moduleNumber, excelStyle=excelStyle, location=location)

                            # Jeżeli pola parametr są takie same sprawdź czy pole wyniku i czasu NIE jest puste
                            elif sheet.cell_value(item+i, 8) != '' and sheet.cell_value(item, 9) != '':
                                # Jeżeli NIE są puste wprowadź log do pliku Results_alredy_exist_in_excel.txt
                                excelResults = [sheet.cell_value(item+i, 0), sheet.cell_value(item+i, 1),
                                                sheet.cell_value(item+i, 8), sheet.cell_value(item+i, 9),
                                                sheet.cell_value(item+i, 10)]
                                if excelResults[2] == 'P':
                                    excelResults[2] = 'PASS'
                                elif excelResults[2] == 'F':
                                    excelResults[2] = 'FAIL'
                                writeToFile(tab=tcList, excelResult=excelResults, param='TC_added')
                            break
                break


    excelName = os.path.basename(pathXlsFile)
    if excelName[-14:] == (str(datetime.date.today())+'.xls'):
        wb.release_resources()
        rb.save(os.path.join(logPatch, excelName))
    else:
        rb.save(os.path.join(logPatch,(excelName[:-4]+'_'+str(datetime.date.today())+'.xls')))

        # PermissionRestriction

    return 'Done'
# Funkcja do wprowadzania formuł i metod do excel`a (Nie działa. Do naprawy !!!)
# def sheetFunctions(excelSheetName, sheet, rb_sheet):
#     stylePassedCell = easyxf('font: color green; align: vert centre, horiz centre')
#     styleFailedCell = easyxf('font: color red; align: vert centre, horiz centre')
#     styleNotExecutedCell = easyxf('font: color blue; borders: bottom thin; align: vert centre, horiz centre')
#     styleSummeCell = easyxf('font: color black, bold on; borders: bottom double; align: vert centre, horiz centre')
#     styleSummeTimeCell = easyxf('align: vert centre, horiz centre')
#     styleNACell = easyxf('font: color blue; align: vert centre, horiz centre')
#     styleTimeCell = easyxf('align: vert centre, horiz centre; borders: left double, right double, top double, bottom  double')
#
#     cellNumber = {'NA':0, 'Pass':0, 'Fail':0, 'NotExecuted':0, 'Summe':0, 'TC':0}
#     tab = []
#     if excelSheetName == '2G':
#         TC = {'KC201':'', 'KC202':'', 'KC203':'', 'KC204':'', 'KC205':'', 'KC206':'', 'KC207':'', 'KC208':'', 'KC211':'',
#               'KC221':'', 'KC222':'', 'KC223':'', 'KC231':'', 'KC232':'', 'KC233':'', 'KC241':''}
#     elif excelSheetName == '3G':
#         TC = {'KC401':'', 'KC402':'', 'KC403':'', 'KC404':'', 'KC405':'', 'KC406':'', 'KC408':'', 'KC420':'', 'KC421':'',
#               'KC422':'', 'KC423':'', 'KC424':'', 'KC425':'', 'KC426':'', 'KC427':'', 'KC429':'', 'KC433':''}
#
#     for i in range(sheet.nrows):
#
#         if sheet.cell_value(i,6) == 'N/A':
#             cellNumberNA = i
#             tab.append(i)
#         elif sheet.cell_value(i,6) == 'Passed':
#             cellNumberPass = i
#             tab.append(i)
#         elif sheet.cell_value(i,6) == 'Failed':
#             cellNumberFail = i
#             tab.append(i)
#         elif sheet.cell_value(i,6) == 'Not executed':
#             cellNumberNotExecuted = i
#             tab.append(i)
#         elif sheet.cell_value(i,6) == 'Summe':
#             cellNumberSumme = i
#             tab.append(i)
#
#         if sheet.cell_value(i, 9) in TC.keys():
#             TC[sheet.cell_value(i, 9)] = i
#
#     cellNumberMin = tab[0]
#     for i in tab:
#         if cellNumberMin > i:
#             cellNumberMin = i
#
#     if cellNumber['NA'] != '' and cellNumber['Pass'] != '' and cellNumber['Fail'] != '' and cellNumber['NotExecuted'] != '' and cellNumber['Summe'] != '':
#         rb_sheet.write(cellNumberNA, 8, xlwt.Formula('COUNTIF(I4:I'+str(cellNumberMin-1)+';"=N/A")'),styleNACell )
#         rb_sheet.write(cellNumberPass, 8, xlwt.Formula('COUNTIF(I4:I'+str(cellNumberMin-1)+';"=P")'),stylePassedCell)
#         rb_sheet.write(cellNumberFail, 8, xlwt.Formula('COUNTIF(I4:I'+str(cellNumberMin-1)+';"=F")+COUNTIF(I4:I'+str(cellNumberMin-1)+';"=I")'),styleFailedCell)
#         rb_sheet.write(cellNumberNotExecuted, 8, xlwt.Formula('COUNTIF(I4:I'+str(cellNumberMin-1)+';"")'),styleNotExecutedCell)
#         rb_sheet.write(cellNumberSumme, 8, xlwt.Formula('SUM(I'+str(cellNumberMin)+':I'+str(cellNumberSumme)+')'),styleSummeCell)
#         rb_sheet.write(cellNumberSumme, 9, xlwt.Formula('SUM(J4:J'+str(cellNumberMin-1)+')'), styleSummeTimeCell)
#
#     for i in range(50):
#         if excelSheetName == '2G':
#             if sheet.cell_value(i+cellNumber['Summe'], 2) == 'KC201':
#                 cellNumber['TC'] = i+cellNumber['Summe']
#                 break
#         elif excelSheetName == '3G':
#             if sheet.cell_value(i+cellNumber['Summe'], 2) == 'WCDMA R99':
#                 cellNumber['TC'] = i+cellNumber['Summe']
#                 break
#
#     if excelSheetName == '2G':
#         rb_sheet.write(cellNumber['TC'], 9, xlwt.Formula('SUM(J' + str(TC['KC201'] + 2) + ':J' + str(TC['KC202']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 1, 9, xlwt.Formula('SUM(J' + str(TC['KC202'] + 2) + ':J' + str(TC['KC203']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 2, 9, xlwt.Formula('SUM(J' + str(TC['KC203'] + 2) + ':J' + str(TC['KC204']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 3, 9, xlwt.Formula('SUM(J' + str(TC['KC204'] + 2) + ':J' + str(TC['KC205']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 4, 9, xlwt.Formula('SUM(J' + str(TC['KC205'] + 2) + ':J' + str(TC['KC206']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 5, 9, xlwt.Formula('SUM(J' + str(TC['KC206'] + 2) + ':J' + str(TC['KC207']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 6, 9, xlwt.Formula('SUM(J' + str(TC['KC207'] + 2) + ':J' + str(TC['KC208']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 7, 9, xlwt.Formula('SUM(J' + str(TC['KC208'] + 2) + ':J' + str(TC['KC221']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 8, 9, xlwt.Formula('SUM(J' + str(TC['KC221'] + 2) + ':J' + str(TC['KC222']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 9, 9, xlwt.Formula('SUM(J' + str(TC['KC222'] + 2) + ':J' + str(TC['KC223']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 10, 9, xlwt.Formula('SUM(J' + str(TC['KC223'] + 2) + ':J' + str(TC['KC231']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 11, 9, xlwt.Formula('SUM(J' + str(TC['KC231'] + 2) + ':J' + str(TC['KC232']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 12, 9, xlwt.Formula('SUM(J' + str(TC['KC232'] + 2) + ':J' + str(TC['KC233']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 13, 9, xlwt.Formula('SUM(J' + str(TC['KC233'] + 2) + ':J' + str(TC['KC241']) + ')'), styleTimeCell)
#         rb_sheet.write(cellNumber['TC'] + 14, 9, xlwt.Formula('SUM(J' + str(TC['KC241'] + 2) + ':J' + str(cellNumberMin - 1) + ')'), styleTimeCell)
#     elif excelSheetName == '3G':
#         rb_sheet.write(cellNumber['TC'], 9, xlwt.Formula('SUM(J' + str(TC['KC401'] + 2) + ':J' + str(TC['KC402']) + ')'), styleTimeCell) # WCDMA R99
#         rb_sheet.write(cellNumber['TC'] + 1, 9, xlwt.Formula('SUM(J' + str(TC['KC404'] + 2) + ':J' + str(TC['KC405']) + ')'), styleTimeCell) # WCDMA R5 HSDPA
#         rb_sheet.write(cellNumber['TC'] + 2, 9, xlwt.Formula('SUM(J' + str(TC['KC405'] + 2) + ':J' + str(TC['KC406']) + ')'), styleTimeCell) # WCDMA R6 HSUPA
#         rb_sheet.write(cellNumber['TC'] + 3, 9, xlwt.Formula('SUM(J' + str(TC['KC406'] + 2) + ':J' + str(TC['KC408']) + ')'), styleTimeCell) # WCDMA R7 CIPH
#         rb_sheet.write(cellNumber['TC'] + 4, 9, xlwt.Formula('SUM(J' + str(TC['KC421'] + 2) + ':J' + str(TC['KC422']) + ')'), styleTimeCell) # WCDMA R7 CPC
#         rb_sheet.write(cellNumber['TC'] + 5, 9, xlwt.Formula('SUM(J' + str(TC['KC422'] + 2) + ':J' + str(TC['KC423']) + ')'), styleTimeCell) # WCDMA R7 64QAM
#         rb_sheet.write(cellNumber['TC'] + 6, 9, xlwt.Formula('SUM(J' + str(TC['KC423'] + 2) + ':J' + str(TC['KC424']) + ')'), styleTimeCell) # WCDMA R7 L2ENH
#         rb_sheet.write(cellNumber['TC'] + 7, 9, xlwt.Formula('SUM(J' + str(TC['KC424'] + 2) + ':J' + str(TC['KC425']) + ')'), styleTimeCell) # WCDMA ECFACH DL
#         rb_sheet.write(cellNumber['TC'] + 8, 9, xlwt.Formula('SUM(J' + str(TC['KC425'] + 2) + ':J' + str(TC['KC426']) + ')'), styleTimeCell) # WCDMA R7 MIMO
#         rb_sheet.write(cellNumber['TC'] + 9, 9, xlwt.Formula('SUM(J' + str(TC['KC427'] + 2) + ':J' + str(TC['KC429']) + ')'), styleTimeCell) # WCDMA R8 CSVoH
#         rb_sheet.write(cellNumber['TC'] + 10, 9, xlwt.Formula('SUM(J' + str(TC['KC429'] + 2) + ':J' + str(TC['KC433']) + ')'), styleTimeCell) # WCDMA R8 Fast Dormancy

# def checkLocation(excelSheetName):
#     if excelSheetName == '2G':
#         return 'WRO2'
#     elif excelSheetName == '3G':
#         return 'WRO1'

def excelSheetStyle(testRunType):
    if testRunType == 'Automatic':
        styleResultCell = easyxf('font: color blue, bold on; borders: left double; align: vert centre, horiz centre')

    elif testRunType == 'Manual':
        styleResultCell = easyxf('font: color green, bold on; borders: left double; align: vert centre, horiz centre')

    styleTimeCell = easyxf('align: vert centre, horiz centre', num_format_str='h:mm:ss')
    # styleTimeCell = XFStyle()
    # styleTimeCell.alignment.horz = Alignment.HORZ_CENTER
    # styleTimeCell.num_format_str = 'HH:MM:SS'
    styleTestRunCell = easyxf('align: vert centre, horiz centre; borders: right double')
    styleTestSW_HW = easyxf('align: vert centre, horiz centre; borders: right double, left double')

    return [styleResultCell, styleTimeCell, styleTestRunCell, styleTestSW_HW]

def writeToExcel(rb_sheet, item, tcList, moduleNumber, excelStyle, location):
    rb_sheet.write(item, 8, tcList[2][0], excelStyle[0])
    rb_sheet.write(item, 9, datetime.datetime.strptime(tcList[4], "%H:%M:%S"), excelStyle[1])
    rb_sheet.write(item, 10, moduleNumber, excelStyle[2])
    rb_sheet.write(item, 14, tcList[8], excelStyle[3])
    rb_sheet.write(item, 16, location, excelStyle[3])