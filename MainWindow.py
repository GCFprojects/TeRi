# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ImportResultsToExcel import sheets

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
        MainWindow.resize(912, 591)
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
        self.path_txt_window.setObjectName(_fromUtf8("path_txt_window"))
        self.path_xml_window = QtGui.QTextEdit(self.centralwidget)
        self.path_xml_window.setGeometry(QtCore.QRect(10, 470, 471, 31))
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
        # self.comboBox = QtGui.QComboBox(self.excelSheets)
        # self.comboBox.setGeometry(QtCore.QRect(30, 20, 171, 22))
        # self.comboBox.setObjectName(_fromUtf8("comboBox"))
        # # try:
        # #     for item in range(len(sheets())):
        # #         self.comboBox.addItem(_fromUtf8(""))
        # # except TypeError:
        # #     self.comboBox.addItem(_fromUtf8(""))
        # self.comboBox.addItem(_fromUtf8(""))
        self.textBrowser = QtGui.QTextBrowser(self.excelSheets)
        self.textBrowser.setGeometry(QtCore.QRect(100, 50, 131, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.excelSheets)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 100, 131, 31))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.excelSheets)
        self.textBrowser_3.setGeometry(QtCore.QRect(100, 150, 131, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 912, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionZamknij = QtGui.QAction(MainWindow)
        self.actionZamknij.setObjectName(_fromUtf8("actionZamknij"))
        self.load(MainWindow)

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
        self.comboBox.setItemText(0, _translate("MainWindow", "None", None))
        # try:
        #     count = 1
        #     for item in sheets():
        #         self.comboBox.setItemText(count, _translate("MainWindow", item, None))
        #         count += 1
        # except TypeError:
        #     self.comboBox.setItemText(0, _translate("MainWindow", 'None', None))
        self.actionZamknij.setText(_translate("MainWindow", "Zamknij", None))

    def load(self, sheets = None):
        """
        
        :param MainWindow: 
        :param sheets: 
        :return: 
        """
        self.comboBox = QtGui.QComboBox(self.excelSheets)
        self.comboBox.setGeometry(QtCore.QRect(30, 20, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        # self.comboBox.clear()

        try:
            to_fill = list(sheets)
        except Exception as e:
            to_fill = []




        print("###")
        print(to_fill)
        print("##$$$")

        try:
            for item in to_fill:
                self.comboBox.addItem(_fromUtf8("abc"))
        except Exception as e:
            print(e)



                # self.comboBox.addItem(item)

                # self.comboBox.addItem(_fromUtf8(item))


                # self.comboBox.setItemText(0, _translate("MainWindow", item, None))
            # self.comboBox.update()



        # try:
        #     self.comboBox.clear()
        #     for item in range(len(sheets)):
        #         self.comboBox.addItem(_fromUtf8(""))
        #         self.comboBox.setItemText(0, _translate("MainWindow", sheets[item], None))
        #         self.comboBox.update()
        #     # self.retranslateUi(MainWindow)
        #     print(sheets)
        #     # for item in range(len(sheets())):
        #     #     self.comboBox.addItem(_fromUtf8(""))
        # except TypeError:
        #self.comboBox.addItem(_fromUtf8("abc"))
        #self.comboBox.addItem(_fromUtf8("aaa"))
        #self.comboBox.addItem(_fromUtf8("sss"))
        #self.comboBox.addItem(_fromUtf8("d"))
        #self.comboBox.addItem(_fromUtf8("waq"))

        #self.comboBox.addItem(_fromUtf8(""))

