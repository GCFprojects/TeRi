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
        MainWindow.resize(621, 591)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.result_window = QtGui.QTextEdit(self.centralwidget)
        self.result_window.setGeometry(QtCore.QRect(10, 20, 601, 391))
        self.result_window.setObjectName(_fromUtf8("result_window"))
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
        self.logs_button = QtGui.QPushButton(self.centralwidget)
        self.logs_button.setGeometry(QtCore.QRect(130, 520, 101, 31))
        self.logs_button.setObjectName(_fromUtf8("logs_button"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.button_close.setText(_translate("MainWindow", "Zamknij", None))
        self.browse_txt_button.setText(_translate("MainWindow", "Browse", None))
        self.browse_xml_button.setText(_translate("MainWindow", "Browse", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.logs_button.setText(_translate("MainWindow", "Logi", None))
        self.actionZamknij.setText(_translate("MainWindow", "Zamknij", None))
