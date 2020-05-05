# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Árbol_Jerárquico_de_Categorías.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Arbol_Jerarquico_MainWindow(object):

    def setupUi(self, Arbol_Jerarquico_MainWindow):

        Arbol_Jerarquico_MainWindow.setObjectName("Arbol_Jerarquico_MainWindow")
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(0)
        Arbol_Jerarquico_MainWindow.setGeometry(QtCore.QRect((sizeObject.height()/2),(sizeObject.width()/2),480,548))
        Arbol_Jerarquico_MainWindow.resize(753, 425)
        Arbol_Jerarquico_MainWindow.setMinimumSize(QtCore.QSize(753, 425))
        Arbol_Jerarquico_MainWindow.setMaximumSize(QtCore.QSize(753, 425))
        font = QtGui.QFont()
        font.setFamily("Hack")
        Arbol_Jerarquico_MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Python/Nucleo/Imagenes/logos-UNAH-600x600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Arbol_Jerarquico_MainWindow.setWindowIcon(icon)
        Arbol_Jerarquico_MainWindow.setStyleSheet("background-color:rgb(204, 204, 204);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Arbol_Jerarquico_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 731, 381))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        Arbol_Jerarquico_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Arbol_Jerarquico_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Arbol_Jerarquico_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Arbol_Jerarquico_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Arbol_Jerarquico_MainWindow)

    def retranslateUi(self, Arbol_Jerarquico_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Arbol_Jerarquico_MainWindow.setWindowTitle(_translate("Arbol_Jerarquico_MainWindow", "Árbol Jerárquico de Categorías"))
