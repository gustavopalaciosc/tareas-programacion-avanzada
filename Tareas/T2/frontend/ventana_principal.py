from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QCheckBox
from PyQt5 import uic
import os
import sys

window_name, base_class = uic.loadUiType(os.path.join('frontend',\
     'assets', 'uifiles', 'ui-ventana-principal.ui'))

class VentanaPrincipal(window_name, base_class):
    
    senal_empezar_juego = pyqtSignal(set)
    senal_elegir_cancha = pyqtSignal(bool, bool)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
    

    def init_gui(self):
        self.check_dia = QCheckBox('Jardin de la abuela', self)
        self.check_noche = QCheckBox('Salida nocturna', self)

        self.check_dia.setGeometry(200, 480, 200, 100)
        self.check_dia.setStyleSheet("color: rgb(255, 255, 255);")

        self.check_noche.setGeometry(680, 480, 200, 100)
        self.check_noche.setStyleSheet("color: rgb(255, 255, 255);")

        self.boton_inicio.clicked.connect(self.elegir_cancha)
    
    def mostrar_ventana(self):
        self.show()
    
    def elegir_cancha(self):
        self.senal_elegir_cancha.emit(self.check_dia.isChecked(), self.check_noche.isChecked())
    
    def recibir_validacion(self, valid, choice):
        if valid:
            self.senal_empezar_juego.emit(choice)
            self.hide()
        else:
            print("Opcion invalida")
        



        
        






if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())