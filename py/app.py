from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys
import os

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        rutaUI = os.path.join(os.path.dirname(__file__), '../ui/test.ui')
        loadUi(rutaUI, self)
        
      
        # Conectar el evento valueChanged del slider
        self.sliderRed.valueChanged.connect(self.valueChanged)
        
        # Conectar el evento valueChanged del slider
        self.sliderGreen.valueChanged.connect(self.valueChanged)
        
        # Conectar el evento valueChanged del slider
        self.sliderBlue.valueChanged.connect(self.valueChanged)
        

        self.exit.clicked.connect(self.close)
        
    def colorsView(self):
        #Crear qdialog para seleccionar color
        color = QColorDialog().getColor(QColor(self.hexDecimal.text()))
        
        # Cambiar el color predeterminado del dialogo al entrar
        
        

        hex = color.name()
        self.frame.setStyleSheet('background-color: ' + hex)
        
        self.hexDecimal.setText(hex)
        
        #Pasar de hexadecimal a decimal
        redValue = int(hex[1:3], 16)
        greenValue = int(hex[3:5], 16)
        blueValue = int(hex[5:7], 16)
        
        self.sliderRed.setValue(redValue)
        self.sliderGreen.setValue(greenValue)
        self.sliderBlue.setValue(blueValue)
        
        
        
        
    # Redeclarar el evento valueChanged del slider
    def valueChanged(self):
        redValue = self.sliderRed.value()
        greenValue = self.sliderGreen.value()
        blueValue = self.sliderBlue.value()
        
        hex = '#%02x%02x%02x' % (redValue, greenValue, blueValue)
        
        self.frame.setStyleSheet('background-color: ' + hex)
        
        self.hexDecimal.setText(hex)
   
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()