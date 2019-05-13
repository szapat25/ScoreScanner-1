from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog
from PyQt5 import QtGui, QtCore, QtWidgets
from Interfaz import *

import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setWindowTitle('ScoreScanner')
        self.setupUi(self)
        boton_Adjuntar = QPushButton('Adjuntar',self)
        boton_Adjuntar.clicked.connect(self.AdjuntarImagen)

    def AdjuntarImagen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
