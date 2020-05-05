# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Agregar_Pélicula.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Agregar_MainWindow(object):

    def setupUi(self, Agregar_MainWindow):
            
        Agregar_MainWindow.setObjectName("Agregar_MainWindow")
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(0)
        Agregar_MainWindow.setGeometry(QtCore.QRect((sizeObject.height()/2),(sizeObject.width()/2),480,548))
        Agregar_MainWindow.resize(762, 479)
        Agregar_MainWindow.setMinimumSize(QtCore.QSize(762, 479))
        Agregar_MainWindow.setMaximumSize(QtCore.QSize(762, 479))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Python/Nucleo/Imagenes/logos-UNAH-600x600.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Agregar_MainWindow.setWindowIcon(icon)
        Agregar_MainWindow.setStyleSheet("background-color:rgb(204, 204, 204);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Agregar_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Descripcion_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Descripcion_textEdit.setGeometry(QtCore.QRect(40, 140, 681, 131))
        self.Descripcion_textEdit.setStyleSheet("color:black;\n"
"font: 10pt \"Hack\";\n"
"border-width: 3px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Descripcion_textEdit.setObjectName("Descripcion_textEdit")
        self.Nombre_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Nombre_lineEdit.setGeometry(QtCore.QRect(40, 30, 681, 34))
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.Nombre_lineEdit.setFont(font)
        self.Nombre_lineEdit.setStyleSheet("QLineEdit{\n"
"color:black;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit::{\n"
"sizeHint(10);\n"
"}")
        self.Nombre_lineEdit.setText("")
        self.Nombre_lineEdit.setMaxLength(25)
        self.Nombre_lineEdit.setClearButtonEnabled(True)
        self.Nombre_lineEdit.setObjectName("Nombre_lineEdit")
        self.Duracion_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Duracion_lineEdit.setGeometry(QtCore.QRect(40, 80, 681, 34))
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.Duracion_lineEdit.setFont(font)
        self.Duracion_lineEdit.setStyleSheet("QLineEdit{\n"
"color:black;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit::{\n"
"sizeHint(10);\n"
"}")
        self.Duracion_lineEdit.setText("")
        self.Duracion_lineEdit.setMaxLength(8)
        self.Duracion_lineEdit.setClearButtonEnabled(True)
        self.Duracion_lineEdit.setObjectName("Duracion_lineEdit")
        self.Director_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Director_lineEdit.setGeometry(QtCore.QRect(40, 290, 681, 34))
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.Director_lineEdit.setFont(font)
        self.Director_lineEdit.setStyleSheet("QLineEdit{\n"
"color:black;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit::{\n"
"sizeHint(10);\n"
"}")
        self.Director_lineEdit.setText("")
        self.Director_lineEdit.setMaxLength(50)
        self.Director_lineEdit.setClearButtonEnabled(True)
        self.Director_lineEdit.setObjectName("Director_lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 340, 681, 34))
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color:black;\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Agregar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Agregar_pushButton.setGeometry(QtCore.QRect(230, 390, 131, 61))
        self.Agregar_pushButton.setStyleSheet("background-color: rgb(119, 174, 255);\n"
"font: 10pt \"Hack\";\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"border-radius: 30px;")
        self.Agregar_pushButton.setShortcut("")
        self.Agregar_pushButton.setDefault(False)
        self.Agregar_pushButton.setFlat(False)
        self.Agregar_pushButton.setObjectName("Agregar_pushButton")
        self.Cancelar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Cancelar_pushButton.setGeometry(QtCore.QRect(380, 390, 131, 61))
        self.Cancelar_pushButton.setStyleSheet("background-color: rgb(255, 115, 115);\n"
"font: 10pt \"Hack\";\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 0.5px;\n"
"border-radius: 30px;")
        self.Cancelar_pushButton.setShortcut("")
        self.Cancelar_pushButton.setDefault(False)
        self.Cancelar_pushButton.setFlat(False)
        self.Cancelar_pushButton.setObjectName("Cancelar_pushButton")
        Agregar_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Agregar_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Agregar_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Agregar_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Agregar_MainWindow)

    def retranslateUi(self, Agregar_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Agregar_MainWindow.setWindowTitle(_translate("Agregar_MainWindow", "Agregar Pélicula"))
        self.Descripcion_textEdit.setHtml(_translate("Agregar_MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hack\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Noto Sans\';\"><br /></p></body></html>"))
        self.Descripcion_textEdit.setPlaceholderText(_translate("Agregar_MainWindow", "Descripción de la Pélicula"))
        self.Nombre_lineEdit.setPlaceholderText(_translate("Agregar_MainWindow", "Nombre de Pélicula"))
        self.Duracion_lineEdit.setPlaceholderText(_translate("Agregar_MainWindow", "Duración de la Pélicula(HH:MM:SS)"))
        self.Director_lineEdit.setPlaceholderText(_translate("Agregar_MainWindow", "Director de la Pélicula"))
        self.comboBox.setCurrentText(_translate("Agregar_MainWindow", "----Seleccione un Género----"))
        self.comboBox.setItemText(0, _translate("Agregar_MainWindow", "----Seleccione un Género----"))
        self.comboBox.setItemText(1, _translate("Agregar_MainWindow", "Hechos Reales"))
        self.comboBox.setItemText(2, _translate("Agregar_MainWindow", "Bélicas "))
        self.comboBox.setItemText(3, _translate("Agregar_MainWindow", "Comedias Musicales"))
        self.comboBox.setItemText(4, _translate("Agregar_MainWindow", "Acción"))
        self.comboBox.setItemText(5, _translate("Agregar_MainWindow", "Artes marciales"))
        self.comboBox.setItemText(6, _translate("Agregar_MainWindow", "Aventuras"))
        self.comboBox.setItemText(7, _translate("Agregar_MainWindow", "Ciencia ficción "))
        self.comboBox.setItemText(8, _translate("Agregar_MainWindow", "Comedia"))
        self.comboBox.setItemText(9, _translate("Agregar_MainWindow", "Dibujos animados "))
        self.comboBox.setItemText(10, _translate("Agregar_MainWindow", "Documental "))
        self.comboBox.setItemText(11, _translate("Agregar_MainWindow", "Espada y Hechicería "))
        self.comboBox.setItemText(12, _translate("Agregar_MainWindow", "Espionaje"))
        self.comboBox.setItemText(13, _translate("Agregar_MainWindow", "Horror"))
        self.comboBox.setItemText(14, _translate("Agregar_MainWindow", "Misterio "))
        self.comboBox.setItemText(15, _translate("Agregar_MainWindow", "Muertos vivientes "))
        self.comboBox.setItemText(16, _translate("Agregar_MainWindow", "Propaganda"))
        self.comboBox.setItemText(17, _translate("Agregar_MainWindow", "Suspenso"))
        self.comboBox.setItemText(18, _translate("Agregar_MainWindow", "Terror"))
        self.comboBox.setItemText(19, _translate("Agregar_MainWindow", "Deportivas"))
        self.comboBox.setItemText(20, _translate("Agregar_MainWindow", "Dramáticas"))
        self.comboBox.setItemText(21, _translate("Agregar_MainWindow", "Fantásticas"))
        self.comboBox.setItemText(22, _translate("Agregar_MainWindow", "Infantiles"))
        self.comboBox.setItemText(23, _translate("Agregar_MainWindow", "Musicales"))
        self.comboBox.setItemText(24, _translate("Agregar_MainWindow", "Policíacas"))
        self.comboBox.setItemText(25, _translate("Agregar_MainWindow", "Psicológicas"))
        self.comboBox.setItemText(26, _translate("Agregar_MainWindow", "Románticas"))
        self.comboBox.setItemText(27, _translate("Agregar_MainWindow", "Sobre animales"))
        self.comboBox.setItemText(28, _translate("Agregar_MainWindow", "Sobre aviación"))
        self.comboBox.setItemText(29, _translate("Agregar_MainWindow", "Sobre delincuencia"))
        self.comboBox.setItemText(30, _translate("Agregar_MainWindow", "Sobre discapacitados"))
        self.comboBox.setItemText(31, _translate("Agregar_MainWindow", "Sobre religión"))
        self.comboBox.setItemText(32, _translate("Agregar_MainWindow", "Sobre política"))
        self.Agregar_pushButton.setText(_translate("Agregar_MainWindow", "Agregar"))
        self.Cancelar_pushButton.setText(_translate("Agregar_MainWindow", "Cancelar"))
