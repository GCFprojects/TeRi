def update_excel():
    TC_added=open('TC_added.txt','a')
    TC_added.write=('Following TC results were added in Excel:\n\n')
    TC_added.close()

    TC_updated=open('TC_updated.txt','a')
    TC_updated.write=('Warning!\nFollowing TC results were updated in Excel:\n\n')
    TC_updated.close()

    TC_error=open('TC_error.txt','a')
    TC_error.write=('Error!\nFollowing TC results were NOT updated in Excel. Current Verdict in Excel is different with latest result:\n\n')
    TC_error.close()
    
    if sheet.cell(row=i, column=col_ver).value == None:
        sheet.cell(row=i, column=col_ver).value = linelist[2]
        sheet.cell(row=i, column=col_dur).value = linelist[3]
        sheet.cell(row=i, column=col_ms).value = linelist[4]
        
        TC_added=open('TC_added.txt','a')
        TC_added.write=(str(line)+'\n')
        TC_added.close()
    else:
        if sheet.cell(row=i, column=col_ver).value == linelist[2]:
            if sheet.cell(row=i, column=col_dur).value == linelist[3]:
                if sheet.cell(row=i, column=col_ms).value == linelist[4]:
                    True
                else:
                    sheet.cell(row=i, column=col_ms).value = linelist[4]

                    TC_updated=open('TC_updated.txt','a')
                    TC_updated.write=(str(line)+'\n')
                    TC_updated.close()
            else:
                sheet.cell(row=i, column=col_dur).value == linelist[3]
                sheet.cell(row=i, column=col_ms).value == linelist[4]

                TC_updated=open('TC_updated.txt','a')
                TC_updated.write=(str(line)+'\n')
                TC_updated.close()
        else:            
            TC_error=open('TC_error.txt','a')
            TC_error.write=(str(line)+'\n')
            TC_error.close()
# need add in Verdict value N/A handling
