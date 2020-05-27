# -*- coding: utf-8 -*-

#Importando archivos necesarios para funcionamiento de la Interfaz
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QApplication, QMainWindow, QMessageBox, QWidget 

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

"""
class Acerca_de(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi("Nucleo//Acerca_de.ui", self) #Configurando todos los parámetros de la QMainWindow
        Center.center(self)
"""
#Se crea una subclase  de QMainWindow en donde recibe de parametro la clase Ventana_Principal donde está construida la UI
class Ventana_Principal(QMainWindow):
    
    def __init__(self):

        super().__init__() 
        uic.loadUi("Nucleo//Ventana_Principal.ui",self) #Cargando desde .ui la interfaz gráfica
        Center.center(self) #Centrando en pantalla la Ventana Princpal 
    
        self.Acerca_de_button.clicked.connect(self.Acerca_de_window)
       
    """def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Cierre de Ventana', '¿Desea cerrar esta ventana?', 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                event.accept()
                
            else:
                event.ignore()
    """
    
    def Acerca_de_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        Center.center(self.window)
        self.window.show()
        
        
#Función Main
def main():

    app = QApplication(sys.argv) #Creando una instancia de QApplication para poder controlar el blucle infinito de pintado
    VentanaPrincipal = Ventana_Principal()

    VentanaPrincipal.show()
    sys.exit(app.exec_()) #Ejecutando el bucle infinito de pintado

if __name__ == '__main__':
    main()

