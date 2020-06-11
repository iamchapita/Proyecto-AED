# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ver_y_Editar_Péliculas.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ver_y_Editar_MainWindow(object):
    def setupUi(self, Ver_y_Editar_MainWindow):
        Ver_y_Editar_MainWindow.setObjectName("Ver_y_Editar_MainWindow")
        Ver_y_Editar_MainWindow.resize(762, 456)
        Ver_y_Editar_MainWindow.setMinimumSize(QtCore.QSize(762, 456))
        Ver_y_Editar_MainWindow.setMaximumSize(QtCore.QSize(762, 456))
        font = QtGui.QFont()
        font.setFamily("Hack")
        Ver_y_Editar_MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Nucleo/Imagenes/logos-UNAH-600x600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ver_y_Editar_MainWindow.setWindowIcon(icon)
        Ver_y_Editar_MainWindow.setStyleSheet("background-color:rgb(204, 204, 204);")
        self.centralwidget = QtWidgets.QWidget(Ver_y_Editar_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Editar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Editar_pushButton.setGeometry(QtCore.QRect(310, 360, 161, 71))
        self.Editar_pushButton.setStyleSheet("background-color: rgb(211, 137, 9);\n"
"font: 10pt \"Hack\";\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"border-radius: 35px;")
        self.Editar_pushButton.setObjectName("Editar_pushButton")
        self.Borrar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Borrar_pushButton.setGeometry(QtCore.QRect(480, 360, 161, 71))
        self.Borrar_pushButton.setStyleSheet("background-color: rgb(255, 41, 41);\n"
"font: 10pt \"Hack\";\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"border-radius: 35px;")
        self.Borrar_pushButton.setObjectName("Borrar_pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 721, 321))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("font: 8pt \"Hack\";\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;")
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setLineWrapColumnOrWidth(0)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        self.ID_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_regex = QtCore.QRegExp("[0-9]+")
        self.ID_validator = QtGui.QRegExpValidator(self.ID_regex, self.ID_lineEdit)
        self.ID_lineEdit.setValidator(self.ID_validator)
        self.ID_lineEdit.setGeometry(QtCore.QRect(40, 380, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(8)
        self.ID_lineEdit.setFont(font)
        self.ID_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ID_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ID_lineEdit.setObjectName("ID_lineEdit")
        Ver_y_Editar_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ver_y_Editar_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Ver_y_Editar_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Ver_y_Editar_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Ver_y_Editar_MainWindow)

    def retranslateUi(self, Ver_y_Editar_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Ver_y_Editar_MainWindow.setWindowTitle(_translate("Ver_y_Editar_MainWindow", "Ver y Editar Péliculas"))
        self.Editar_pushButton.setText(_translate("Ver_y_Editar_MainWindow", "Editar"))
        self.Borrar_pushButton.setText(_translate("Ver_y_Editar_MainWindow", "Borrar"))
        self.ID_lineEdit.setPlaceholderText(_translate("Ver_y_Editar_MainWindow", "N° de Item a borrar o eliminar"))
