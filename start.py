import os, sys
import datetime
import xlrd
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from MainWindow import *
from os.path import isfile
from ct import start
# from ImportResultsToExcel import readTxtResultsFile
from ImportResultsToExcel import searchTcInExcel



# Zmienne globalne
pathTxtFile = ''
pathXmlFile = ''

class StartQT4(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Ustawienie help
        helpFile = open('Help.txt').read()
        self.ui.resultWindow.setText(helpFile)
        # Ustawienie wartosci poczatkowej dla okien browser`ow
        self.ui.path_txt_window.setText("Wskaż ścieżkę do pliku txt lub csv")
        self.ui.path_xml_window.setText("Wskaż ścieżkę do pliku xml")

        self.ui.resultColumn.setText('I')
        # Wlasne polaczenia slotow
        QtCore.QObject.connect(self.ui.browse_txt_button, QtCore.SIGNAL("clicked()"), self.browse_txt_file)
        QtCore.QObject.connect(self.ui.browse_xml_button, QtCore.SIGNAL("clicked()"), self.browse_xml_file)
        QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"), self.startProcess)
        # QtCore.QObject.connect(self.ui.helpButton, QtCore.SIGNAL("clicked()"), self.showHelp)
    # Wyszukiwarka plików txt i csv
    def browse_txt_file(self):
        browserTxt = QtGui.QFileDialog(self)
        self.filename = browserTxt.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop')
        if isfile(self.filename):
            plikTxt = open(self.filename)
            if os.path.basename(plikTxt.name)[-4:] == '.txt' or os.path.basename(plikTxt.name)[-4:] == '.csv':
                # self.ui.path_xml_window.setText(os.path.basename(plikTxt.name))
                self.ui.path_txt_window.setText(plikTxt.name)
                global pathTxtFile
                pathTxtFile = plikTxt.name
                return plikTxt.name
            else:
                self.showDialog(0)
    # Wyszukiwarka plików xls i xlsx
    def browse_xml_file(self):
        browserXml = QtGui.QFileDialog(self)
        self.filename = browserXml.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop')
        if isfile(self.filename):
            plikXml = open(self.filename)
            if os.path.basename(plikXml.name)[-4:] == '.xls':
                # self.ui.path_xml_window.setText(os.path.basename(plikXml.name))
                self.ui.path_xml_window.setText(plikXml.name)
                global pathXmlFile
                pathXmlFile = plikXml.name
                #self.loadComboBoxItems()
                return plikXml.name
            else:
                self.showDialog(1)

    def loadComboBoxItems(self):
        """
        Funkcja odświeża listę wyświetlającą się w ComboBox dodając nazwy zakładek zaczytanych z  
        :return: 
        """
        #self.ui.setupUi()
        wb=xlrd.open_workbook(pathXmlFile)
        sheet = wb.sheet_names()
        self.ui.load(sheets=sheet)
    # Popup informujący o błędnym rozszeżeniu pliku
    def showDialog(self, button=None):
        msg = QMessageBox()
        msg.setText("Information:")
        if button == 0:
            msg.setInformativeText("Wybrałeś plik o niepoprawnym rozszeżeniu.\nWybierz plik .txt lub .csv")
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Notification")
            msg.setStandardButtons(QMessageBox.Ok)
        elif button == 1:
            msg.setInformativeText("Wybrałeś plik o niepoprawnym rozszeżeniu.\nWybierz plik .xml")
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Notification")
            msg.setStandardButtons(QMessageBox.Ok)
        elif button == 2:
            msg.setInformativeText("Nieprowidłowa ścieżka dostępowa do plików.\nSprawdź czy podałeś poprawną ścieżkę i spróbuj ponownie")
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Notification")
            msg.setStandardButtons(QMessageBox.Ok)
        elif button == 3:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("SUCCEC SUCCES !!!")
            msg.setInformativeText("Copy results from CMW-500 file to excel was finished with SUCCES !!!\n Great Job mate :)")
        elif button == 4:
            msg.setWindowTitle("Information:")
            msg.setIcon(QMessageBox.Question)
            msg.setWindowTitle("Module Number")
            msg.setInformativeText("Do you want to enter results without specifying module number ?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg.exec_()

        if result == QtGui.QMessageBox.Yes:
            return 'Yes'
        elif result == QtGui.QMessageBox.No:
            return 'No'

    def startProcess(self):
        """
        Funkcja przekazuje ścieżkę do plików.
        """
        if pathTxtFile != '' and pathXmlFile != '':
            logPatch = start(pathTxtFile)
            excelSheetName = str(self.ui.comboBox.currentText())
            if self.ui.automaticTestRun.isChecked():
                testRunType = 'Automatic'
            elif self.ui.manualTestRun.isChecked():
                testRunType = 'Manual'
            if self.ui.moduleNumber.text() != '':
                moduleNumber = self.ui.moduleNumber.text()
                if (searchTcInExcel(pathXmlFile=pathXmlFile, logPatch=logPatch, testRunType=testRunType,
                                    moduleNumber=moduleNumber, excelSheetName=excelSheetName)) == 'Done':
                    self.showDialog(3)
            else:
                if self.showDialog(4) == 'Yes':
                    moduleNumber = ''
                    if (searchTcInExcel(pathXmlFile=pathXmlFile, logPatch=logPatch, testRunType=testRunType,
                                        moduleNumber=moduleNumber, excelSheetName=excelSheetName)) == 'Done':
                        self.showDialog(3)

        else:
            self.showDialog(2)
        # patchXmlFile zmienna globalna z ścieżką do pliku xml

    # def showHelp(self):
    #     pass
        # fd = QtGui.QFileDialog(self)
        # file = open('help.txt').read()
        # self.ui.resultWindow.setText(file)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec())