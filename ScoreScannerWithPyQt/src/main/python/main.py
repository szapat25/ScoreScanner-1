from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog
from PyQt5 import QtGui, QtCore, QtWidgets, uic
import Interfaz
from Interfaz import *
from Interfaz import Ui_MainWindow

import sys


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
        self.boton_RegistroP.clicked.connect(self.RegistroPartituras)
        #self.boton_cerrarRP.clicked.connect(self.CerrarFrame(self.frame_RegistroP))
        self.boton_Adjuntar.clicked.connect(self.AdjuntarImagen)

    def RegistroPartituras(self):
        self.frame_RegistroP.show()

    def AdjuntarImagen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose Contact Icon", "", "Image Files (*.jpg *.pdf)",'/home')
        if fileName:
            print(fileName)
            self.label_Partitura.setPixmap(QtGui.QPixmap(fileName).scaled(731, 491))

        
    
    # def CerrarFrame(self, frameACerrar):
    #     frameACerrar.hide()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
