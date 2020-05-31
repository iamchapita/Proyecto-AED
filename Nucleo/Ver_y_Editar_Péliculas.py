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
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(0)
        Ver_y_Editar_MainWindow.setGeometry(QtCore.QRect((sizeObject.height()/2),(sizeObject.width()/2),480,548))
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 721, 331))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(40, 300, 641, 16))
        self.horizontalScrollBar.setStyleSheet("background-color:rgb(204, 204, 204);")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.verticalScrollBar.setGeometry(QtCore.QRect(690, 30, 20, 251))
        self.verticalScrollBar.setStyleSheet("background-color:rgb(204, 204, 204);")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.ID_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ID_textEdit.setGeometry(QtCore.QRect(153, 360, 131, 71))
        self.ID_textEdit.setStyleSheet("color:black;\n"
"font: 75 10pt \"Hack\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"")
        self.ID_textEdit.setObjectName("ID_textEdit")
        self.Editar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Editar_pushButton.setGeometry(QtCore.QRect(310, 360, 161, 71))
        self.Editar_pushButton.setStyleSheet("background-color: rgb(211, 137, 9);\n"
"font: 10pt \"Hack\";\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"border-radius: 35px;")
        self.Editar_pushButton.setObjectName("Editar_pushButton")
        self.Borrar_pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Borrar_pushButton_2.setGeometry(QtCore.QRect(480, 360, 161, 71))
        self.Borrar_pushButton_2.setStyleSheet("background-color: rgb(255, 41, 41);\n"
"font: 10pt \"Hack\";\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"border-radius: 35px;")
        self.Borrar_pushButton_2.setObjectName("Borrar_pushButton_2")
        Ver_y_Editar_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ver_y_Editar_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Ver_y_Editar_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Ver_y_Editar_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Ver_y_Editar_MainWindow)

    def retranslateUi(self, Ver_y_Editar_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Ver_y_Editar_MainWindow.setWindowTitle(_translate("Ver_y_Editar_MainWindow", "Ver y Editar Péliculas"))
        self.ID_textEdit.setPlaceholderText(_translate("Ver_y_Editar_MainWindow", "Ingrese el número del ID a Editar o Borrar"))
        self.Editar_pushButton.setText(_translate("Ver_y_Editar_MainWindow", "Editar"))
        self.Borrar_pushButton_2.setText(_translate("Ver_y_Editar_MainWindow", "Borrar"))
