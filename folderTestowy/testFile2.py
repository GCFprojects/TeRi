import os
import xlrd
from xlrd import *
from xlwt import *
from xlutils import copy, styles, save


book = open_workbook('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\testExcel.xls', formatting_info=True)
s = styles.Styles(book)

sheet = book.sheet_by_index(0)
A1_style = easyxf('pattern: pattern solid;')
A1_style.pattern.pattern_fore_colour = 0
sheet.

# rb.save('C:\\Python34\\Workspace\\GlobalLogic\\GCF project\\TeRi\\folderTestowy\\testExcel.xls')