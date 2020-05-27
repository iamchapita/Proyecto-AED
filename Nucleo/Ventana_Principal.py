# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_Principal.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
import sys
import os

from Nucleo.Acerca_de import *
from Nucleo.Tamaño_Pantalla import Center
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QApplication
from Nucleo.Ver_y_Editar_Péliculas import Ui_Ver_y_Editar_MainWindow
from Nucleo.Árbol_Jerárquico_de_Categorías import Ui_Arbol_Jerarquico_MainWindow
from Nucleo.Árbol_Binario_de_Duración import Ui_Arbol_Binario_MainWindow
#from Tamaño_Pantalla import Center


class Ui_Principal_MainWindow(object):

        
        def setupUi(self, Principal_MainWindow):
        

                Principal_MainWindow.setObjectName("Principal_MainWindow")
                sizeObject = QtWidgets.QDesktopWidget().screenGeometry(0)
                Principal_MainWindow.setGeometry(QtCore.QRect((sizeObject.height()/2),(sizeObject.width()/2),480,548))
                Principal_MainWindow.setMinimumSize(QtCore.QSize(480, 548))
                Principal_MainWindow.setMaximumSize(QtCore.QSize(480, 548))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(
                        "../Proyecto1AED/Nucleo/Imagenes/logos-UNAH-600x600.png"), 
                        QtGui.QIcon.Normal, QtGui.QIcon.Off
                        )
                Principal_MainWindow.setWindowIcon(icon)
                Principal_MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.centralwidget = QtWidgets.QWidget(Principal_MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.Agregar_button = QtWidgets.QPushButton(self.centralwidget)
                self.Agregar_button.setGeometry(QtCore.QRect(90, 320, 301, 61))
                self.Agregar_button.setStyleSheet("background-color: rgb(146, 196, 125);\n"
        "font: 10pt \"Hack\";\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 0.5px;\n"
        "border-radius: 30px;")
                self.Agregar_button.setShortcut("")
                self.Agregar_button.setDefault(False)
                self.Agregar_button.setFlat(False)
                self.Agregar_button.setObjectName("Agregar_button")
                self.Ver_y_editar_button = QtWidgets.QPushButton(self.centralwidget)
                self.Ver_y_editar_button.setGeometry(QtCore.QRect(90, 390, 301, 61))
                self.Ver_y_editar_button.setStyleSheet("background-color: rgb(254, 217, 102);\n"
        "font: 10pt \"Hack\";\n"
        "color: rgb(188, 145, 15);\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 0.5px;\n"
        "border-radius: 30px;")
                self.Ver_y_editar_button.setShortcut("")
                self.Ver_y_editar_button.setDefault(False)
                self.Ver_y_editar_button.setFlat(False)
                self.Ver_y_editar_button.setObjectName("Ver_y_editar_button")
                self.Visualizacion_button = QtWidgets.QPushButton(self.centralwidget)
                self.Visualizacion_button.setGeometry(QtCore.QRect(90, 460, 301, 61))
                self.Visualizacion_button.setStyleSheet("background-color: rgb(109, 158, 235);\n"
        "font: 10pt \"Hack\";\n"
        "color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 0.5px;\n"
        "border-radius: 30px;")
                self.Visualizacion_button.setShortcut("")
                self.Visualizacion_button.setDefault(False)
                self.Visualizacion_button.setFlat(False)
                self.Visualizacion_button.setObjectName("Visualizacion_button")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(100, 250, 301, 41))
                self.label.setStyleSheet("font-size:35px;\n"
        "color:black;")
                self.label.setObjectName("label")
                self.Acerca_de_button = QtWidgets.QPushButton(self.centralwidget)
                self.Acerca_de_button.setGeometry(QtCore.QRect(340, 10, 131, 61))
                self.Acerca_de_button.setStyleSheet("background-color: rgb(141, 124, 194);\n"
        "font: 10pt \"Hack\";\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 0.5px;\n"
        "border-radius: 30px;")
                self.Acerca_de_button.setShortcut("")
                self.Acerca_de_button.setDefault(False)
                self.Acerca_de_button.setFlat(False)
                self.Acerca_de_button.setObjectName("Acerca_de_button")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(200, 120, 131, 101))
                self.label_2.setStyleSheet("color:black;\n"
        "font: 70pt \"Hack\";\n"
        "")
                self.label_2.setScaledContents(False)
                self.label_2.setObjectName("label_2")
                Principal_MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(Principal_MainWindow)
                self.statusbar.setObjectName("statusbar")
                Principal_MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(Principal_MainWindow)
                QtCore.QMetaObject.connectSlotsByName(Principal_MainWindow)

        def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
                
            else:
                event.ignore()
                
        def retranslateUi(self, Principal_MainWindow):
                _translate = QtCore.QCoreApplication.translate
                Principal_MainWindow.setWindowTitle(_translate("Principal_MainWindow", "Principal"))
                self.Agregar_button.setText(_translate("Principal_MainWindow", "Agregar"))
                self.Ver_y_editar_button.setText(_translate("Principal_MainWindow", "Ver y Editar Listado"))
                self.Visualizacion_button.setText(_translate("Principal_MainWindow", "Visualización de Árbol"))
                self.label.setText(_translate("Principal_MainWindow", "Péliculas en total"))
                self.Acerca_de_button.setText(_translate("Principal_MainWindow", "Acerca de"))
                self.label_2.setText(_translate("Principal_MainWindow", "0"))

