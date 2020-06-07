# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QApplication, QMainWindow, QMessageBox, QWidget 
from PyQt5.QtCore import *

from os import system
import datetime
import ast

from Nucleo import Acerca_de 
from Nucleo import Agregar_Pélicula 
from Nucleo import Árbol_Binario_de_Duración
from Nucleo import Árbol_Jerárquico_de_Categorías 
from Nucleo.Tamaño_Pantalla import *
from Nucleo import Ventana_Principal 
from Nucleo import Ver_y_Editar_Péliculas
from Nucleo.Información_Pélicula  import *
from Nucleo.LinkedList import *
from Nucleo.Manejador_de_Archivos import *

ll = LinkedList()
objeto = FileManager()

class Ventana_Principal(QMainWindow, Ventana_Principal.Ui_Principal_MainWindow):
    
    def __init__(self, parent = None):
            
        super(Ventana_Principal, self).__init__(parent)
        self.setupUi(self)
        Center.center(self)
        self.actualizar_desde_JSON()
        self.Acerca_de_button.clicked.connect(self.abrir_Acerca_de) 
        self.Agregar_button.clicked.connect(self.abrir_Agregar_Pelicula) 
        self.Ver_y_editar_button.clicked.connect(self.abrir_Ver_y_Editar)
        self.Numero_label.setText(str(ll.length()))
        
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

    def actualizar_desde_JSON(self):

        dict = ast.literal_eval(objeto.readFile("Memoria/Péliculas_ingresadas.json"))

        print(dict.keys())
        #Falta convertir de JSON a LinkedList
        
    def closeEvent(self, event): 

        cerrar = QMessageBox() 
        cerrar.setIcon(QMessageBox.Warning)
        cerrar.setWindowTitle("Salir") 
        cerrar.setText("<p align='center'>¿Está Seguro?") 
        cerrar.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel) 
        cerrar = cerrar.exec() 

        if cerrar == QMessageBox.Yes:

            event.accept() 

        else:

            event.ignore() 
  
class Acerca_de(QMainWindow, Acerca_de.Ui_MainWindow):

    def __init__(self, parent = None):

        super(Acerca_de, self).__init__(parent)
        self.setupUi(self)
        Center.center(self) 

class Agregar_Pelicula(QMainWindow, Agregar_Pélicula.Ui_Agregar_MainWindow):

    def __init__(self, parent = None ):

        super(Agregar_Pelicula, self).__init__(parent)
        self.setupUi(self)
        Center.center(self) 
        self.Agregar_pushButton.clicked.connect(self.validando_Agregar) 
        self.Cancelar_pushButton.clicked.connect(self.close)

    def closeEvent(self, event2): 

        cerrar1 = QMessageBox()
        cerrar1.setIcon(QMessageBox.Warning)
        cerrar1.setWindowTitle("Salir") 
        cerrar1.setText("<p align='center'>¿Está seguro que desea salir?\n<p align='center'>Esta acción descartará los cambios hechos") 
        cerrar1.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel) 
        cerrar1 = cerrar1.exec()

        if cerrar1 == QMessageBox.Yes:

            self.abrir_Ventana_Principal() 
            event2.accept() 
        
        else:
            
            event2.ignore() 
    
    def validando_Agregar(self): 

        ventana_mensaje = QMessageBox()
        ventana_mensaje.setIcon(QMessageBox.Information)

        cadena = "Campos no válidos:\n"

        if(len(self.Nombre_lineEdit.text()) == 0):
            cadena += "  Nombre de la Pélicula\n"
            
        formato_hora = "%H:%M:%S"
            
        try:
            validtime = datetime.datetime.strptime(self.Duracion_lineEdit.text(), formato_hora)
                
        except ValueError:
            cadena += "  Duración de la Pélicula\n"

        if(len(self.Descripcion_textEdit.toPlainText()) == 0):
            cadena += "  Descripción de la Pélicula\n"

        if(len(self.Director_lineEdit.text()) == 0):
            cadena += "  Director de la Pélicula\n"
        
        if(self.comboBox.currentText() == "----Seleccione un Género----"):
            cadena += "  Género de la Pélicula"

        if(cadena != "Campos no válidos:\n"):

            ventana_mensaje.setWindowTitle("Error") 
            ventana_mensaje.setText("%s"%(cadena)) 
            ventana_mensaje.addButton(QMessageBox.Ok) 
            respuesta = ventana_mensaje.exec()             

        else:
            
            objeto_Pelicula = Info_Pelicula(self.Nombre_lineEdit.text(), self.Duracion_lineEdit.text(), 
            self.Descripcion_textEdit.toPlainText(), self.Director_lineEdit.text(), self.comboBox.currentText())
            ll.push(objeto_Pelicula)
            ventana_mensaje.setWindowTitle("Exito") 
            ventana_mensaje.setText("<p align='center'>Se ha Agregado con Exito") 
            ventana_mensaje.addButton(QMessageBox.Ok) 
            respuesta = ventana_mensaje.exec()
            
            if(respuesta == QMessageBox.Ok):
                
                self.guardar_json()
                ventana_mensaje.close()
                self.abrir_Ventana_Principal() 
            
    def abrir_Ventana_Principal(self): 

        self.Objeto = Ventana_Principal()
        self.Objeto.show() 
        self.hide()

    def guardar_json(self):
        
        current = ll.first
        contador = 0
        json = '{\n'

        while(current):
    
            indice_str = "%s" %(str(contador))
            json += '\t"%s":{\n' %(indice_str)
            json += '\t\t\"nombre":"%s",\n'%(current.value.nombre)
            json += '\t\t\"duracion":"%s",\n'%(current.value.duracion)
            json += '\t\t\"descripcion":"%s",\n'%(current.value.descripcion)
            json += '\t\t\"director":"%s",\n'%(current.value.director)
            json += '\t\t\"genero":"%s"\n'%(current.value.genero)
            
            if(current.next):
                
                json += '\t},\n'
            
            else:
                json += '\t}\n'
                json += '}'

            current = current.next
            contador += 1

        objeto.createFile("Memoria/Péliculas_ingresadas.json", json)
      
class Ver_y_Editar_Peliculas(QMainWindow, Ver_y_Editar_Péliculas.Ui_Ver_y_Editar_MainWindow):

    def __init__(self, parent = None):
        super(Ver_y_Editar_Peliculas, self).__init__(parent)
        self.setupUi(self) 
        Center.center(self)  
    
    def closeEvent(self, event3): 

        cerrar3 = QMessageBox()
        cerrar3.setIcon(QMessageBox.Warning)
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

