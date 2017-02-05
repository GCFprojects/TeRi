import os, sys

from PyQt4 import QtCore, QtGui
from TeRi import *
from os.path import isfile

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Ustawienie wartosci poczatkowej dla okien browser`ow
        self.ui.path_txt_window.setText("Wskarz ścieżkę do pliku txt")
        self.ui.path_xml_window.setText("Wskarz ścieżkę do pliku xml")
        # Wlasne polaczenia slotow
        QtCore.QObject.connect(self.ui.browse_txt_button, QtCore.SIGNAL("clicked()"), self.file_browse_txt_file)
        QtCore.QObject.connect(self.ui.browse_xml_button, QtCore.SIGNAL("clicked()"), self.file_browse_xml_file)

    def file_browse_txt_file(self):
        browserTxt = QtGui.QFileDialog(self)
        self.filename = browserTxt.getOpenFileName()
        if isfile(self.filename):
            plikTxt = open(self.filename)
            if os.path.basename(plikTxt.name)[-4:] == '.txt' or os.path.basename(plikTxt.name)[-4:] == '.csv':
                self.ui.path_txt_window.setText(plikTxt.name)
            else:
                print("Hej txt")
            #print(os.path.basename(plikTxt.name)[-4:])

    def file_browse_xml_file(self):
        browserXml = QtGui.QFileDialog(self)
        self.filename = browserXml.getOpenFileName()
        if isfile(self.filename):
            plikXml = open(self.filename)
            if os.path.basename(plikXml.name)[-4:] == '.xml':
                self.ui.path_xml_window.setText(plikXml.name)
            else:
                print("Hej xml")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec())
