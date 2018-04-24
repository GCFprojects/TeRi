import os
import sys
import xlrd
import time
from PyQt4 import Qt
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
        self.pathTxtFile = ''
        self.pathXlsFile = ''
        # Ustawienie help
        help_file = open('Help.txt').read()
        self.ui.resultWindow.setText(help_file)
        # Ustawienie wartosci poczatkowej dla okien browser`ow
        self.ui.path_txt_window.setText("Browse path to the txt or csv file. Path to results from CMW-500")

        self.ui.path_xls_window.setText("Browse path to the xls file. Path to Excel file where you want put results")

        # Wlasne polaczenia slotow
        QtCore.QObject.connect(self.ui.browse_txt_button, QtCore.SIGNAL("clicked()"), self.browse_txt_file)
        QtCore.QObject.connect(self.ui.browse_xls_button, QtCore.SIGNAL("clicked()"), self.browse_xls_file)
        QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"), self.startProcess)
        self.ui.pushButtonCSVCreate.clicked.connect(self.startCreateCsvFile)
        # QtCore.QObject.connect(self.ui.helpButton, QtCore.SIGNAL("clicked()"), self.showHelp)


        # --------------------------------------------------------------------------
        self.ui.moduleNumber.setText('Z10')
        self.ui.comboBoxLoc.setCurrentIndex(5)


    # Wyszukiwarka plików txt i csv
    def browse_txt_file(self):
        browserTxt = QtGui.QFileDialog(self)
        # self.filename = browserTxt.getOpenFileName(self, 'Open file', os.path.expanduser('~') + '\\Desktop')
        self.filename = browserTxt.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop\\TeRI_Results\\Presentation\\2G\\temp\\KC205')
        if isfile(self.filename):
            plikTxt = open(self.filename)
            if os.path.basename(plikTxt.name)[-4:] == '.txt' or os.path.basename(plikTxt.name)[-4:] == '.csv':
                self.ui.path_txt_window.setText(os.path.basename(plikTxt.name))
                # self.ui.path_txt_window.setText(plikTxt.name)
                self.pathTxtFile = plikTxt.name
                return plikTxt.name
            else:
                self.showDialog(0)

    # Wyszukiwarka plików xls
    def browse_xls_file(self):
        browserXls = QtGui.QFileDialog(self)
        # self.filename = browserXls.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop')
        self.filename = browserXls.getOpenFileName(self, 'Open file', os.path.expanduser('~')+'\\Desktop\\TeRI_Results\\Presentation')
        if isfile(self.filename):
            plikXls = open(self.filename)
            if os.path.basename(plikXls.name)[-4:] == '.xls':
                self.ui.path_xls_window.setText(os.path.basename(plikXls.name))
                # self.ui.path_xls_window.setText(plikXls.name)
                self.pathXlsFile = plikXls.name
                self.update_combobox()
                return plikXls.name
            else:
                self.showDialog(1)

    #
    def update_combobox(self):
        wb=xlrd.open_workbook(self.pathXlsFile)
        sheet = wb.sheet_names()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(list(sheet))

    # Popup informujący o błędnym rozszeżeniu pliku
    def showDialog(self, button=None):
        msg = QtGui.QMessageBox()
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        msg.setText("Information:")
        msg.setModal(True)

        if button == 0:
            msg.setInformativeText("You have selected a file with an incorrect extension.\nChoose an .txt or .csv")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Notification")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)

        elif button == 1:
            msg.setInformativeText("You have selected a file with an incorrect extension.\nChoose an .xls file")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Notification")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)

        elif button == 2:
            msg.setInformativeText("Path to the files have some issue.\nCheck if you properly added both path "
                                   "to CMW-500 result file and excel sheet.")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Warning !!!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)

        elif button == 3:
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setWindowTitle("SUCCESS SUCCESS !!!")
            msg.setInformativeText("Copy results from CMW-500 file to excel was finished successfully !!!\n"
                                   "Great Job mate :)")
        elif button == 4:
            msg.setWindowTitle("Information:")
            msg.setIcon(QtGui.QMessageBox.Question)
            msg.setWindowTitle("Module Number")
            msg.setInformativeText("Do you want to enter results without specifying module number ?")
            msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        elif button == 5:
            msg.setInformativeText("You have an open excel file to whitch you want to enter the results.\n"
                                   "Close excel file and then press \"Start\" again.")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Warning !!!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)

        elif button == 6:
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setWindowTitle("SUCCEC SUCCES !!!")
            msg.setInformativeText("Creating csv file to import results to WebImax was finished successfully !!!\n"
                                   "Great Job mate :)")
        elif button == 7:
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setWindowTitle("Warning !!!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.setInformativeText('No locations entered. It is required parameter.')

        # elif button == 7:
        #     msg.setWindowTitle()

        result = msg.exec_()

        if result == QtGui.QMessageBox.Yes:
            return 'Yes'
        elif result == QtGui.QMessageBox.No:
            return 'No'


    def startProcess(self):

        if self.pathTxtFile != '' and self.pathXlsFile != '':
            if self.ui.comboBoxLoc.currentText() != '':
                location = str(self.ui.comboBoxLoc.currentText()[:4])
                logPatch = start(self.pathTxtFile)
                excelSheetName = str(self.ui.comboBox.currentText())

                if self.ui.automaticTestRun.isChecked():
                    testRunType = 'Automatic'
                elif self.ui.manualTestRun.isChecked():
                    testRunType = 'Manual'

                if self.ui.moduleNumber.text() != '':
                    moduleNumber = self.moduleFormat()
                    result = searchTcInExcel(pathXlsFile=self.pathXlsFile, logPatch=logPatch,
                                             testRunType=testRunType,
                                             moduleNumber=moduleNumber, excelSheetName=excelSheetName,
                                             location=location)
                    if result == 'Done':
                        self.showDialog(3)
                    elif result == 'Excel':
                        self.showDialog(5)
                else:
                    if self.showDialog(4) == 'Yes':
                        moduleNumber = ''
                        result = searchTcInExcel(pathXlsFile=self.pathXlsFile, logPatch=logPatch,
                                                 testRunType=testRunType,
                                                 moduleNumber=moduleNumber, excelSheetName=excelSheetName)
                        if result == 'Done':
                            self.showDialog(3)

            else:
                self.showDialog(7)
            # else:
            #     QtGui.QMessageBox.warning(self, 'Permission denied', 'File '+os.path.basename(self.pathXlsFile)+' is already opened.\n'
            #                                                         'Please close document and start process again',
            #                               QtGui.QMessageBox.Ok)
        else:
            self.showDialog(2)


    def moduleFormat(self):
        moduleNumber = (self.ui.moduleNumber.text()).upper()
        if moduleNumber[0].isdigit():
            print('There is no letter of the module name at the beginning')
        if not moduleNumber[1:].isdigit():
            print('No module number')
        return moduleNumber
        # patchXmlFile zmienna globalna z ścieżką do pliku xls

    # def showHelp(self):
    #     pass
        # fd = QtGui.QFileDialog(self)
        # file = open('help.txt').read()
        # self.ui.resultWindow.setText(file)


    def startCreateCsvFile(self):

        if self.ui.lineEditCSVUser.text() != '':
            responsible = self.ui.lineEditCSVUser.text()
            if self.pathXlsFile != '':
                if self.ui.comboBox.currentText() == '2G' or self.ui.comboBox.currentText() == '3G':
                    excel_sheet_name = str(self.ui.comboBox.currentText())
                    self.importResultsToCSV = ImportResultsToCSV(responsible=responsible,
                                                                 path_xls_file=self.pathXlsFile,
                                                                 excel_sheet_name=excel_sheet_name)
                    self.importResultsToCSV.start()
                else:
                    QtGui.QMessageBox.warning(self, 'Warning',
                                              'TeRI currently supports import to WebImax only for 2G/3G')
            else:
                QtGui.QMessageBox.warning(self, 'Error !!!', 'Browse path to excel sheet with results.\n'
                                                             'It is requaierd to creating csv file.')
        else:
            responsible = ''
            while responsible == '':
                responsible, ok = QtGui.QInputDialog.getText(self, 'Responsibility', 'Enter your login to WebImax:')
                if not ok:
                    QtGui.QMessageBox.warning(self, 'Erorr !!!', 'Login to WebImax is required !!!')
                if ok:
                    self.ui.lineEditCSVUser.setText(responsible)

        try:
            QtGui.QMessageBox.information(self, 'Wait!', 'Work in Progress')
            while self.importResultsToCSV.isRunning():
                time.sleep(1)
            else:
                QtGui.QMessageBox.information(self, 'SUCCEC SUCCES !!!', 'Creating csv file to import results to '
                                                                        'WebImax was finished successfully !!!\n'
                                                                        'Great Job mate :)')
        except AttributeError:
            pass

    def checkExcelStatus(self, xlsFile):
        pass
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec())