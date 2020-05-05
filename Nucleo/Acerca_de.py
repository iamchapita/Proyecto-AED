# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Acerca_de.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Nucleo.Tamaño_Pantalla import Center

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(0)
        MainWindow.setGeometry(QtCore.QRect((sizeObject.height()/2),(sizeObject.width()/2),480,548))
        MainWindow.resize(567, 562)
        MainWindow.setMinimumSize(QtCore.QSize(567, 562))
        MainWindow.setMaximumSize(QtCore.QSize(567, 562))
        font = QtGui.QFont()
        font.setFamily("Hack")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Proyecto1AED/Nucleo/Imagenes/logos-UNAH-600x600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 31))
        self.label.setStyleSheet("color:black;\n"
"\n"
"font: 15pt \"Hack\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 301, 31))
        self.label_2.setStyleSheet("color:black;\n"
"font: 15pt \"Hack\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 171, 31))
        self.label_3.setStyleSheet("color:black;\n"
"font: 15pt \"Hack\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 161, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 200, 181, 21))
        self.label_7.setStyleSheet("color:black;\n"
"font: 15pt \"Hack\";\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 230, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 390, 211, 21))
        self.label_9.setStyleSheet("color:black;\n"
"font: 15pt \"Hack\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 420, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, -20, 531, 461))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../Proyecto1AED/Nucleo/Imagenes/logos-UNAH-600x600.png"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 330, 211, 21))
        self.label_12.setStyleSheet("color:black;\n"
"font: 15pt \"Hack\";\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(60, 360, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(40, 260, 231, 21))
        self.label_14.setStyleSheet("color:black;\n"
"font: 15pt \"Hack\";\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(60, 290, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 450, 231, 21))
        self.label_16.setStyleSheet("color:black;\n"
"font: 15pt \"Hack\";\n"
"")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(60, 480, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"")
        self.label_17.setObjectName("label_17")
        self.label_3.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_10.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Acerca de"))
        self.label.setText(_translate("MainWindow", "Facultad de Ingeniería"))
        self.label_2.setText(_translate("MainWindow", "Ingeniería en Sistemas"))
        self.label_3.setText(_translate("MainWindow", "Integrantes:"))
        self.label_4.setText(_translate("MainWindow", "-William Josué Bonilla"))
        self.label_5.setText(_translate("MainWindow", "-Javier Orlando Viera"))
        self.label_6.setText(_translate("MainWindow", "-Luis Alejandro Morales"))
        self.label_7.setText(_translate("MainWindow", "Docente:"))
        self.label_8.setText(_translate("MainWindow", "Ing. José Inestroza"))
        self.label_9.setText(_translate("MainWindow", "Asignatura:"))
        self.label_10.setText(_translate("MainWindow", "IS-310 Algoritmos y Estructura de Datos"))
        self.label_12.setText(_translate("MainWindow", "Sección:"))
        self.label_13.setText(_translate("MainWindow", "0900"))
        self.label_14.setText(_translate("MainWindow", "Periodo Academico:"))
        self.label_15.setText(_translate("MainWindow", "I PAE"))
        self.label_16.setText(_translate("MainWindow", "Año:"))
        self.label_17.setText(_translate("MainWindow", "2020"))

