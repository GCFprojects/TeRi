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
        createFile(tab[0])

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
# Tworzenie pliku Warnings zapisywanie
def createFile(tab):
    warning = open("Test\Warnings.txt", "w+")
    for item in tab:
        warning.write("%s, " % item)

def checkTC(tab, count):
    tabToCompare = tab[0]
    tcList = []
    licznik = 0
    for item in range(count):
        if tab[item][0] == tabToCompare[0]:
            tcList.append(tab[item])
        else:
            if len(tcList) != 0:
                checkTcList(tcList)
                tcList.clear()
                tabToCompare = tab[item]
                licznik += 1
    print(licznik)


def checkTcList(tcList):
    print(tcList)
start()