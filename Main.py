# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QApplication, QMainWindow, QMessageBox, QWidget 
from PyQt5.QtCore import *

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

class Ventana_Principal(QMainWindow):
    
    def __init__(self, parent = None):

        super(Ventana_Principal, self).__init__(parent) 
        uic.loadUi("Nucleo//Ventana_Principal.ui",self) 
        Center.center(self) 
        self.Acerca_de_button.clicked.connect(self.abrir_Acerca_de) 
        self.Agregar_button.clicked.connect(self.abrir_Agregar_Pelicula) 
        self.Ver_y_editar_button.clicked.connect(self.abrir_Ver_y_Editar)

    def abrir_Acerca_de(self): 

        self.Acerca_de_ventana = Acerca_de()
        self.Acerca_de_ventana.show() 
    
    def abrir_Agregar_Pelicula(self): 
        self.hide() 
        self.Agregar_Pelicula_ventana = Agregar_Pelicula()
        self.Agregar_Pelicula_ventana.show() 
    
    def abrir_Ver_y_Editar(self): 
        self.hide()
        self.Ver_y_Editar_ventana = Ver_y_Editar_Peliculas()
        self.Ver_y_Editar_ventana.show() 
    
    def closeEvent(self, event): 

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
        uic.loadUi("Nucleo//Acerca_de.ui", self) 
        Center.center(self) 


class Agregar_Pelicula(QMainWindow):

    def __init__(self, parent = None ):

        super(Agregar_Pelicula, self).__init__(parent)
        uic.loadUi("Nucleo//Agregar_Pélicula.ui", self)
        Center.center(self) 
        self.Agregar_pushButton.clicked.connect(self.revison_Agregar) 
        self.Cancelar_pushButton.clicked.connect(self.close) 

    def closeEvent(self, event2): 

        cerrar1 = QMessageBox() 
        cerrar1.setWindowTitle("Salir") 
        cerrar1.setText("<p align='center'>¿Está seguro que desea salir?\n<p align='center'>Esta acción descartará los cambios hechos") 
        cerrar1.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel) 
        cerrar1 = cerrar1.exec()

        if cerrar1 == QMessageBox.Yes:

            self.abrir_Ventana_Principal() 
            event2.accept() 
        
        else:
            
            event2.ignore() 
    
    def revison_Agregar(self): 

        exitoso = QMessageBox() 
        exitoso.setWindowTitle("Exito") 
        exitoso.setText("<p align='center'>Se ha Agregado con Exito") 
        exitoso.addButton(QMessageBox.Ok) 
        respuesta = exitoso.exec() 

        if(respuesta == QMessageBox.Ok):

            exitoso.close()
            self.abrir_Ventana_Principal() 
    
    def abrir_Ventana_Principal(self): 
        self.Objeto = Ventana_Principal()
        self.Objeto.show() 
        self.hide() 

class Ver_y_Editar_Peliculas(QMainWindow):

    def __init__(self, parent = None):
        super(Ver_y_Editar_Peliculas, self).__init__(parent)
        uic.loadUi("Nucleo//Ver_y_Editar_Péliculas.ui", self) 
        Center.center(self)  
    
    def closeEvent(self, event3): 

        cerrar3 = QMessageBox() 
        cerrar3.setWindowTitle("Salir")
        cerrar3.setText("<p align='center'>¿Está seguro que desea salir?")
        cerrar3.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel) 
        cerrar3 = cerrar3.exec() 

        if cerrar3 == QMessageBox.Yes:

            self.abrir_Ventana_Principal() 
            event3.accept() 
        
        else:
            
            event3.ignore() 

    def abrir_Ventana_Principal(self): 
        self.Objeto = Ventana_Principal()
        self.Objeto.show()
        self.hide()

#Función Main
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Principal_MainWindow = Ventana_Principal()
    
    Ventana_Principal_MainWindow.show()

    sys.exit(app.exec_())
