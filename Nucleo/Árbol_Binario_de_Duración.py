# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Árbol_Binario_de_Duración.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Arbol_Binario_MainWindow(object):

    def setupUi(self, Arbol_Binario_MainWindow):
        
        Arbol_Binario_MainWindow.setObjectName("Arbol_Binario_MainWindow")
        Arbol_Binario_MainWindow.resize(753, 432)
        Arbol_Binario_MainWindow.setMinimumSize(QtCore.QSize(753, 432))
        Arbol_Binario_MainWindow.setMaximumSize(QtCore.QSize(753, 432))
        font = QtGui.QFont()
        font.setFamily("Hack")
        Arbol_Binario_MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Python/Nucleo/Imagenes/logos-UNAH-600x600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Arbol_Binario_MainWindow.setWindowIcon(icon)
        Arbol_Binario_MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Arbol_Binario_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 731, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(10, 360, 691, 16))
        self.horizontalScrollBar.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.verticalScrollBar.setGeometry(QtCore.QRect(710, 10, 16, 331))
        self.verticalScrollBar.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        Arbol_Binario_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Arbol_Binario_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Arbol_Binario_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Arbol_Binario_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Arbol_Binario_MainWindow)

    def retranslateUi(self, Arbol_Binario_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Arbol_Binario_MainWindow.setWindowTitle(_translate("Arbol_Binario_MainWindow", "Árbol Binario de Duración"))
