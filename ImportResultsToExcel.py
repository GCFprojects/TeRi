
import xlrd
from xlutils.copy import copy
from xlutils.styles import Styles
from xlwt import easyxf
from ct import writeToFile

def searchTcInExcel(resultTab, pathXmlFile, testRunType, moduleNumber):
    if testRunType == 'Automatic':
        styleResultCell = easyxf('font: color blue, bold on; borders: left double; align: vert centre, horiz centre')
        styleTimeCell = easyxf(num_format_str='h:mm:ss')
        styleTestRunCell = easyxf('align: vert centre, horiz centre')
    elif testRunType == 'Manual':
        styleResultCell = easyxf('font: color green, bold on; borders: left double; align: vert centre, horiz centre')
        # styleTimeCell = easyxf()
        styleTestRunCell = easyxf('align: vert centre, horiz centre')

    wb = xlrd.open_workbook(pathXmlFile, formatting_info=True)
    # wb = xlrd.open_workbook('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\testExcel.xls', , formatting_info=True)
    sheet = wb.sheet_by_name('3G')
    rb = copy(wb)
    rb_sheet = rb.get_sheet('3G')
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
                        rb.save(pathXmlFile)
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
                                rb.save(pathXmlFile)
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



def readTxtResultsFile(pathXmlFile, logPatch, testRunType, moduleNumber):
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

    searchTcInExcel(resultTab=resultTab, pathXmlFile=pathXmlFile, testRunType=testRunType, moduleNumber=moduleNumber)
    return 'Done'


