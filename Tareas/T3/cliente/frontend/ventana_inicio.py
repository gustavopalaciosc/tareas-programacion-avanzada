from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from os.path import join
from funciones import read_json

window_name, base_class = uic.loadUiType(join(*read_json("RUTA_PANTALLA_LOGIN")))


class VentanaInicio(window_name, base_class):

    senal_enviar_nombre = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
    
    def init_gui(self):
        self.input_usuario.setPlaceholderText("Introduzca su nombre")
        self.boton.clicked.connect(self.enviar_nombre)
    
    def mostrar_ventana(self):
        self.show()
    
    def cerrar_ventana(self):
        self.close()
    
    def enviar_nombre(self):
        print(f"{self.input_usuario.text()}")
        self.senal_enviar_nombre.emit(self.input_usuario.text())
    
    def set_nombre_invalido(self):
        self.input_usuario.setText("")
        self.input_usuario.setPlaceholderText("Nombre invalido")

    

    