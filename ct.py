import os
import datetime

# Zmienne globalne
dir_path = ''

# Otwieranie pliku, czytanie tekstu linia po lini. Kazdą linię przekazuje do funkcji primFormat. Funkcja tworzy listę list zwróconych z primFormat.
def start(pathTxtFile):
    plikTxt = open(pathTxtFile, encoding='utf-8')
    count = sum(1 for line in open(pathTxtFile))-1

    userdir = os.path.expanduser('~')
    global dir_path
    dir_path = userdir + '\\Desktop\\TeRI_Results\\' + str(datetime.date.today())
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    tab = []
    for s in range(count):
        line = plikTxt.readline()
        tab.append(primFormat(line))
    if tab[0][0] == 'Test':
        writeToFile(tab[0], param='Test')
        tab.remove(tab[0])

    tab = deleteListsWithoutResults(tab)
    tab = findDublicateTC(tab)
    #tab = deleteWarningsResults(tab) # Do przerobienia
    #checkTC(tab) # Do przerobienia

    return dir_path

# Formatowanie tekstu. Tworzenie listy, usówanie cudzysłowów. Funkcja zwraca listę
def primFormat(line):
    tab = []
    line = line.split(",")

    for item in line:
        item = item.strip()
        item = item.strip("\"")
        tab.append(item)
    return tab

# Wpisywanie do plików
def writeToFile(tab, excelResult=None, param=None):
    if param == 'Result':
        result = open(dir_path+'\\Results.txt', 'a', encoding='utf-8')
        for item in tab:
            result.write('{0}, '.format(item))
        result.write('\n')
        result.close()
    elif param == 'Warning':
        warning = open(dir_path+'\\Warnings.txt', 'a', encoding='utf-8')
        for item in tab:
            warning.write('{0}, '.format(item))
        warning.write('\n')
        warning.close()
    elif param == 'Fail':
        fail = open(dir_path+'\\Fails_to _user_weryfication.txt', 'a', encoding='utf-8')
        for item in tab:
            fail.write('{0}, '.format(item))
        fail.write('\n')
        fail.close()
    elif param == 'TC_added':
        TC_added = open(dir_path+"\\Results_alredy_exist_in_excel.txt", 'a', encoding='utf-8')
        TC_added.write('In excel: '+str(excelResult)+'\n')
        TC_added.write('In CMW-500: '+str(tab)+'\n\n')
        TC_added.close()
    elif param == 'Test':
        result = open(dir_path+'\\Results.txt', 'a', encoding='utf-8')
        for item in tab:
            result.write('{0}, '.format(item))
        result.write('\n')
        result.close()

        warning = open(dir_path+'\\Warnings.txt', 'a', encoding='utf-8')
        warning.write('Duplicate TC with different results !!!\nFollowint TC requires verification by the user.\n\n')
        for item in tab:
            warning.write('{0}, '.format(item))
        warning.write('\n')
        warning.close()

        fail = open(dir_path + '\\Fails_to _user_weryfication.txt', 'a', encoding='utf-8')
        for item in tab:
            fail.write('{0}, '.format(item))
        fail.write('\n')
        fail.close()

        TC_added = open(dir_path + '\\Results_alredy_exist_in_excel.txt', 'a', encoding='utf-8')
        TC_added.write('Following results were added in Excel sheet:\n\n')
        for item in tab:
            TC_added.write('{0}, '.format(item))
        TC_added.write('\n')
        TC_added.close()

# Usówanie list, które posiadają puste pole rezultatów
def deleteListsWithoutResults(tcList):
    tab = [item for item in tcList if item[2] == '']
    for rm in tab:
        tcList.remove(rm)
    return tcList


def findDublicateTC(tab):
    # Dla każdego elementu listy tab
    list = []
    for item in tab:
        # Sporządź listę tcList w której znajdować się będą elementy o tych samych nazwach TC
        tcList = [x for x in tab if x[0] == item[0]]
        # Jeżeli lista będzie większa od 1
        if len(tcList) > 1:
            # Dla każdego elementu listy tcList
            for param in tcList:
                # Sporządź listę paramList w której umieścisz elementy o tych samych parametrach
                paramList = [x for x in tcList if x[1] == param[1]]
                # Jeżeli lista będzie większa od 1
                if len(paramList) > 1:
                    # Wywołaj funkcję checkResults przekazując listę parametrów
                    checkResults(paramList)
                else:
                    if paramList[0][2] == 'PASS':
                        writeToFile(paramList[0], param='Result')
                    elif paramList[0][2] == 'FAIL' or tcList[0][2] == 'INCONCLUSIVE' or tcList[0][2] == 'ERROR' or tcList[0][2] == 'INVALID':
                        writeToFile(paramList[0], param='Fail')
        else:
            if tcList[0][2] == 'PASS':
                writeToFile(tab=tcList[0], param='Result')
            elif tcList[0][2] == 'FAIL' or tcList[0][2] == 'INCONCLUSIVE' or tcList[0][2] == 'ERROR' or tcList[0][2] == 'INVALID':
                writeToFile(tcList[0], param='Fail')


def checkResults(paramList):
    # Sporządź listę z elementami zawierającymi na 3 miejscu 'PASS'
    resultPass = [item for item in paramList if item[2] == 'PASS']
    # Sporządź listę z elementami zawierającymi na 3 miejscu 'FAIL' lub 'INCONCLUSIVE'
    resultFail = [item for item in paramList if item[2] == 'FAIL' or item[2] == 'INCONCLUSIVE' or item[2] == 'ERROR' or item[2] == 'INVALID']

    if len(resultPass) == len(paramList): #or len(resultFail) == len(paramList) or len(resultRest) == len(paramList):
        writeToFile(resultPass[-1], param='Result')
    elif len(resultFail) == len(paramList):
        for item in resultFail:
            writeToFile(resultFail, param='Fail')

# # Porównywanie TC. Tworzenie listy list posiadających te same TC. Przekazywanie listy tcList do funkcji checkTcList
# def checkTC(tab):
#     tempList = []
#     for item in tab:
#         list = [x for x in tab if x[0] == item[0]]
#
#         if len(tempList) == 0:
#             tempList.extend(list)
#             if len(tempList) > 1:
#                 checkParameterAndResult(tempList)
#             elif len(tempList) == 1:
#                 writeToFile(tempList[0], param='Result')
#         elif tempList != list:
#             tempList.clear()
#             tempList.extend(list)
#             if len(tempList) > 1:
#                 checkParameterAndResult(tempList)
#             elif len(tempList) == 1:
#                 writeToFile(tempList[0], param='Result')
#
# #
# def deleteWarningsResults(tab):
#     tabWarningResults = [item for item in tab if item[2] == 'INCONCLUSIVE' or item[2] == 'INVALID' or item[2] == 'ERROR']
#     for rm in tabWarningResults:
#         tab.remove(rm)
#     for item in tabWarningResults:
#         writeToFile(item, param='Warning')
#     tabFailResults = [item for item in tab if item[2] == 'FAIL']
#     for rm in tabFailResults:
#         tab.remove(rm)
#     for item in tabFailResults:
#         writeToFile(item, param='Fail')
#
#     return tab
#
# def checkParameterAndResult(tcList):
#     #Deklaracje List
#     uniqueLists = []
#     dublicateLists = []
#     #Pętla tworząca listę unikalnych list oraz dublikatów
#     for item in range(len(tcList)):
#         #Do listy tab zapisywane są listy filtrowane po parametrze
#         tab = [x for x in tcList if x[1] == tcList[item][1]]
#         #Tworzymy pętle z unikatowymi wpisami
#         if len(tab) == 1:
#             uniqueLists.extend(tab)
#         #Tworzymy listę dublikatów.
#         elif len(tab) > 1:
#             passResults = [x for x in tab if x[2] == 'PASS']
#             failResults = [x for x in tab if x[2] != 'PASS']
#             if len(passResults) == len(tab) or len(failResults) == len(tab):
#                 if tab[-1] not in uniqueLists:
#                     uniqueLists.append(tab[-1])
#             else:
#                 writeToFile(tab, param='Warning')
#     for item in uniqueLists:
#         writeToFile(item, param='Result')