import os
<<<<<<< HEAD
import xlwt

def openFile():
    plikTxt = open('Test\Status.csv')
    count = sum(1 for line in open('Test\Status.csv'))-1
    print(count)
    tab = []
    for s in range(count):
        line = plikTxt.readline()
        tab.append(primFormat(line))
        if tab[s][0] == 'Test':
            warning = open("Test\Warnings.txt", "w+")
            for item in tab[0]:
                warning.write("%s, " % item)

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

=======

def openFile():
    plikTxt = open('Test\Status.csv')
    for s in range(3):
        line = plikTxt.readline()
        line = line.split(",")
        for b in range(9):
            string = line[b]
            if b == 8:
                string = string[1:len(string) - 2]
            else:
                string = string[1:len(string) - 1]
            print(string)
>>>>>>> baa97cda733495472f31f84acb673824bcd47a0d
openFile()