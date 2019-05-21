from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5 import *
#from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog, QProgressBar, QDialog, QMessageBox
#from PyQt5 import QtGui, QtCore, QtWidgets, uic
import Interfaz
from Interfaz import *
from Interfaz import Ui_MainWindow
#from pymongo import Connection

import sys
import time

TIME_LIMIT = 100

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle('ScoreScanner')
        self.resize(1300, 720)
        self.setMinimumSize(1300, 720)
        self.setMaximumSize(1300,720)        
        
        self.boton_RegistroP.clicked.connect(self.RegistroPartituras)
        self.boton_GestorP.clicked.connect(self.GestorPartituras)
        self.boton_Usuario.clicked.connect(self.Usuario)

        self.frame_RegistroP.hide()
        self.frame_GestorP.hide()
        self.frame_Usuario.hide()

    
    def RegistroPartituras(self):
        self.mdiArea.addSubWindow(self.frame_GestorP.hide())
        self.mdiArea.addSubWindow(self.frame_Usuario.hide())
        self.mdiArea.addSubWindow(self.frame_RegistroP.show())

    def GestorPartituras(self):
        self.mdiArea.addSubWindow(self.frame_RegistroP.hide())
        self.mdiArea.addSubWindow(self.frame_Usuario.hide())
        self.mdiArea.addSubWindow(self.frame_GestorP.show())

    def Usuario(self):
        self.mdiArea.addSubWindow(self.frame_RegistroP.hide())
        self.mdiArea.addSubWindow(self.frame_GestorP.hide())
        self.mdiArea.addSubWindow(self.frame_Usuario.show())
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
