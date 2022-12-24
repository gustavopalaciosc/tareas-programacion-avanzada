from PyQt5 import uic
from os.path import join
from funciones import read_json


window_name, base_class = uic.loadUiType(join(*read_json("RUTA_PANTALLA_ESPERA")))

class VentanaEspera(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def mostrar_ventana(self):
        self.show()
    
    def cerrar_ventana(self):
        self.close()
    
    def set_jugador(self, nombre, is_me: bool):
        if is_me:
            self.label_jugador_uno.setText(nombre)
        else:
            self.label_jugador_dos.setText(nombre)
    
    def actualizar_tiempo_espera(self, tiempo):
        self.tiempo_espera.setText("")
        self.tiempo_espera.setText(f"{tiempo}")
        
    
        
    