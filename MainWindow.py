# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(867, 575)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.resultWindow = QtGui.QTextEdit(self.centralwidget)
        self.resultWindow.setGeometry(QtCore.QRect(10, 10, 601, 391))
        self.resultWindow.setObjectName(_fromUtf8("resultWindow"))
        self.button_close = QtGui.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(500, 520, 101, 31))
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.browse_txt_button = QtGui.QPushButton(self.centralwidget)
        self.browse_txt_button.setGeometry(QtCore.QRect(500, 420, 101, 31))
        self.browse_txt_button.setObjectName(_fromUtf8("browse_txt_button"))
        self.browse_xml_button = QtGui.QPushButton(self.centralwidget)
        self.browse_xml_button.setGeometry(QtCore.QRect(500, 470, 101, 31))
        self.browse_xml_button.setObjectName(_fromUtf8("browse_xml_button"))
        self.path_txt_window = QtGui.QTextEdit(self.centralwidget)
        self.path_txt_window.setGeometry(QtCore.QRect(10, 420, 471, 31))
        self.path_txt_window.setReadOnly(True)
        self.path_txt_window.setOverwriteMode(True)
        self.path_txt_window.setObjectName(_fromUtf8("path_txt_window"))
        self.path_xml_window = QtGui.QTextEdit(self.centralwidget)
        self.path_xml_window.setGeometry(QtCore.QRect(10, 470, 471, 31))
        self.path_xml_window.setReadOnly(True)
        self.path_xml_window.setOverwriteMode(True)
        self.path_xml_window.setObjectName(_fromUtf8("path_xml_window"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 520, 101, 31))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.logsButton = QtGui.QPushButton(self.centralwidget)
        self.logsButton.setGeometry(QtCore.QRect(130, 520, 101, 31))
        self.logsButton.setObjectName(_fromUtf8("logsButton"))
        self.excelSheets = QtGui.QGroupBox(self.centralwidget)
        self.excelSheets.setGeometry(QtCore.QRect(620, 10, 241, 211))
        self.excelSheets.setFlat(False)
        self.excelSheets.setCheckable(False)
        self.excelSheets.setObjectName(_fromUtf8("excelSheets"))
        self.comboBox = QtGui.QComboBox(self.excelSheets)
        self.comboBox.setGeometry(QtCore.QRect(30, 20, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.textBrowser = QtGui.QTextBrowser(self.excelSheets)
        self.textBrowser.setGeometry(QtCore.QRect(100, 50, 131, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.excelSheets)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 100, 131, 31))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.excelSheets)
        self.textBrowser_3.setGeometry(QtCore.QRect(100, 150, 131, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label = QtGui.QLabel(self.excelSheets)
        self.label.setGeometry(QtCore.QRect(50, 50, 51, 31))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.excelSheets)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 61, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.excelSheets)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 51, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.testRunType = QtGui.QGroupBox(self.centralwidget)
        self.testRunType.setGeometry(QtCore.QRect(620, 230, 241, 121))
        self.testRunType.setObjectName(_fromUtf8("testRunType"))
        self.automaticTestRun = QtGui.QRadioButton(self.testRunType)
        self.automaticTestRun.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.automaticTestRun.setChecked(True)
        self.automaticTestRun.setObjectName(_fromUtf8("automaticTestRun"))
        self.manualTestRun = QtGui.QRadioButton(self.testRunType)
        self.manualTestRun.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.manualTestRun.setChecked(False)
        self.manualTestRun.setObjectName(_fromUtf8("manualTestRun"))
        self.moduleNumber = QtGui.QLineEdit(self.testRunType)
        self.moduleNumber.setGeometry(QtCore.QRect(110, 80, 111, 20))
        self.moduleNumber.setText(_fromUtf8(""))
        self.moduleNumber.setObjectName(_fromUtf8("moduleNumber"))
        self.label_4 = QtGui.QLabel(self.testRunType)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionZamknij = QtGui.QAction(MainWindow)
        self.actionZamknij.setObjectName(_fromUtf8("actionZamknij"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TeRI", None))
        self.button_close.setText(_translate("MainWindow", "Zamknij", None))
        self.browse_txt_button.setText(_translate("MainWindow", "Browse", None))
        self.browse_xml_button.setText(_translate("MainWindow", "Browse", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.logsButton.setText(_translate("MainWindow", "Logi", None))
        self.excelSheets.setTitle(_translate("MainWindow", "Wybierz zakładkę z excel`a", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "2G", None))
        self.label.setText(_translate("MainWindow", "Wynik:", None))
        self.label_2.setText(_translate("MainWindow", "Czas:", None))
        self.label_3.setText(_translate("MainWindow", "Moduł: ", None))
        self.testRunType.setTitle(_translate("MainWindow", "Wyniki", None))
        self.automaticTestRun.setText(_translate("MainWindow", "Automatic", None))
        self.manualTestRun.setText(_translate("MainWindow", "Manual", None))
        self.label_4.setText(_translate("MainWindow", "Podaj nr. modułu:", None))
        self.actionZamknij.setText(_translate("MainWindow", "Zamknij", None))

