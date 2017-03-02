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
        warning = open("Test\Warnings.txt", "w+")
        for item in tab:
            warning.write("{}, ".format(item))
        warning.close()
    tab.remove(tab[0])
    count = sum(1 for line in tab)
    checkTC(tab, count)
# Formatowanie tekstu. Tworzenie listy, usówanie cudzysłowów. Funkcja zwraca listę
def primFormat(line):
    tab = []
    line = line.split(",")
    for b in range(9):
        string = line[b]
        if b == 8:
            string = string[1:len(string) - 2]
        else:
            string = string[1:len(string) - 1]
        tab.append(string)
    return tab
# Wpisywanie do plików
def writeToFile(tab, tab2 = []):
    if len(tab2) == 0:
        True
# Porównywanie TC. Tworzenie listy list posiadających te same TC. Przekazywanie listy tcList do funkcji checkTcList
def checkTC(tab, count):
    tabToCompare = tab[0]
    tcList = []
    for item in range(count):
        if tabToCompare == tab[item]:
            continue
        elif tab[item][0] == tabToCompare[0]:
            tcList.append(tabToCompare)
            tabToCompare = tab[item]
        else:
            if len(tcList) != 0:
                tcList.append(tabToCompare)
                checkResultList(tcList)
                tcList.clear()
            tabToCompare = tab[item]
# Usówanie list posiadające puste pole rezultatów
def checkResultList(tcList):
    count = 0
    tab = []
    for item in range(len(tcList)):
        tab = tcList[item-count]
        if tab[2] == '':
            tcList.remove(tab)
            count += 1
    checkTcList(tcList)

def checkTcList(tcList):
    count = 0
    paramList = []
    for item in range(len(tcList)): #Pętla dla całej przekazanej listy list.
        if len(paramList) != 0: #Warunek sprawdzający wartość listy paramList
            count += 1 #Licznik zwiększający swoją wartość
            for s in range(len(tcList)-count): #Sprawdzam tu wszystkie kolejne listy za listą wpisaną do paramList
                if paramList[1] == tcList[s+count][1]: #Porównanie parametrów w liście paramList i tcList
                    if paramList[2] == 'PASS': #Sprawdzam rezultat wpisany do paramList. Jeżeli PASS to:
                        if tcList[s+count][2] == 'PASS': # Sprawdzamy rezultat wpisany do tcList. Jeżeli PASS to:
                            paramList = tcList[s+count] # Wpisuję do listy paramList kolejną listę z listy list tcList
                        else: #Jeżeli warunek tcList[s+count][2] == 'PASS' nie jest spełniony to:
                            writeToFile(paramList, tcList[s+count]) #Wpisuje obie listy do pliku Error
                    else: #Jeżeli warunek paramList[2] == 'PASS' nie jest spełniony to:
                        True
                else: #Jeżeli warunek paramList[1] == tcList[s+count][1] nie jest spełniony to:
                    True # Pobieramy koeleny rekord z listy tcList
                input()
            paramList = tcList[item]
        else: #Jeżeli warunek len(paramList) != 0 nie jest spełniony
            paramList = tcList[item] #wpisujemy do listy paramList pierwszą listę z listy list tcList
start()