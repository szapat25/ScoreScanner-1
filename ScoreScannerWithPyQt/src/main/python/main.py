from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog, QProgressBar, QDialog, QMessageBox
from PyQt5 import QtGui, QtCore, QtWidgets, uic
import Interfaz
from Interfaz import *
from Interfaz import Ui_MainWindow
from pymongo import MongoClient
client = MongoClient()
db = client['ScoreScannerDB']

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
        self.frame_Usuario.hide()
        self.progress = QProgressBar(self)
        self.progress.setGeometry(650, 350, 300, 50)
        self.progress.hide()
        self.progress.setMaximum(100)
        self.boton_RegistroP.clicked.connect(self.RegistroPartituras)
        self.boton_Adjuntar.clicked.connect(self.AdjuntarImagen)
        self.boton_Procesar.clicked.connect(self.ProcesarImagen)
        self.boton_GestorP.clicked.connect(self.GestorPartituras)
        self.boton_Usuario.clicked.connect(self.RegistrarUsuario)
         # Setup signals to slots for GUI interaction
        #self.connect(self.ui.connectButton, QtCore.SIGNAL('clicked()'), self.connectButtonClicked)

    def RegistroPartituras(self):
        self.frame_RegistroP.show()
        collection = db['Users']


    def RegistrarUsuario(self):
        self.frame_Usuario.show()

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


    # def connectButtonClicked(self):
      # Connect button was clicked, this method is called    
     # try:
        # Attempt to connect with given host and port
      #  self.connection = Connection(self.ui.hostTextField.text(), int(self.ui.portTextField.text()))
       # print('Connected')
     # except Exception:
      #  errorMessage = 'Error connecting to ' + self.ui.hostTextField.text()
       # print(errorMessage)
        # Alert the user about connection error
       # QtGui.QMessageBox.warning(self, 'Error', errorMessage, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok) 


    

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
