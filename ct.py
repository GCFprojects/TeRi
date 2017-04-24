import os
import datetime
#import ImportResultsToExcel as IRTE

# Zmienne globalne
dir_path = ''
timeNow = ''
# Otwieranie pliku, czytanie tekstu linia po lini. Kazdą linię przekazuje do funkcji primFormat. Funkcja tworzy listę list zwróconych z primFormat.
def start(pathTxtFile):
    plikTxt = open(pathTxtFile, encoding='utf-8')
    count = sum(1 for line in open(pathTxtFile))-1

    userdir = os.path.expanduser('~')
    global dir_path
    dir_path = userdir + '\\Desktop\\TeRI_Results\\' + str(datetime.date.today())
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    global timeNow
    timeNow = datetime.datetime.now().strftime('%H_%M_%S')
    tab = []
    for s in range(count):
        line = plikTxt.readline()
        tab.append(primFormat(line))

    if tab[0][0] == 'Test':
        writeToFile(tab[0], 'Test')
        tab.remove(tab[0])

    tab = deleteListsWithoutResults(tab)
    tab = deleteWarningsResults(tab)
    checkTC(tab)

    return 'Done'
# Formatowanie tekstu. Tworzenie listy, usówanie cudzysłowów. Funkcja zwraca listę
def primFormat(line):
    tab = []
    line = line.split(",")

    for s in line:
        s = s.strip()
        s = s.strip("\"")
        tab.append(s)
    return tab
# Wpisywanie do plików
def writeToFile(tab, param=None):
    if param == 'Result':
        result = open(dir_path+'\\Results_'+timeNow+'.txt', 'a', encoding='utf-8')
        for item in tab:
            result.write('{0}, '.format(item))
        result.write('\n')
        result.close()
    elif param == 'Warning':
        warning = open(dir_path+"\\Warnings_"+timeNow+'.txt', 'a', encoding='utf-8')
        for item in tab:
            warning.write('{0}, '.format(item))
        warning.write('\n')
        warning.close()
    elif param == 'Fail':
        fail = open(dir_path+"\\Fails_"+timeNow+'.txt', 'a', encoding='utf-8')
        for item in tab:
            fail.write('{0}, '.format(item))
        fail.write('\n')
        fail.close()
    elif param == 'Test':
        result = open(dir_path+"\\Results_"+timeNow+'.txt', 'w+', encoding='utf-8')
        for item in tab:
            result.write('{0}, '.format(item))
        result.write('\n\n')
        result.close()
        warning = open(dir_path+"\\Warnings_"+timeNow+'.txt', 'w+', encoding='utf-8')
        for item in tab:
            warning.write('{0}, '.format(item))
        warning.write('\n\n')
        warning.close()
        fail = open(dir_path + "\\Fails_" + timeNow + '.txt', 'a', encoding='utf-8')
        for item in tab:
            fail.write('{0}, '.format(item))
        fail.write('\n\n')
        fail.close()
# Porównywanie TC. Tworzenie listy list posiadających te same TC. Przekazywanie listy tcList do funkcji checkTcList
def checkTC(tab):
    tempList = []
    for item in tab:
        list = [x for x in tab if x[0] == item[0]]

        if len(tempList) == 0:
            tempList.extend(list)
            if len(tempList) > 1:
                checkParameterAndResult(tempList)
            elif len(tempList) == 1:
                writeToFile(tempList, 'Result')
        elif tempList != list:
            tempList.clear()
            tempList.extend(list)
            if len(tempList) > 1:
                checkParameterAndResult(tempList)
            elif len(tempList) == 1:
                writeToFile(tempList, 'Result')
# Usówanie list, które posiadają puste pole rezultatów
def deleteListsWithoutResults(tcList):
    tab = [item for item in tcList if item[2] == '']
    for rm in tab:
        tcList.remove(rm)
    return tcList
#
def deleteWarningsResults(tab):
    tabWarningResults = [item for item in tab if item[2] == 'INCONCLUSIVE' or item[2] == 'INVALID' or item[2] == 'ERROR']
    for rm in tabWarningResults:
        tab.remove(rm)
    for item in tabWarningResults:
        writeToFile(item, 'Warning')
    tabFailResults = [item for item in tab if item[2] == 'FAIL']
    for rm in tabFailResults:
        tab.remove(rm)
    for item in tabFailResults:
        writeToFile(item, 'Fail')

    return tab

def checkParameterAndResult(tcList):
    #Deklaracje List
    uniqueLists = []
    dublicateLists = []
    #Pętla tworząca listę unikalnych list oraz dublikatów
    for item in range(len(tcList)):
        #Do listy tab zapisywane są listy filtrowane po parametrze
        tab = [x for x in tcList if x[1] == tcList[item][1]]
        #Tworzymy pętle z unikatowymi wpisami
        if len(tab) == 1:
            uniqueLists.extend(tab)
        #Tworzymy listę dublikatów.
        elif len(tab) > 1:
            passResults = [x for x in tab if x[2] == 'PASS']
            failResults = [x for x in tab if x[2] != 'PASS']
            if len(passResults) == len(tab) or len(failResults) == len(tab):
                if tab[-1] not in uniqueLists:
                    uniqueLists.append(tab[-1])
            else:
                writeToFile(tab, 'Warning')
    writeToFile(uniqueLists, 'Result')