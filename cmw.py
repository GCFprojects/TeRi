def copy_result():

    file=open('C:\\Python35\\cmw500.txt')
    wb=openpyxl.load_workbook('D:\\Field Test\\rome.xlsx')
    sheet = wb.get_sheet_by_name('2G')
    col_ver = 10
    col_dur = 11
    col_ms = 12
    ms = M01
    TC_not_found=open('TC_not_found.txt','a')
    TC_not_found.write=('Following TC with Parameters were not found in Excel:\n\n')
    TC_not_found.close()

    for line in file.readlines():
        print(line)
        linelist=line.split(",")
        
        for rowNum in range(4,2000):
            if sheet.cell(row=rowNum, column=1).value==linelist[0]:
                for i in range (rowNum, rownum+10):
                    if sheet.cell(row=rowNum, column=2).value==linelist[1]:
                        update_excel()
                        break
                    else:
                        TC_not_found=open('TC_not_found.txt','a')
                        TC_not_found.write=(str(line)+'\n')
                        TC_not_found.close()
            else:
                TC_not_found=open('TC_not_found.txt','a')
                TC_not_found.write=(str(line)+'\n')
                TC_not_found.close()
            break
    
