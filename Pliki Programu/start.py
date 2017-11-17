import os
import sys
import xlrd
from xlutils.copy import copy
from PyQt4 import QtGui, QtCore

from mainWindowCSV import Ui_MainWindow
from os.path import isfile
from ct import start
from importResultsToExcel import searchTcInExcel
from importResultsToWebImax import ImportResultsToCSV


class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(StartQT4, self).__init__(parent)
        # QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Ustawienie help
        help_file = open('Help.txt').read()
        self.ui.resultWindow.setText(help_file)
        # Ustawienie wartosci poczatkowej dla okien browser`ow
        self.ui.path_txt_window.setText("Browse path to the txt or csv file. Path to results from CMW-500")
        self.ui.path_xls_window.setText("Browse path to the xls file. Path to Excel file where you want put results")
        self.ui.moduleNumber.setText("Z15")

        # Wlasne polaczenia slotow
        QtCore.QObject.connect(self.ui.browse_txt_button, QtCore.SIGNAL("clicked()"), self.browse_txt_file)
        QtCore.QObject.connect(self.ui.browse_xls_button, QtCore.SIGNAL("clicked()"), self.browse_xls_file)
        QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"), self.startProcess)
        self.ui.pushButtonCSVCreate.clicked.connect(self.startCreateCsvFile)
        # QtCore.QObject.connect(self.ui.helpButton, QtCore.SIGNAL("clicked()"), self.showHelp)

    # Wyszukiwarka plików txt i csv
    def browse_txt_file(self):
        browserTxt = QtGui.QFileDialog(self)
        self.filename = browserTxt.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop\\TeRI_Results\\PLAS9_W_200_068 TeRI test\\2G\\KC201-207')
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

    # Wyszukiwarka plików xls
    def browse_xls_file(self):
        browserXls = QtGui.QFileDialog(self)
        self.filename = browserXls.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop\\TeRI_Results\\Zurich')
        if isfile(self.filename):
            plikXls = open(self.filename)
            if os.path.basename(plikXls.name)[-4:] == '.xls':
                # self.ui.path_xml_window.setText(os.path.basename(plikXml.name))
                self.ui.path_xls_window.setText(plikXls.name)
                global pathXlsFile
                pathXlsFile = plikXls.name
                self.update_combobox()
                return plikXls.name
            else:
                self.showDialog(1)

    #
    def update_combobox(self):
        wb=xlrd.open_workbook(pathXlsFile)
        sheet = wb.sheet_names()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(list(sheet))

    # Popup informujący o błędnym rozszeżeniu pliku
    def showDialog(self, button=None):
        msg = QtGui.QMessageBox()
        msg.setText("Information:")
        if button == 0:
            msg.setInformativeText("Wybrałeś plik o niepoprawnym rozszeżeniu.\nWybierz plik .txt lub .csv")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Notification")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
        elif button == 1:
            msg.setInformativeText("Wybrałeś plik o niepoprawnym rozszeżeniu.\nWybierz plik .xls")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Notification")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
        elif button == 2:
            msg.setInformativeText("Nieprowidłowa ścieżka dostępowa do plików.\nSprawdź czy podałeś poprawną ścieżkę i spróbuj ponownie")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Notification")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
        elif button == 3:
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setWindowTitle("SUCCEC SUCCES !!!")
            msg.setInformativeText("Copy results from CMW-500 file to excel was finished with SUCCES !!!\n Great Job mate :)")
        elif button == 4:
            msg.setWindowTitle("Information:")
            msg.setIcon(QtGui.QMessageBox.Question)
            msg.setWindowTitle("Module Number")
            msg.setInformativeText("Do you want to enter results without specifying module number ?")
            msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        elif button == 5:
            msg.setInformativeText("You have an open excel file to whitch you want to enter the results.\nClose excel file and then press \"Start\" again.")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Warning !!!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)

        result = msg.exec_()

        if result == QtGui.QMessageBox.Yes:
            return 'Yes'
        elif result == QtGui.QMessageBox.No:
            return 'No'


    def startProcess(self):
        if pathTxtFile != '' and pathXlsFile != '':
            logPatch = start(pathTxtFile)
            excelSheetName = str(self.ui.comboBox.currentText())
            if self.ui.automaticTestRun.isChecked():
                testRunType = 'Automatic'
            elif self.ui.manualTestRun.isChecked():
                testRunType = 'Manual'

            if self.ui.moduleNumber.text() != '':
                moduleNumber = self.moduleFormat()
                result = searchTcInExcel(pathXlsFile=pathXlsFile, logPatch=logPatch, testRunType=testRunType,
                                    moduleNumber=moduleNumber, excelSheetName=excelSheetName)
                if result == 'Done':
                    self.showDialog(3)
                elif result == 'Excel':
                    self.showDialog(5)
            else:
                if self.showDialog(4) == 'Yes':
                    moduleNumber = ''
                    result = searchTcInExcel(pathXlsFile=pathXlsFile, logPatch=logPatch, testRunType=testRunType,
                                        moduleNumber=moduleNumber, excelSheetName=excelSheetName)
                    if result == 'Done':
                        self.showDialog(3)

        else:
            self.showDialog(2)


    def moduleFormat(self):
        moduleNumber = (self.ui.moduleNumber.text()).upper()
        if moduleNumber[0].isdigit():
            print('Nie jest litera')
        if not moduleNumber[1:].isdigit():
            print('Nie jest Liczba')
        return moduleNumber
        # patchXmlFile zmienna globalna z ścieżką do pliku xls

    # def showHelp(self):
    #     pass
        # fd = QtGui.QFileDialog(self)
        # file = open('help.txt').read()
        # self.ui.resultWindow.setText(file)


    def startCreateCsvFile(self):

        responsible = self.ui.lineEditCSVUser.text()
        excel_sheet_name = str(self.ui.comboBox.currentText())
        self.importReResultsToCSV = ImportResultsToCSV(responsible=responsible, path_xls_file=pathXlsFile,
                                                       excel_sheet_name=excel_sheet_name)
        self.importReResultsToCSV.start()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec())