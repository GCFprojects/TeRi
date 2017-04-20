import xlrd
import xlwt
import xlutils


def sheets():
    wb = xlrd.open_workbook(
        'C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\rome_rel2_protokolltestresults.xls')
    sheet = wb.sheet_names()
    print(sheet)
    return sheet

