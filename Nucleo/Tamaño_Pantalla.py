# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QApplication
import sys

class Center:
    #Metodo para centrar una ventana:
    def center(self):
        qRect = self.frameGeometry()     
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
