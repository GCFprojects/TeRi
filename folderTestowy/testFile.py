import xlrd
import xlwt
import xlutils

# from xlrd import *
# from xlwt import *
# from xlutils import *
def sheets():
    wb = xlrd.open_workbook('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\rome_rel2_protokolltestresults.xls')
    sheet = wb.sheet_names()
    wb.release_resources()
    return sheet
def openFiles():
    txtFile = open('C:\\Users\\marek.polak\\Desktop\\TeRI_Results\\2017-04-13\\Results.txt')
    workbook = xlrd.open_workbook('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\rome_rel2_protokolltestresults.xls')
    worksheet = workbook.sheet_by_name('2G')
    count = (sum(1 for line in txtFile))
    for item in range(count):
        for r in range(worksheet.nrows):
            pass

    tcName = txtFile.readline()
    tcName = tcName.split(',')
    print(tcName[0])



openFiles()


#print(sheets())
