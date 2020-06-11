# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_Principal.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Principal_MainWindow(object):

    def setupUi(self, Principal_MainWindow):
        Principal_MainWindow.setObjectName("Principal_MainWindow")
        Principal_MainWindow.resize(480, 548)
        Principal_MainWindow.setMinimumSize(QtCore.QSize(480, 548))
        Principal_MainWindow.setMaximumSize(QtCore.QSize(480, 548))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Nucleo/Imagenes/logos-UNAH-600x600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Principal_MainWindow.setWindowIcon(icon)
        Principal_MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Principal_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Agregar_Principal_button = QtWidgets.QPushButton(self.centralwidget)
        self.Agregar_Principal_button.setGeometry(QtCore.QRect(90, 320, 301, 61))
        self.Agregar_Principal_button.setStyleSheet("background-color: rgb(146, 196, 125);\n"
"font: 10pt \"Hack\";\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"border-radius: 30px;")
        self.Agregar_Principal_button.setShortcut("")
        self.Agregar_Principal_button.setDefault(False)
        self.Agregar_Principal_button.setFlat(False)
        self.Agregar_Principal_button.setObjectName("Agregar_button")
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
        self.Numero_label = QtWidgets.QLabel(self.centralwidget)
        self.Numero_label.setGeometry(QtCore.QRect(180, 120, 131, 101))
        self.Numero_label.setStyleSheet("color:black;\n"
"font: 70pt \"Hack\";\n"
"")
        self.Numero_label.setScaledContents(False)
        self.Numero_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Numero_label.setObjectName("Numero_label")
        self.Ver_y_editar_button = QtWidgets.QPushButton(self.centralwidget)
        self.Ver_y_editar_button.setGeometry(QtCore.QRect(90, 390, 301, 61))
        self.Ver_y_editar_button.setStyleSheet("background-color: rgb(254, 217, 102);\n"
"font: 10pt \"Hack\";\n"
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
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"border-radius: 30px;")
        self.Visualizacion_button.setShortcut("")
        self.Visualizacion_button.setDefault(False)
        self.Visualizacion_button.setFlat(False)
        self.Visualizacion_button.setObjectName("Visualizacion_button")
        Principal_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Principal_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Principal_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Principal_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Principal_MainWindow)

    def retranslateUi(self, Principal_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Principal_MainWindow.setWindowTitle(_translate("Principal_MainWindow", "Principal"))
        self.Agregar_Principal_button.setText(_translate("Principal_MainWindow", "Agregar"))
        self.label.setText(_translate("Principal_MainWindow", "Péliculas en total"))
        self.Acerca_de_button.setText(_translate("Principal_MainWindow", "Acerca de"))
        self.Numero_label.setText(_translate("Principal_MainWindow", "0"))
        self.Ver_y_editar_button.setText(_translate("Principal_MainWindow", "Ver y Editar Péliculas"))
        self.Visualizacion_button.setText(_translate("Principal_MainWindow", "Visualización de Árbol"))


