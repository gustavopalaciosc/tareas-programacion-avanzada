from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import os
import sys

window_name, base_class = uic.loadUiType(os.path.join('frontend',\
     'assets', 'uifiles', 'ui-ventana-post-juego.ui'))

class VentanaPostJuego(window_name, base_class):
    senal_nueva_ronda = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ganador = None
        self.ronda = 1
        self.jugador = None
        self.puntaje = None
        self.label_ganador.hide()
        self.label_perder.hide()
        self.boton_siguiente_ronda.clicked.connect(self.siguiente_ronda)
        self.boton_salir.clicked.connect(self.salir)
    
    def set_usuario(self, usuario):
        self.jugador = usuario
    

    def mostrar_ventana(self, ganador, dict):
        if ganador:
            self.ganador = True
            self.label_ganador.show()
        else:
            self.ganador = False
            self.label_perder.show()
        
        self.puntaje = int(dict['puntaje total'])

        self.valor_ronda.setText(str(dict['ronda']))
        self.valor_ronda.repaint()
        self.valor_soles.setText(str(dict['soles']))
        self.valor_soles.repaint()
        self.valor_zombies.setText(str(dict['zombies']))
        self.valor_zombies.repaint()
        self.valor_puntaje_ronda.setText(str(dict['puntaje']))
        self.valor_puntaje_ronda.repaint()
        self.valor_puntaje_total.setText(str(int(dict['puntaje total'])))
        self.valor_puntaje_total.repaint()

        self.show()
    
    def siguiente_ronda(self):
        if self.ganador:
            self.ronda += 1
            self.senal_nueva_ronda.emit(self.ronda)
            self.hide()
        else:
            pass
    
    def salir(self):
        self.guardar_puntaje()
        self.close()
    
    def guardar_puntaje(self):
        if self.puntaje != None:
            puntajes = open("puntajes.txt", "r", encoding="utf-8")
            puntos = puntajes.readlines()
            for i in range(0, len(puntos)):
                if puntos[i].split(",")[0] == self.jugador:
                    del puntos[i]
                    break
            puntos.append(f"{self.jugador},{self.puntaje}\n")
            puntajes.close()
            puntajes = open("puntajes.txt", "w", encoding="utf-8")
            for puntaje in puntos:
                puntajes.write(puntaje)
            puntajes.close()
        else:
            pass


    








if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPostJuego()
    ventana.show()
    sys.exit(app.exec_())