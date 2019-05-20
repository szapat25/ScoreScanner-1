from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog, QProgressBar, QDialog, QMessageBox
from PyQt5 import QtGui, QtCore, QtWidgets, uic
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
        #boton_Adjuntar = QPushButton('Adjuntar',self)
        #boton_Adjuntar.clicked.connect(self.AdjuntarImagen)
        self.frame_RegistroP.hide()
        self.frame_GestorP.hide()
        self.progress = QProgressBar(self)
        self.progress.setGeometry(650, 350, 300, 50)
        self.progress.hide()
        self.progress.setMaximum(100)
        self.boton_RegistroP.clicked.connect(self.RegistroPartituras)
        self.boton_Adjuntar.clicked.connect(self.AdjuntarImagen)
        self.boton_Procesar.clicked.connect(self.ProcesarImagen)
        self.boton_GestorP.clicked.connect(self.GestorPartituras)

    def RegistroPartituras(self):
        self.frame_RegistroP.show()

    def GestorPartituras(self):
        self.frame_GestorP.show()

    def AdjuntarImagen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose Contact Icon", "", "Image Files (*.jpg *.pdf)",'/home')
        if fileName:
            print(fileName)
            self.label_Partitura.setPixmap(QtGui.QPixmap(fileName).scaled(731, 491))   
    
    def ProcesarImagen(self):        
        self.progress.show()
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(0.2)
            self.progress.setValue(count)
        self.progress.hide()

        msg = QMessageBox()
        msg.setGeometry(650, 350, 300, 50)
        msg.setIcon(QMessageBox.Information)
        msg.setText("La imagen ha sido procesada")
        msg.setWindowTitle("Proceso Terminado")
        msg.exec_()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
