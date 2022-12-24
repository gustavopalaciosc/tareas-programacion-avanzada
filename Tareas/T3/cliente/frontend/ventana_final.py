from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from os.path import join
from funciones import read_json

window_name, base_class = uic.loadUiType(join(*read_json("RUTA_PANTALLA_FINAL")))

class VentanaFinal(window_name, base_class):
    senal_abrir_ventana_inicio = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
    
    def mostrar_ventana(self, gano, nombre):
        if gano:
            self.texto_victoria.setText(f"Felicidades {nombre}, has ganado!")
        else:
            self.texto_victoria.setText(f"Lo sentimos {nombre}, has perdido")

        self.show()
    
    def volver(self):
        self.hide()
        self.texto_victoria.setText("")
        self.senal_abrir_ventana_inicio.emit()