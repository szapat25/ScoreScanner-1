# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alejandra/ProyectoP1/ScoreScanner/ScoreScannerWithPyQt/src/main/python/Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 720)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(186, 199, 208);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_SSL = QtWidgets.QLabel(self.centralwidget)
        self.label_SSL.setGeometry(QtCore.QRect(0, 0, 211, 71))
        self.label_SSL.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.label_SSL.setObjectName("label_SSL")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_logo.setStyleSheet("border-image: url(:/Icons/logo.png);\n"
"background-color: rgb(105, 105, 105);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.label_ScoreScanner = QtWidgets.QLabel(self.centralwidget)
        self.label_ScoreScanner.setGeometry(QtCore.QRect(70, 10, 111, 51))
        self.label_ScoreScanner.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.label_ScoreScanner.setObjectName("label_ScoreScanner")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 70, 211, 611))
        self.listView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView.setObjectName("listView")
        self.boton_Usuario = QtWidgets.QPushButton(self.centralwidget)
        self.boton_Usuario.setGeometry(QtCore.QRect(20, 200, 81, 27))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.boton_Usuario.setFont(font)
        self.boton_Usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;")
        self.boton_Usuario.setObjectName("boton_Usuario")
        self.label_Dashboard = QtWidgets.QLabel(self.centralwidget)
        self.label_Dashboard.setGeometry(QtCore.QRect(10, 176, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_Dashboard.setFont(font)
        self.label_Dashboard.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Dashboard.setObjectName("label_Dashboard")
        self.label_Partituras = QtWidgets.QLabel(self.centralwidget)
        self.label_Partituras.setGeometry(QtCore.QRect(10, 340, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_Partituras.setFont(font)
        self.label_Partituras.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Partituras.setObjectName("label_Partituras")
        self.boton_RegistroP = QtWidgets.QPushButton(self.centralwidget)
        self.boton_RegistroP.setGeometry(QtCore.QRect(20, 370, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.boton_RegistroP.setFont(font)
        self.boton_RegistroP.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;")
        self.boton_RegistroP.setObjectName("boton_RegistroP")
        self.boton_GestorP = QtWidgets.QPushButton(self.centralwidget)
        self.boton_GestorP.setGeometry(QtCore.QRect(20, 420, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.boton_GestorP.setFont(font)
        self.boton_GestorP.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;")
        self.boton_GestorP.setObjectName("boton_GestorP")
        self.label_Extras = QtWidgets.QLabel(self.centralwidget)
        self.label_Extras.setGeometry(QtCore.QRect(10, 600, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_Extras.setFont(font)
        self.label_Extras.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Extras.setObjectName("label_Extras")
        self.boton_AboutUs = QtWidgets.QPushButton(self.centralwidget)
        self.boton_AboutUs.setGeometry(QtCore.QRect(20, 620, 81, 27))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.boton_AboutUs.setFont(font)
        self.boton_AboutUs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;")
        self.boton_AboutUs.setObjectName("boton_AboutUs")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 0, 1081, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.frame_RegistroP = QtWidgets.QFrame(self.centralwidget)
        self.frame_RegistroP.setGeometry(QtCore.QRect(230, 90, 1061, 581))
        self.frame_RegistroP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_RegistroP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_RegistroP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_RegistroP.setObjectName("frame_RegistroP")
        self.line = QtWidgets.QFrame(self.frame_RegistroP)
        self.line.setGeometry(QtCore.QRect(27, 40, 1011, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.frame_RegistroP)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 241, 31))
        self.label_2.setObjectName("label_2")
        self.boton_Adjuntar = QtWidgets.QPushButton(self.frame_RegistroP)
        self.boton_Adjuntar.setGeometry(QtCore.QRect(80, 110, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.boton_Adjuntar.setFont(font)
        self.boton_Adjuntar.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.boton_Adjuntar.setObjectName("boton_Adjuntar")
        self.boton_Procesar = QtWidgets.QPushButton(self.frame_RegistroP)
        self.boton_Procesar.setGeometry(QtCore.QRect(80, 260, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.boton_Procesar.setFont(font)
        self.boton_Procesar.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.boton_Procesar.setObjectName("boton_Procesar")
        self.boton_Descargar = QtWidgets.QPushButton(self.frame_RegistroP)
        self.boton_Descargar.setGeometry(QtCore.QRect(80, 410, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.boton_Descargar.setFont(font)
        self.boton_Descargar.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.boton_Descargar.setObjectName("boton_Descargar")
        self.label_Partitura = QtWidgets.QLabel(self.frame_RegistroP)
        self.label_Partitura.setGeometry(QtCore.QRect(280, 80, 731, 491))
        self.label_Partitura.setText("")
        self.label_Partitura.setObjectName("label_Partitura")
        self.frame_GestorP = QtWidgets.QFrame(self.frame_RegistroP)
        self.frame_GestorP.setGeometry(QtCore.QRect(0, 0, 1061, 581))
        self.frame_GestorP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_GestorP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_GestorP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_GestorP.setObjectName("frame_GestorP")
        self.line_2 = QtWidgets.QFrame(self.frame_GestorP)
        self.line_2.setGeometry(QtCore.QRect(27, 40, 1011, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_GestorP = QtWidgets.QLabel(self.frame_GestorP)
        self.label_GestorP.setGeometry(QtCore.QRect(40, 10, 241, 31))
        self.label_GestorP.setObjectName("label_GestorP")
        self.label_3 = QtWidgets.QLabel(self.frame_GestorP)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Cherokee")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.boton_Autor = QtWidgets.QPushButton(self.frame_GestorP)
        self.boton_Autor.setGeometry(QtCore.QRect(60, 150, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.boton_Autor.setFont(font)
        self.boton_Autor.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: solid;\n"
"border-radius:15px;\n"
"")
        self.boton_Autor.setObjectName("boton_Autor")
        self.boton_Titulo = QtWidgets.QPushButton(self.frame_GestorP)
        self.boton_Titulo.setGeometry(QtCore.QRect(60, 260, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.boton_Titulo.setFont(font)
        self.boton_Titulo.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: solid;\n"
"border-radius:15px;\n"
"")
        self.boton_Titulo.setObjectName("boton_Titulo")
        self.boton_Id = QtWidgets.QPushButton(self.frame_GestorP)
        self.boton_Id.setGeometry(QtCore.QRect(60, 380, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.boton_Id.setFont(font)
        self.boton_Id.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: solid;\n"
"border-radius:15px;\n"
"")
        self.boton_Id.setObjectName("boton_Id")
        self.boton_Genero = QtWidgets.QPushButton(self.frame_GestorP)
        self.boton_Genero.setGeometry(QtCore.QRect(60, 500, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.boton_Genero.setFont(font)
        self.boton_Genero.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: solid;\n"
"border-radius:15px;\n"
"")
        self.boton_Genero.setObjectName("boton_Genero")
        self.spinBox_Autor = QtWidgets.QSpinBox(self.frame_GestorP)
        self.spinBox_Autor.setGeometry(QtCore.QRect(250, 160, 771, 31))
        self.spinBox_Autor.setObjectName("spinBox_Autor")
        self.spinBox_Titulo = QtWidgets.QSpinBox(self.frame_GestorP)
        self.spinBox_Titulo.setGeometry(QtCore.QRect(250, 270, 771, 31))
        self.spinBox_Titulo.setObjectName("spinBox_Titulo")
        self.spinBox_Id = QtWidgets.QSpinBox(self.frame_GestorP)
        self.spinBox_Id.setGeometry(QtCore.QRect(250, 390, 771, 31))
        self.spinBox_Id.setObjectName("spinBox_Id")
        self.spinBox_Genero = QtWidgets.QSpinBox(self.frame_GestorP)
        self.spinBox_Genero.setGeometry(QtCore.QRect(250, 510, 771, 31))
        self.spinBox_Genero.setObjectName("spinBox_Genero")
        self.listView.raise_()
        self.label_SSL.raise_()
        self.label_logo.raise_()
        self.label_ScoreScanner.raise_()
        self.boton_Usuario.raise_()
        self.label_Dashboard.raise_()
        self.label_Partituras.raise_()
        self.boton_RegistroP.raise_()
        self.boton_GestorP.raise_()
        self.label_Extras.raise_()
        self.boton_AboutUs.raise_()
        self.horizontalLayoutWidget.raise_()
        self.frame_RegistroP.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_Partitura.setBuddy(self.label_Partitura)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_SSL.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_ScoreScanner.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Score</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Scanner </span></p></body></html>"))
        self.boton_Usuario.setText(_translate("MainWindow", "Usuario"))
        self.label_Dashboard.setText(_translate("MainWindow", "Dashboard"))
        self.label_Partituras.setText(_translate("MainWindow", "Partituras"))
        self.boton_RegistroP.setText(_translate("MainWindow", "Registro de partituras"))
        self.boton_GestorP.setText(_translate("MainWindow", "Gestor de partituras"))
        self.label_Extras.setText(_translate("MainWindow", "Extras"))
        self.boton_AboutUs.setText(_translate("MainWindow", "About us"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">@Username</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Registro de Partituras</span></p></body></html>"))
        self.boton_Adjuntar.setText(_translate("MainWindow", "Adjuntar"))
        self.boton_Procesar.setText(_translate("MainWindow", "Procesar"))
        self.boton_Descargar.setText(_translate("MainWindow", "Descargar"))
        self.label_GestorP.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Gestor de Partituras</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Búsqueda por:</span></p></body></html>"))
        self.boton_Autor.setText(_translate("MainWindow", "Autor"))
        self.boton_Titulo.setText(_translate("MainWindow", "Título"))
        self.boton_Id.setText(_translate("MainWindow", "ID"))
        self.boton_Genero.setText(_translate("MainWindow", "Género"))


import logo_rc
