from xlrd import open_workbook
from xlwt import *
from xlutils.copy import copy


wb = open_workbook('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\testExcel.xls')
rb = copy(wb)

s = rb.get_sheet(0)
s.write(0,0,'Czesc')
rb.save('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\testExcel.xls')