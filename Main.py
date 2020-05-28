# -*- coding: utf-8 -*-

#Importando archivos necesarios para funcionamiento de la Interfaz
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QApplication, QMainWindow, QMessageBox, QWidget 
from PyQt5.QtCore import *

#Importando Archivo.py donde se construyó la interfaz
#Segundo Commit

import sys
import os

from Nucleo.Acerca_de import *
from Nucleo.Agregar_Pélicula import *
from Nucleo.Árbol_Binario_de_Duración  import *
from Nucleo.Árbol_Jerárquico_de_Categorías import *
from Nucleo.DialogBox_Agregar import *
from Nucleo.DialogBox_Confirmar import *
from Nucleo.Tamaño_Pantalla import *
from Nucleo.Ventana_Principal import *
from Nucleo.Ver_y_Editar_Péliculas import *

#Se crea una subclase  de QMainWindow en donde recibe de parametro la clase Ventana_Principal donde está construida la UI
class Ventana_Principal(QMainWindow):
    
    def __init__(self):

        super(Ventana_Principal, self).__init__() 
        uic.loadUi("Nucleo//Ventana_Principal.ui",self) #Cargando desde .ui la interfaz gráfica
        Center.center(self) #Centrando en pantalla la Ventana Princpal 
        self.Acerca_de_button.clicked.connect(self.abrir_Acerca_de)

    def abrir_Acerca_de(self): #Función para abrir ventana de Acerca de
        self.hide()
        Acerca_de_ventana = Acerca_de(self)
        Acerca_de_ventana.show()
        
    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("¿Estás Seguro?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class Acerca_de(QMainWindow):

    def __init__(self, parent = None):

        super(Acerca_de, self).__init__(parent)
        uic.loadUi("Nucleo//Acerca_de.ui", self) #Configurando todos los parámetros de la QMainWindow
        Center.center(self)

    def closeEvent(self, event):
        
        close = QMessageBox()
        close.setText("¿Estás Seguro?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:

            self.abrir_Ventana_Principal()

            event.accept()

        else:
            event.ignore()
    
    def abrir_Ventana_Principal(self):
        self.parent().show()


#Función Main
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Principal_MainWindow = Ventana_Principal()
    
    Ventana_Principal_MainWindow.show()

    sys.exit(app.exec_())
