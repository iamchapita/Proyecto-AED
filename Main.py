# -*- coding: utf-8 -*-

#Importando archivos necesarios para funcionamiento de la Interfaz
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QApplication

#Importando Archivo.py donde se construyó la interfaz
#Segundo Commit
import sys
import os

from Nucleo import Acerca_de
from Nucleo.Acerca_de import *
from Nucleo import Agregar_Pélicula
from Nucleo import Árbol_Binario_de_Duración
from Nucleo import Árbol_Jerárquico_de_Categorías
from Nucleo import DialogBox_Agregar
from Nucleo import DialogBox_Confirmar
from Nucleo import Interfaz_rc
from Nucleo.Tamaño_Pantalla import Center
from Nucleo import Ventana_Principal
from Nucleo import Ver_y_Editar_Péliculas

"""
NO SE NECESITA

Se crea una subclase  de QMainWindow en donde recibe de parametro la clase Acerca_de donde está construida la UI
class Acerca_de(QtWidgets.QMainWindow, Acerca_de.Ui_MainWindow):

    def __init__(self, parent = None):

        super(Acerca_de, self).__init__(parent)
        self.setupUi(self) #Configurando todos los parámetros de la QMainWindow
        Center.center(self)
"""
#Se crea una subclase  de QMainWindow en donde recibe de parametro la clase Ventana_Principal donde está construida la UI
class Ventana_Principal(QtWidgets.QMainWindow, Ventana_Principal.Ui_Principal_MainWindow):
    
    def __init__(self, parent=None):

        super(Ventana_Principal,self).__init__(parent)
        self.setupUi(self) #Configurando todos los parámetros de la QMainWindow
        Center.center(self)
        
#Función Main
def main():

    app = QApplication(sys.argv) #Creando una instancia de QApplication para poder controlar el blucle infinito de pintado
    VentanaPrincipal = Ventana_Principal()

    VentanaPrincipal.show()
    sys.exit(app.exec_()) #Ejecutando el bucle infinito de pintado

if __name__ == '__main__':
    main()

