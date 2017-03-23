import os

# Otwieranie pliku, czytanie tekstu linia po lini. Kazdą linię przekazuje do funkcji primFormat. Funkcja tworzy listę list zwróconych z primFormat.
def start():
    plikTxt = open('Test\Status.csv')
    count = sum(1 for line in open('Test\Status.csv'))-1

    tab = []
    for s in range(count):
        line = plikTxt.readline()
        tab.append(primFormat(line))

    if tab[0][0] == 'Test':
        writeToFile(tab[0], 'Test')
        tab.remove(tab[0])

    tab = deleteListsWithoutResults(tab)
    checkTC(tab)
# Formatowanie tekstu. Tworzenie listy, usówanie cudzysłowów. Funkcja zwraca listę
def primFormat(line):
    tab = []
    line = line.split(",")
    for b in range(len(line)):
        string = line[b]
        if b == (len(line)-1):
            string = string[1:len(string) - 2]
        else:
            string = string[1:len(string) - 1]
        tab.append(string)
    return tab
# Wpisywanie do plików
def writeToFile(tab, param=None):
    if param == 'Result':
        result = open("Test\Results.txt", "a")
        for item in tab:
            result.write('\n')
            for i in item:
                result.write('{}, '.format(i))
        result.close()
    elif param == 'Warning':
        warning = open("Test\Warnings.txt", "a")
        for item in tab:
            warning.write('\n')
            for i in item:
                warning.write('{}, '.format(i))
    elif param == 'Test':
        result = open("Test\Results.txt", "w+")
        for item in tab:
            result.write('{}, '.format(item))
        result.close()
        warning = open("Test\Warnings.txt", "w+")
        for item in tab:
            warning.write('{}, '.format(item))
        warning.close()
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

start()
