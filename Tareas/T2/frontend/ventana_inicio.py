from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
import os


window_name, base_class = uic.loadUiType(os.path.join('frontend',\
     'assets', 'uifiles', 'ui-ventana-inicio.ui'))


class VentanaInicio(window_name, base_class):
    senal_enviar_usuario = pyqtSignal(str)
    senal_ver_ranking = pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
    
    def init_gui(self):
        self.input_usuario.setPlaceholderText("Introduzca usuario")
        self.boton_inicio_jugar.clicked.connect(self.enviar_usuario)
        self.boton_inicio_ranking.clicked.connect(self.ver_ranking)
        self.boton_inicio_salir.clicked.connect(self.close)
    
    def mostrar_ventana(self):
        self.show()
    
    def enviar_usuario(self):
        self.senal_enviar_usuario.emit(self.input_usuario.text())
        
    
    def comprobar_usuario(self, valid):
        if valid:
            self.hide()
        else:
            self.input_usuario.setText('')
            self.input_usuario.setPlaceholderText("Usuario invalido")
    
    def ver_ranking(self):
        self.senal_ver_ranking.emit()
        self.hide()


    
        

