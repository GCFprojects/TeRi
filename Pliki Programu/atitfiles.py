import os, glob, datetime


def path():
    localPath = os.path.expanduser('~')+'\\Desktop\\TeRI_Results\\IOT_ATT_WCDMA_GSM_singleCMW'
    listItems = os.listdir(localPath)
    find(listItems, localPath)


def find(listItems, localPath):

    for item in listItems:
        os.chdir(localPath)
        if os.path.isdir(item):
            folderPath = localPath+'\\'+item
            os.chdir(folderPath)
            folderItems = os.listdir(folderPath)
            if 'summary.txt' in folderItems:
                createAtit(folderItems, folderPath)
            find(folderItems, folderPath)


def writeToFile(at):
    result = open(os.path.expanduser('~')+'\\Desktop\\TeRI_Results\\' + str(datetime.date.today()) + '\\AT&T.txt', 'a', encoding='utf-8')
    # for item in atit_summary:
    #     result.write('{0}, '.format(item))
    result.write('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}'.format(at[6][0:14], 'None', at[10], at[1], at[8], 'None', 'None', at[4], at[12], '\n'))
    result.close()


def createAtit(folderItem, folderPath):
    summary_file = open(folderPath+'\\summary.txt','r', encoding='utf-8')
    count = sum(1 for line in open(folderPath+"\\summary.txt"))
    for item in range(count):
        atit_summary = summary_file.readline()
        atit_summary = atit_summary.strip()
        atit_summary = atit_summary.split(",")
        for item in range(len(atit_summary)):
            atit_summary[item] = atit_summary[item].strip("\"")
        if atit_summary[0] != 'Project name':
            writeToFile(atit_summary)

path()