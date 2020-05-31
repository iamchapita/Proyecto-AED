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

#Clase que hereda de QMainWindow donde se carga la UI de Ventana_Principal y se crean todos los métodos necesario para su
#funcionamiento
class Ventana_Principal(QMainWindow):
    
    def __init__(self, parent = None):

        super(Ventana_Principal, self).__init__(parent) 
        uic.loadUi("Nucleo//Ventana_Principal.ui",self) #Cargando desde .ui la interfaz gráfica
        Center.center(self) #Heredado de la clase Center en Tamaño_Pantalla.py que centra la ventana en la pantalla
        self.Acerca_de_button.clicked.connect(self.abrir_Acerca_de) #Conecta el botón al método que abre la ventana Acerca de
        self.Agregar_button.clicked.connect(self.abrir_Agregar_Pelicula) #Conecta el botón al método que abre la ventana Agregar
        self.Ver_y_editar_button.clicked.connect(self.abrir_Ver_y_Editar)

    def abrir_Acerca_de(self): #Función para abrir ventana de Acerca de

        self.Acerca_de_ventana = Acerca_de()
        self.Acerca_de_ventana.show() #Muestra la ventana Acerca de
    
    def abrir_Agregar_Pelicula(self): #Función para abrir ventana Agregar Pélicula
        self.hide() #Oculta la ventana Principal mientras se muestra la ventana de Agregar Pélicula
        self.Agregar_Pelicula_ventana = Agregar_Pelicula()
        self.Agregar_Pelicula_ventana.show() #Muestra la ventana Agregar Pélicula
    
    def abrir_Ver_y_Editar(self): #Función para abrir ventana Ver y Editar Péliculas
        self.hide()
        self.Ver_y_Editar_ventana = Ver_y_Editar_Peliculas()
        self.Ver_y_Editar_ventana.show() #Muestra la ventana Acerca de
    
    def closeEvent(self, event): #Funcion para mostrar Dialogo de cierre de ventana

        cerrar = QMessageBox() #Crea una Ventana de Mensaje
        cerrar.setWindowTitle("Salir") #Cambia si titulo
        cerrar.setText("<p align='center'>¿Está Seguro?") #Cambia el contenido de la ventana
        cerrar.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel) #Establece los botones de la ventana
        cerrar = cerrar.exec() #Ejecuta la ventana

        if cerrar == QMessageBox.Yes:

            event.accept() #Acepta el vento de cerrado y termina la ejecución del programa cerrando la Ventana Principal

        else:

            event.ignore() #Ignora el evento y sigue mostrando la ventana Principal
  
#Clase que hereda de QMainWindow en donde se carga la UI de Acerca de y se instancian todos los métodos para el funcionamiento
#de su interfaz
class Acerca_de(QMainWindow):

    def __init__(self, parent = None):

        super(Acerca_de, self).__init__(parent)
        uic.loadUi("Nucleo//Acerca_de.ui", self) #Configurando todos los parámetros de la QMainWindow
        Center.center(self) #Heredado de la clase Center en Tamaño_Pantalla.py que centra la ventana en la pantalla

#Clase que hereda de QMainWindow en donde se carga la UI de la ventana Agregar Pélicula y se instancian todos los métodos 
# para el funcionamiento de su interfaz
class Agregar_Pelicula(QMainWindow):

    def __init__(self, parent = None ):

        super(Agregar_Pelicula, self).__init__(parent)
        uic.loadUi("Nucleo//Agregar_Pélicula.ui", self)#Cargando desde .ui la interfaz gráfica
        Center.center(self) #Heredado de la clase Center en Tamaño_Pantalla.py que centra la ventana en la pantalla
        self.Agregar_pushButton.clicked.connect(self.revison_Agregar) #Conecta el botón Agregar con el método para revisar si están conrrectos los campos
        self.Cancelar_pushButton.clicked.connect(self.close) #Conecta el botón Cancelar con la función para cerrar la ventana Agregar

    def closeEvent(self, event2): #Funcion para mostrar Dialogo de cierre de ventana

        cerrar1 = QMessageBox() #Crea una Ventana de Mensaje
        cerrar1.setWindowTitle("Salir") #Cambia si titulo
        cerrar1.setText("<p align='center'>¿Está seguro que desea salir?\n<p align='center'>Esta acción descartará los cambios hechos") #Establece el texto de la Ventana
        cerrar1.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel) #Crea los botones de la Ventana
        cerrar1 = cerrar1.exec() #Ejecuta la Ventana

        if cerrar1 == QMessageBox.Yes:

            self.abrir_Ventana_Principal() #Método que oculta la ventana Agregar y muestra la ventana Principal
            event2.accept() #Acepta el Evento de Cierre
        
        else:
            
            event2.ignore() #Ignora el Evento de Cierre y mantiene abierta la ventana Agrega Pélicula
    
    def revison_Agregar(self): #Este método envia un mensaje de exitoso si los campos están llenos correctamente

        exitoso = QMessageBox() #Crea una Ventana de Mensaje
        exitoso.setWindowTitle("Exito") #Cambia si titulo
        exitoso.setText("<p align='center'>Se ha Agregado con Exito") #Establece el texto de la Ventana
        exitoso.addButton(QMessageBox.Ok) #Crea los botones de la Ventana
        respuesta = exitoso.exec() #Ejecuta la Ventana

        if(respuesta == QMessageBox.Ok):

            exitoso.close()
            self.abrir_Ventana_Principal() #Llama al método
    
    def abrir_Ventana_Principal(self): #Función que oculta le ventana Agregar Pélicula y muestra le Ventana Principal
        self.Objeto = Ventana_Principal()
        self.Objeto.show() #Muestra la Ventana Principal
        self.hide() #Oculta la ventana Agrega Pélicula

#Clase que hereda de QMainWindow en donde se carga la UI de la Ventana Ver y Editar Péliculas y se instancias todos sus métodos
class Ver_y_Editar_Peliculas(QMainWindow):

    def __init__(self, parent = None):
        super(Ver_y_Editar_Peliculas, self).__init__(parent)
        uic.loadUi("Nucleo//Ver_y_Editar_Péliculas.ui", self) #Cargando desde .ui la interfaz gráfica
        Center.center(self)  #Heredado de la clase Center en Tamaño_Pantalla.py que centra la ventana en la pantalla
    
    def closeEvent(self, event3): #Funcion para mostrar Dialogo de cierre de ventana

        cerrar3 = QMessageBox() #Crea una Ventana de Mensaje
        cerrar3.setWindowTitle("Salir") #Cambia si titulo
        cerrar3.setText("<p align='center'>¿Está seguro que desea salir?") #Establece el texto de la Ventana
        cerrar3.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel) #Crea los botones de la Ventana
        cerrar3 = cerrar3.exec() #Ejecuta la Ventana

        if cerrar3 == QMessageBox.Yes:

            self.abrir_Ventana_Principal() #Método que oculta la ventana Ver y Editar Péliculas y muestra la ventana Principal
            event3.accept() #Acepta el Evento de Cierre
        
        else:
            
            event3.ignore() #Ignora el Evento de Cierre y mantiene abierta la ventana Ver y Editar Pélicula

    def abrir_Ventana_Principal(self): #Función que oculta le ventana Ver y Editar Péliculas y muestra le Ventana Principal
        self.Objeto = Ventana_Principal()
        self.Objeto.show() #Muestra la Ventana Principal
        self.hide() #Oculta la ventana Ver y Editar Péliculas

#Función Main
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Principal_MainWindow = Ventana_Principal()
    
    Ventana_Principal_MainWindow.show()

    sys.exit(app.exec_())
