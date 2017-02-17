import os

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
openFile()