import os

# Otwieranie pliku, czytanie tekstu linia po lini. Kazdą linię przekazuje do funkcji primFormat. Funkcja tworzy listę list zwróconych z primFormat.
def start():
    plikTxt = open('Test\Status.csv')
    count = sum(1 for line in open('Test\Status.csv'))-1
    print(count)
    tab = []
    for s in range(count):
        line = plikTxt.readline()
        tab.append(primFormat(line))

    if tab[s][0] != 'Test':
        checkTC(tab[s])
    else:
        createFile(tab[0])


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

def checkTC(tab):
    tab1 = tab
    tab2 = []
    if len(tab2 == 0):
        print("empty list tab2")
        tab2 = tab1
    elif tab1[0] == tab2[0]:
        print('tak')
start()

