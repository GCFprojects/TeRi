import xlrd
from xlrd import *
from xlwt import *
from xlutils.copy import copy

def searchTcInExcel(txtLine):
    wb = xlrd.open_workbook('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\rome_rel2_protokolltestresults.xls', formatting_info=True)
    # wb = xlrd.open_workbook('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\testExcel.xls')
    sheet = wb.sheet_by_name("2G")
    cell_value = sheet.cell(0,0).value
    for item in range(sheet.nrows):
        # print(item+1, ": ", sheet.cell_value(item, 0))
        if sheet.cell_value(item, 0) == txtLine[0] and sheet.cell_value(item, 1) == txtLine[1]:
            if sheet.cell_value(item, 9) == '':
                rb = copy(wb)
                rb_sheet = rb.get_sheet('2G')
                rb_sheet.write(item, 8, txtLine[2][0])
                rb_sheet.write(item, 9, txtLine[4])
                rb.save('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\rome_rel2_protokolltestresults.xls')
            # print("Wiersz: ", item+1)
        else:
            # Jeżeli TC nie zostanie znaleziony w excelu to wpisz do pliku "TCnotFound.txt"
            pass

def addResultToExcel():
    pass

def readTxtResultsFile():
    plikTxt = open("C:\\Users\\marek.polak\\Desktop\\TeRI_Results\\2017-04-21\\Results.txt")
    for line in plikTxt:
        line = line.split(",")
        for i in range(len(line)):
            line[i] = line[i].strip()
        line.remove('')
        if line[1] == 'none':
            line[1] = ''
        if line[2] == 'INCONCLUSIVE' or line[2] == 'ERROR':
            line[2] = 'FAIL'
        print(line)
        if line[0] != 'Test':
            searchTcInExcel(line)

def sheets():
    wb = xlrd.open_workbook('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\rome_rel2_protokolltestresults.xls')
    sheet = wb.sheet_by_name("2G")
    wb.release_resources()
    print(sheet)

readTxtResultsFile()

