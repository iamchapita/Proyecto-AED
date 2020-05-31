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
    
    def __init__(self, parent = None):

        super(Ventana_Principal, self).__init__(parent) 
        uic.loadUi("Nucleo//Ventana_Principal.ui",self) #Cargando desde .ui la interfaz gráfica
        Center.center(self) #Centrando en pantalla la Ventana Princpal 
        self.Acerca_de_button.clicked.connect(self.abrir_Acerca_de)
        self.Agregar_button.clicked.connect(self.abrir_Agregar_Pelicula)

    def abrir_Acerca_de(self): #Función para abrir ventana de Acerca de
        self.hide()
        Acerca_de_ventana = Acerca_de(self)
        Acerca_de_ventana.show()
    
    def abrir_Agregar_Pelicula(self):
        self.hide()
        Agregar_Pelicula_ventana = Agregar_Pelicula(self)
        Agregar_Pelicula_ventana.show()
        
    def closeEvent(self, event): #Funcion para mostrar Dialogo de cierre de ventana

        cerrar = QMessageBox()
        cerrar.setWindowTitle("Salir")
        cerrar.setText("<p align='center'>¿Está Seguro?")
        cerrar.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        cerrar = cerrar.exec()

        if cerrar == QMessageBox.Yes:

            event.accept()

        else:

            event.ignore()
    
class Acerca_de(QMainWindow):

    def __init__(self, parent = None):

        super(Acerca_de, self).__init__(parent)
        uic.loadUi("Nucleo//Acerca_de.ui", self) #Configurando todos los parámetros de la QMainWindow
        Center.center(self)

    def closeEvent(self, event1): #Evento para controlar que la ventana Acerca de

        self.parent().show()
        event1.accept()
    

class Agregar_Pelicula(QMainWindow):

    def __init__(self, parent = None):

        super(Agregar_Pelicula, self).__init__(parent)
        uic.loadUi("Nucleo//Agregar_Pélicula.ui", self)
        Center.center(self)
        self.Agregar_pushButton.clicked.connect(self.abrir_Ventana_Principal)
        #self.Cancelar_pushButton.clicked.connect(self.closeEvent)

    def closeEvent(self, event2): #Funcion para mostrar Dialogo de cierre de ventana

        cerrar1 = QMessageBox()
        cerrar1.setWindowTitle("Salir")
        cerrar1.setText("¿Está seguro que desea salir?\nEsta acción descartará los cambios hechos")
        cerrar1.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        cerrar1 = cerrar1.exec()

        if cerrar1 == QMessageBox.Yes:

            self.parent().show()
            event2.accept()
        
        else:
            
            event2.ignore()
    
    def abrir_Ventana_Principal(self):
        self.hide()
        self.parent().show()

#Función Main
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Principal_MainWindow = Ventana_Principal()
    
    Ventana_Principal_MainWindow.show()

    sys.exit(app.exec_())
