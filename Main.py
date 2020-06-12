# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QApplication, QMainWindow, QMessageBox, QWidget, QButtonGroup
#from PyQt5.QtCore import 

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
posicion = 0

class Ventana_Principal(QMainWindow, Ventana_Principal.Ui_Principal_MainWindow):
    
    def __init__(self, parent = None):
            
        super(Ventana_Principal, self).__init__(parent)
        self.setupUi(self)
        Center.center(self)
        self.actualizar_desde_JSON()
        self.Acerca_de_button.clicked.connect(self.abrir_Acerca_de) 
        self.Agregar_Principal_button.clicked.connect(self.abrir_Agregar_Pelicula) 
        self.Ver_y_editar_button.clicked.connect(self.abrir_Ver_y_Editar)
        self.Numero_label.setText(str(ll.length()))
        self.Visualizacion_button.clicked.connect(self.abrir_visualizacion)

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

    def abrir_visualizacion(self):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setWindowTitle("Ay")
        mensaje.setText("No hay nada\nVuelva Pronto")
        mensaje.exec()
        respuesta = mensaje.addButton(QMessageBox.Ok)

        if(respuesta == QMessageBox.Ok):
            mensaje.close()

    def actualizar_desde_JSON(self):

        if(objeto.readFile("Memoria/Péliculas_ingresadas.json") and ll.length() == 0):
        
            dict = ast.literal_eval(objeto.readFile("Memoria/Péliculas_ingresadas.json"))
            for i in range((len(dict))):
                
                #temp = str(count)
                var = str(dict[str(i)])
                var = var.split("'")
                instanica_Pelicula = Info_Pelicula(var[3], var[7], var[11], var[15], var[19])
                ll.push(instanica_Pelicula)
        
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

    def __init__(self, parent = None):

        super(Agregar_Pelicula, self).__init__(parent)
        self.setupUi(self)
        Center.center(self)
        self.Cancelar_pushButton.clicked.connect(self.close)
        self.Agregar_pushButton.clicked.connect(self.validando_Agregar)

    def closeEvent(self, event2): 

        boolean = False
        #Boolean True si están vacios los campos

        if(self.Nombre_lineEdit.text() == ""):
            boolean = True
            
        if(self.Duracion_lineEdit.text() == ""):
            boolean = True

        if(self.Descripcion_textEdit.toPlainText() == ""):
            boolean = True

        if(self.Director_lineEdit.text() == ""):
            boolean = True

        if(self.comboBox.currentText() == ""):
            boolean = True

        if(boolean == False):

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

        else:
            self.abrir_Ventana_Principal()

    def keyPressEvent(self, event):
        
        if(self.Agregar_pushButton.hasFocus() and event.key() == QtCore.Qt.Key_Return):

            self.Agregar_pushButton.click()

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
            
            temp = self.Descripcion_textEdit.toPlainText()
            temp = temp.replace("\n"," ")
            objeto_Pelicula = Info_Pelicula(self.Nombre_lineEdit.text(), self.Duracion_lineEdit.text(), 
            temp, self.Director_lineEdit.text(), self.comboBox.currentText())
            ll.push(objeto_Pelicula)
            ventana_mensaje.setWindowTitle("Exito") 
            ventana_mensaje.setText("<p align='center'>Se ha Agregado con Exito") 
            ventana_mensaje.addButton(QMessageBox.Ok) 
            respuesta = ventana_mensaje.exec()
            
            if(respuesta == QMessageBox.Ok):
                
                self.guardar_json()
                ventana_mensaje.close()
                self.abrir_Ventana_Principal() 

    def guardar_json(self):
        
        current = ll.first

        if(current):

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

        else:
            json = ""
            objeto.createFile("Memoria/Péliculas_ingresadas.json", json)        

    def abrir_Ventana_Principal(self): 

        self.Objeto = Ventana_Principal()
        self.Objeto.show() 
        self.hide()

class Ver_y_Editar_Peliculas(QMainWindow, Ver_y_Editar_Péliculas.Ui_Ver_y_Editar_MainWindow):

    def __init__(self, parent = None):
        super(Ver_y_Editar_Peliculas, self).__init__(parent)
        self.setupUi(self)
        Center.center(self)
        self.textEdit.setPlainText(self.cargar_ASCII())
        self.Editar_pushButton.clicked.connect(self.validar_editar)
        self.Borrar_pushButton.clicked.connect(self.eliminar)
        self.Agregar_Objeto = Agregar_Pelicula()
        self.Agregar_Objeto.Agregar_pushButton.disconnect()
        self.Agregar_Objeto.Agregar_pushButton.clicked.connect(self.modificar_entrada)

    def keyPressEvent(self, event):

        self.Editar_pushButton.setFocus()

        if(self.Editar_pushButton.hasFocus() and event.key() == QtCore.Qt.Key_Return):
            self.validar_editar()
            
    def closeEvent(self, event3): 

        if(self.ID_lineEdit.text() != ""):

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
        
        self.abrir_Ventana_Principal()

    def abrir_Ventana_Principal(self): 
        self.Objeto = Ventana_Principal()
        self.Objeto.show()
        self.hide()

    def cargar_ASCII(self):

        prueba = ("--"*84)
        prueba += "\n"
        prueba += "\t\t\t\t\t\tInventario de Productos"
        prueba += "\n"
        prueba += ("--"*84)
        prueba += "\n"
        prueba += "id    | Nombre                                           | Duración    | Descripción                                | Director               | Género                  |"
        prueba += "\n"
        prueba += ("--"*84)
        prueba += "\n"

        current = ll.first
        count = 1

        while(current):

            prueba += ("%s%s%s" %(str(count)," "*(6-len(str(count))),"|"))
            nombre = current.value.nombre
            h, m, s = current.value.duracion.split(":")
            tiempo = int(h)*3600 + int(m)*60 + int(s)
            descripcion = current.value.descripcion
            director = current.value.director
            genero = current.value.genero

            prueba += (" %s%s%s"%(nombre, " "*(49-len(nombre)),"|"))
            prueba += (" %s seg.%s%s"%(str(tiempo), " "*(7-len(str(tiempo))),"|"))
            
            if(len(descripcion) > 44):
                descripcion = descripcion[0:40]
                descripcion += "..."
                prueba += (" %s%s" %(descripcion,"|"))
            
            else:
                prueba += (" %s%s%s" %(descripcion," "*(43-len(descripcion)), "|"))
            
            if(len(director) > 24):
                director = director[0:20]
                director += "..."
                prueba += (" %s%s" %(director, "|"))

            else:
                prueba += (" %s%s%s" %(director, " "*(23-len(director)),"|"))
            
            prueba += (" %s%s%s" %(genero, " "*(24-len(genero)),"|"))
            prueba += "\n"
            prueba += ("--"*84)
            prueba += "\n"
            count += 1
            current = current.next
        
        return prueba
        
    def validar_editar(self):
        
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
    
        try:
            ID = int(self.ID_lineEdit.text())-1

            if(int(ID) < 0 or int(ID)+1 > ll.length()):

                mensaje.setWindowTitle("Error")
                mensaje.setText("Error, el ID ingresado no es válido")
                mensaje.addButton(QMessageBox.Ok)
                mensaje.exec()

            else:

                mensaje.setWindowTitle("Editar")
                mensaje.setText("¿Está seguro que desea editar el elemento %d?" %(int(ID)+1))
                mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                respuesta = mensaje.exec()

                if(respuesta == QMessageBox.Yes):
                    
                    self.hide()
                    current, pos = ll.search(ID)
                    global posicion
                    posicion = pos
                    self.Agregar_Objeto.Nombre_lineEdit.setText(current.value.nombre)
                    self.Agregar_Objeto.Duracion_lineEdit.setText(current.value.duracion)
                    self.Agregar_Objeto.Descripcion_textEdit.setText(current.value.descripcion)
                    self.Agregar_Objeto.Director_lineEdit.setText(current.value.director)
                    self.Agregar_Objeto.show()
                    self.Agregar_Objeto.comboBox.setCurrentText(current.value.genero)

        except ValueError:
            
            mensaje.setWindowTitle("Error")
            mensaje.setText("Error, el ID ingresado no es válido")
            mensaje.addButton(QMessageBox.Ok)
            mensaje.exec()    
    
    def modificar_entrada(self):
            
        global posicion
        current, posicion_editar = ll.search(posicion)

        boolean = False
        #Boolean True si se ha modificado algo

        if(self.Agregar_Objeto.Nombre_lineEdit.isModified()):
            boolean = True
            
        if(self.Agregar_Objeto.Duracion_lineEdit.isModified()):
            boolean = True

        if(self.Agregar_Objeto.Descripcion_textEdit.toPlainText() is current.value.descripcion):
            boolean = True

        if(self.Agregar_Objeto.Director_lineEdit.isModified()):
            boolean = True

        if(self.Agregar_Objeto.comboBox.currentText() != current.value.genero):
            boolean = True
        
        if(boolean):
            self.validar_campos_editados()
        
    def validar_campos_editados(self):
        
        global posicion

        ventana_mensaje = QMessageBox()
        ventana_mensaje.setIcon(QMessageBox.Information)

        cadena = "Campos no válidos:\n"
        
        if(len(self.Agregar_Objeto.Nombre_lineEdit.text()) == 0):
            cadena += "  Nombre de la Pélicula\n"
            
        formato_hora = "%H:%M:%S"
            
        try:
            validtime = datetime.datetime.strptime(self.Agregar_Objeto.Duracion_lineEdit.text(), formato_hora)
                
        except ValueError:
            cadena += "  Duración de la Pélicula\n"

        if(len(self.Agregar_Objeto.Descripcion_textEdit.toPlainText()) == 0):
            cadena += "  Descripción de la Pélicula\n"

        if(len(self.Agregar_Objeto.Director_lineEdit.text()) == 0):
            cadena += "  Director de la Pélicula\n"
        
        if(self.Agregar_Objeto.comboBox.currentText() == "----Seleccione un Género----"):
            cadena += "  Género de la Pélicula"

        if(cadena != "Campos no válidos:\n"):
            
            ventana_mensaje.setWindowTitle("Error") 
            ventana_mensaje.setText("%s"%(cadena)) 
            ventana_mensaje.addButton(QMessageBox.Ok) 
            respuesta = ventana_mensaje.exec()  

        else:
            temp = self.Agregar_Objeto.Descripcion_textEdit.toPlainText()
            temp = temp.replace("\n"," ")
            objeto_Pelicula = Info_Pelicula(self.Agregar_Objeto.Nombre_lineEdit.text(), self.Agregar_Objeto.Duracion_lineEdit.text(), 
            temp, self.Agregar_Objeto.Director_lineEdit.text(), self.Agregar_Objeto.comboBox.currentText())

            ll.delete(posicion)
            ll.push_in(objeto_Pelicula,posicion)

            ventana_mensaje.setWindowTitle("Exito") 
            ventana_mensaje.setText("<p align='center'>Se ha Agregado con Exito") 
            ventana_mensaje.addButton(QMessageBox.Ok) 
            respuesta = ventana_mensaje.exec()
            
            if(respuesta == QMessageBox.Ok):
            
                self.Agregar_Objeto.guardar_json()
                ventana_mensaje.close()
                self.Agregar_Objeto.abrir_Ventana_Principal() 

    def eliminar(self):

        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)

        try:
            ID = int(self.ID_lineEdit.text())-1

            if(int(ID) < 0 or int(ID)+1 > ll.length()):

                mensaje.setWindowTitle("Error")
                mensaje.setText("Error, el ID ingresado no es válido")
                mensaje.addButton(QMessageBox.Ok)
                mensaje.exec()

            else:

                mensaje.setWindowTitle("Editar")
                mensaje.setText("¿Está seguro que desea eliminar el elemento %d?" %(int(ID)+1))
                mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                respuesta = mensaje.exec()

                if(respuesta == QMessageBox.Yes):
                    
                    self.hide()
                    ll.delete(ID)
                    self.Agregar_Objeto = Agregar_Pelicula()
                    self.Agregar_Objeto.guardar_json()
                    self.Objeto_Ventana_Principal = Ventana_Principal()
                    self.Objeto_Ventana_Principal.show()

        except ValueError:
            
            mensaje.setWindowTitle("Error")
            mensaje.setText("Error, el ID ingresado no es válido")
            mensaje.addButton(QMessageBox.Ok)
            mensaje.exec()    
        
#Función Main
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Principal_MainWindow = Ventana_Principal()

    Ventana_Principal_MainWindow.show()

    sys.exit(app.exec_())

