import os, sys
import xlrd
import xlwt
import xlutils
import datetime
from xlutils.copy import copy
from xlutils.save import save
from xlutils.styles import Styles
from xlwt import easyxf
from ct import writeToFile

def readTxtResultsFile(logPatch):
    plikTxt = open(logPatch+"\\Results.txt")
    os.chdir(logPatch)
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

def searchTcInExcel(pathXmlFile, logPatch, testRunType, moduleNumber, excelSheetName):
    resultTab = readTxtResultsFile(logPatch=logPatch)
    if testRunType == 'Automatic':
        styleResultCell = easyxf('font: color blue, bold on; borders: left double; align: vert centre, horiz centre')
        styleTimeCell = easyxf('align: vert centre, horiz centre', num_format_str='H:MM:SS' )
        styleTestRunCell = easyxf('align: vert centre, horiz centre; borders: right double')
    elif testRunType == 'Manual':
        styleResultCell = easyxf('font: color green, bold on; borders: left double; align: vert centre, horiz centre')
        styleTimeCell = easyxf('align: vert centre, horiz centre', num_format_str='H:MM:SS')
        styleTestRunCell = easyxf('align: vert centre, horiz centre; borders: right double')

    wb = xlrd.open_workbook(pathXmlFile, formatting_info=True, on_demand=True)
    sheet = wb.sheet_by_name(excelSheetName)
    rb = copy(wb)
    rb_sheet = rb.get_sheet(excelSheetName)
    # Dla każdego elementu listy resultTab
    for tcList in resultTab:
        # Dla każdego indeksu od 0 do sheet.nrows
        for item in range(sheet.nrows):
            # Sprawdź czy nazwy TC są takie same
            if sheet.cell_value(item, 0) == tcList[0]:
                # Jeżeli TC jest takie same sprawdź czy parametr jest taki sam
                if sheet.cell_value(item, 1) == tcList[1]:
                    # Jeżeli TC i parametr jest taki sam sprawdź czy pole wyniku i czasu jest puste
                    if sheet.cell_value(item, 8) == '' and sheet.cell_value(item, 9) == '':
                        # Jeżeli są puste wprowadź wyniki do excel`a
                        rb_sheet.write(item, 8, tcList[2][0], styleResultCell)
                        rb_sheet.write(item, 9, tcList[4], styleTimeCell)
                        rb_sheet.write(item, 10, moduleNumber, styleTestRunCell)
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
                else:
                    # Dla każdego elementu od 0 do 100
                    for i in range(100):
                        # Sprawdź czy kolejne wiersze w excelu posiadają taką samą wartość pola parametr
                        if sheet.cell_value(item+i, 1) == tcList[1]:
                            # Jeżeli pola parametr są takie same sprawdź czy pole wyniku i czasu jest puste
                            if sheet.cell_value(item+i, 8) == '' and sheet.cell_value(item+i, 9) == '':
                                # Jeżeli są puste wprowadź wyniki do excel`a
                                rb_sheet.write(item, 8, tcList[2][0], styleResultCell)
                                rb_sheet.write(item, 9, tcList[4], styleTimeCell)
                                rb_sheet.write(item, 10, moduleNumber, styleTestRunCell)
                            # Jeżeli pola parametr są takie same sprawdź czy pole wyniku i czasu NIE jest puste
                            elif sheet.cell_value(item+i, 8) != '' and sheet.cell_value(item, 9) != '':
                                # Jeżeli NIE są puste wprowadź log do pliku Results_alredy_exist_in_excel.txt
                                excelResults = [sheet.cell_value(item, 0), sheet.cell_value(item, 1),
                                                sheet.cell_value(item, 8), sheet.cell_value(item, 9),
                                                sheet.cell_value(item, 10)]
                                if excelResults[2] == 'P':
                                    excelResults[2] = 'PASS'
                                elif excelResults[2] == 'F':
                                    excelResults[2] = 'FAIL'
                                writeToFile(tab=tcList, excelResult=excelResults, param='TC_added')
                            break
                break



    if os.path.basename(pathXmlFile[-14:]) == (str(datetime.date.today())+'.xls'):
        wb.release_resources()
        rb.save(os.path.basename(pathXmlFile))
    else:
        rb.save(pathXmlFile[:-4]+'_'+str(datetime.date.today())+'.xls')

    return 'Done'