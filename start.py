import os, sys
import datetime
import xlrd

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from MainWindow import *
from os.path import isfile
from ct import start
from ImportResultsToExcel import readTxtResultsFile


# Zmienne globalne
pathTxtFile = ''
pathXmlFile = ''

class StartQT4(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Ustawienie wartosci poczatkowej dla okien browser`ow
        self.ui.path_txt_window.setText("Wskaż ścieżkę do pliku txt lub csv")
        self.ui.path_xml_window.setText("Wskaż ścieżkę do pliku xml")
        # Wlasne polaczenia slotow
        QtCore.QObject.connect(self.ui.browse_txt_button, QtCore.SIGNAL("clicked()"), self.browse_txt_file)
        QtCore.QObject.connect(self.ui.browse_xml_button, QtCore.SIGNAL("clicked()"), self.browse_xml_file)
        QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"), self.startProcess)
        QtCore.QObject.connect(self.ui.logsButton, QtCore.SIGNAL("clicked()"), self.showLogs)
    # Wyszukiwarka plików txt i csv
    def browse_txt_file(self):
        browserTxt = QtGui.QFileDialog(self)
        self.filename = browserTxt.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop\\TeRI_Results\\Zurich')
        if isfile(self.filename):
            plikTxt = open(self.filename)
            if os.path.basename(plikTxt.name)[-4:] == '.txt' or os.path.basename(plikTxt.name)[-4:] == '.csv':
                self.ui.path_txt_window.setText(plikTxt.name)
                global pathTxtFile
                pathTxtFile = plikTxt.name
                return plikTxt.name
            else:
                self.showDialog(0)
    # Wyszukiwarka plików xls i xlsx

    def browse_xml_file(self):
        browserXml = QtGui.QFileDialog(self)
        self.filename = browserXml.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop\\TeRI_Results\\Zurich')
        if isfile(self.filename):
            plikXml = open(self.filename)
            if os.path.basename(plikXml.name)[-4:] == '.xls':
                self.ui.path_xml_window.setText(os.path.basename(plikXml.name))
                global pathXmlFile
                pathXmlFile = plikXml.name
                #self.loadComboBoxItems()
                #return plikXml
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
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Notification")

        msg.setText("Info:")
        if button == 0:
            msg.setInformativeText("Wybrałeś plik o niepoprawnym rozszeżeniu.\nWybierz plik .txt lub .csv")
        elif button == 1:
            msg.setInformativeText("Wybrałeś plik o niepoprawnym rozszeżeniu.\nWybierz plik .xml")
        elif button == 2:
            msg.setInformativeText("Nieprowidłowa ścieżka dostępowa do plików.\nSprawdź czy podałeś poprawną ścieżkę i spróbuj ponownie")
        elif button == 3:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Information")
            msg.setInformativeText("Done !!!")

        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec()

    def startProcess(self):
        """
        Funkcja przekazuje ścieżkę do plików.
        :return:
        """
        if self.ui.automaticTestRun.isChecked():
            testRunType = 'Automatic'
        elif self.ui.manualTestRun.isChecked():
            testRunType = 'Manual'
        moduleNumber = self.ui.moduleNumber.text()
        if pathTxtFile != '' and pathXmlFile != '':
            logPatch = start(pathTxtFile)
            # if (readTxtResultsFile(pathXmlFile=pathXmlFile, logPatch=logPatch, testRunType=testRunType, moduleNumber=moduleNumber)) == 'Done':
            self.showDialog(3)
        else:
            self.showDialog(2)
        # patchXmlFile zmienna globalna z ścieżką do pliku xml

    def showLogs(self):

        print('Logs')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec())