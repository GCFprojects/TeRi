import os
import datetime

# Zmienne globalne
dir_path = ''
# Otwieranie pliku, czytanie tekstu linia po lini. Kazdą linię przekazuje do funkcji primFormat. Funkcja tworzy listę list zwróconych z primFormat.
def start(pathTxtFile):
    plikTxt = open(pathTxtFile, encoding='utf-8')
    count = sum(1 for line in open(pathTxtFile))-1

    checkPathForLogs()

    tab = []
    for s in range(count):
        line = plikTxt.readline()
        tab.append(primFormat(line))

    if tab[0][0] == 'Test':
        writeToFile(tab[0], param='Test')
        tab.remove(tab[0])

    tab = deleteListsWithoutResults(tab)
    tab = findDublicateTC(tab)

    return dir_path

def checkPathForLogs():
    userdir = os.path.expanduser('~')
    global dir_path
    dir_path = userdir + '\\Desktop\\TeRI_Results\\' + str(datetime.date.today())

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)



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
        result = open(dir_path +  '\\Results.txt', 'a', encoding='utf-8')
        for item in tab:
            result.write('{0}, '.format(item))
        result.write('\n')
        result.close()
    elif param == 'Warning':
        warning = open(dir_path + '\\Warnings.txt', 'a', encoding='utf-8')
        for item in tab:
            warning.write('{0}, '.format(item))
        warning.write('\n')
        warning.close()
    elif param == 'Fail':
        fail = open(dir_path + '\\Fails_to_user_veryfication.txt', 'a', encoding='utf-8')
        for item in tab:
            fail.write('{0}, '.format(item))
        fail.write('\n')
        fail.close()
    elif param == 'TC_added':
        TC_added = open(dir_path + '\\Results_already_exist_in_excel.txt', 'a', encoding='utf-8')
        TC_added.write('In excel: '+str(excelResult)+'\n')
        TC_added.write('In CMW-500: '+str(tab)+'\n\n')
        TC_added.close()
    elif param == 'Test':
        result = open(dir_path + '\\Results.txt', 'a', encoding='utf-8')
        for item in tab:
            result.write('{0}, '.format(item))
        result.write('\n')
        result.close()

        warning = open(dir_path + '\\Warnings.txt', 'a', encoding='utf-8')
        warning.write('Duplicate TC with different results !!!\nFollowint TC requires verification by the user.\n\n')
        for item in tab:
            warning.write('{0}, '.format(item))
        warning.write('\n')
        warning.close()

        fail = open(dir_path + '\\Fails_to_user_veryfication.txt', 'a', encoding='utf-8')
        for item in tab:
            fail.write('{0}, '.format(item))
        fail.write('\n')
        fail.close()

        TC_added = open(dir_path + '\\Results_already_exist_in_excel.txt', 'a', encoding='utf-8')
        TC_added.write('Following results were added in Excel sheet:\n\n')
        for item in tab:
            TC_added.write('{0}, '.format(item))
        TC_added.write('\n')
        TC_added.close()
# Usuwanie list, które posiadają puste pole rezultatów
def deleteListsWithoutResults(tcList):
    tab = [item for item in tcList if item[2] == '']
    if len(tab) > 0:
        for rm in tab:
            tcList.remove(rm)
        del tab[:]
    return tcList

def findDublicateTC(tab):
    tmpList = []
    resultPassList = []
    resultFailList = []

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
                    for a in paramList:
                        if a not in tmpList:
                            tmpList.append(a)
                            if a is paramList[-1]:
                                checkResults(paramList)
                else:
                    if paramList[0][2] == 'PASS':
                        if paramList[0] not in resultPassList:
                            resultPassList.append(paramList[0])
                    elif paramList[0][2] == 'FAIL' or tcList[0][2] == 'INCONCLUSIVE' or tcList[0][2] == 'ERROR' \
                            or tcList[0][2] == 'INVALID' or tcList[0][2] == 'NONE':
                        if paramList[0] not in resultFailList:
                            resultFailList.append(paramList[0])
        else:
            if tcList[0][2] == 'PASS':
                if tcList[0] not in resultPassList:
                    resultPassList.append(tcList[0])
            elif tcList[0][2] == 'FAIL' or tcList[0][2] == 'INCONCLUSIVE' or tcList[0][2] == 'ERROR' \
                    or tcList[0][2] == 'INVALID' or tcList[0][2] == 'NONE':
                if tcList[0] not in resultFailList:
                    resultFailList.append(tcList[0])

    for item in resultPassList:
        writeToFile(item, param='Result')
    for item in resultFailList:
        writeToFile(item, param='Fail')

def checkResults(paramList):
    resultFail = [x for x in paramList if
                  x[2] == 'FAIL' or x[2] == 'INCONCLUSIVE' or x[2] == 'ERROR' or x[2] == 'INVALID' or x[2] == 'NONE']
    resultPass = [x for x in paramList if x[2] == 'PASS']

    if len(resultPass) > 0 and len(resultFail) == 0:
        for item in resultPass:
            writeToFile(item, param='Result')
    elif len(resultPass) == 0 and len(resultFail) > 0:
        for item in resultFail:
            writeToFile(item, param='Fail')
    elif len(resultPass) > 0 and len(resultFail) > 0:
        for item in paramList:
            writeToFile(item, param='Warning')


    # tc_passfail_list = []
    # pass_list = [i for i in tab if i[2] == 'PASS']
    # fail_list = [i for i in tab if i[2] == 'FAIL' or i[2] == 'INCONCLUSIVE' or i[2] == 'ERROR' or i[2] == 'INVALID'
    #              or i[2] == 'NONE']
    # # Dla każdego elementu listy tab
    # for item in tab:
    #     # Sprawdź czy TC znajduje się w liście pass_list oraz fail_list
    #     if any(item[0] in p for p in pass_list) and any(item[0] in f for f in fail_list):
    #         # Jeżeli tak dodaj do tc_passfail_list
    #         tc_passfail_list.append(item)
    # del tab[:]
    # # Usuń wpisy
    # for item in tc_passfail_list:
    #     if item in pass_list:
    #         pass_list.remove(item)
    #     if item in fail_list:
    #         fail_list.remove(item)
    #
    # check_passfail_list(tc_passfail_list)
    #
    # temp_pass_list = []
    # for item in pass_list:
    #     temp = [i for i in pass_list if i[0] == item[0] and i[1] == item[1]]
    #
    #     if len(temp) > 1:
    #         i = temp[:-1]
    #         for z in i:
    #             if z not in temp_pass_list:
    #                 temp_pass_list.append(z)
    #
    # for item in temp_pass_list:
    #     pass_list.remove(item)
    #
    # writeToFile(pass_list, param='Result')
    # writeToFile(fail_list, param='Fail')

# Koncepcyjna funkcja mająca na celu sprawdzanie daty i czasu i na tej podstawie wybierająca najnowszy TC
# def check_date(tc_list):
#     latest_tc = []
#     for item in tc_list:
#         if len(latest_tc) == 0:
#             latest_tc.extend(item)
#         if latest_tc[3].split(" ")[0] > item[3].split(" ")[0]:
#             latest_tc.clear()
#             latest_tc.extend(item)
#         elif latest_tc[3].split(" ")[0] == item[3].split(" ")[0]:
#             if latest_tc[3].split(" ")[1] < item[3].split(" ")[1]:
#                 latest_tc.clear()
#                 latest_tc.extend(item)
#
#     tc_list.remove(latest_tc)
#     return tc_list
