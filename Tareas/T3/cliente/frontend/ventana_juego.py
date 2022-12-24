from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from os.path import join
from funciones import read_json
import os


window_name, base_class = uic.loadUiType(join(*read_json("RUTA_PANTALLA_JUEGO")))

class VentanaJuego(window_name, base_class):
    senal_seleccionar_carta = pyqtSignal(dict)
    senal_mostrar_ventana_final = pyqtSignal(bool, str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.carta_seleccionada = None
        self.num_cartas = read_json("BARAJA_PANTALLA")
        self.label_cartas = [self.carta_0, self.carta_1, 
        self.carta_2, self.carta_3, 
        self.carta_4, self.carta_5,
        self.carta_6]
        self.ui_mazo_propio = [self.mazo_0, 
        self.mazo_1, self.mazo_2, 
        self.mazo_3, self.mazo_4]
        self.ui_mazo_oponente = [self.mazo_op_0, 
        self.mazo_op_1, self.mazo_op_2, 
        self.mazo_op_3, self.mazo_op_4]
        self.mazo_propio = 0
        self.mazo_oponente = 0
        self.len_mazo = 15
        self.cartas = None
        self.ganador = False
        self.seleccionado = False
        self.boton_seleccionar.clicked.connect(self.enviar_carta_seleccionada)
    
    def mostrar_ventana(self, nombre_jugador, nombre_contrincante):
        self.label_nombre_oponente.setText(nombre_contrincante)
        self.label_nombre_jugador.setText(nombre_jugador)
        self.show()
    
    def set_cartas(self, cartas):
        self.len_mazo = len(cartas)
        self.cartas = cartas
        for i in range(0, min(self.num_cartas, self.len_mazo)):
            index = list(cartas.keys())[i]
            path = \
            f"{cartas[index]['color']}_{cartas[index]['elemento']}_{cartas[index]['puntos']}.png"
            self.label_cartas[i].setPixmap(QPixmap(os.path.join("sprites", "cartas", path)))
    
    def enviar_carta_seleccionada(self):
        if self.carta_seleccionada:
            self.senal_seleccionar_carta.emit({'comando': 'carta_seleccionada',
             'index_carta': int(self.carta_seleccionada)})
            
            key = list(self.cartas.keys())[int(self.carta_seleccionada)]
            carta = self.cartas[key]
            path = f"{carta['color']}_{carta['elemento']}_{carta['puntos']}.png"

            self.carta_jugador.setPixmap(QPixmap(os.path.join("sprites", "cartas", path)))
            self.carta_seleccionada = None
            self.seleccionado = True
    
    def set_carta_oponente(self, carta):
         path = f"{carta['color']}_{carta['elemento']}_{carta['puntos']}.png"
         self.carta_oponente.setPixmap(QPixmap(os.path.join("sprites", "cartas", path)))

    def set_mazo_ganador(self, gano, carta):
        color = carta['color']
        elemento = carta['elemento']
        path = f"{elemento}_{color}.png"

        if gano:
            self.ui_mazo_propio[self.mazo_propio].setPixmap(QPixmap(os.path.join("sprites",\
                 "elementos", "fichas", path)))
            self.mazo_propio += 1
            
        else:
            self.ui_mazo_oponente[self.mazo_oponente].setPixmap(QPixmap(os.path.join("sprites",\
                 "elementos", "fichas", path)))
            self.mazo_oponente += 1
        
    def mousePressEvent(self, event):
        if event.button():
            if not self.seleccionado:
                for i in range(0, min(self.num_cartas, self.len_mazo)):
                    pos_x = self.label_cartas[i].x()
                    pos_y = self.label_cartas[i].y()
                    width = self.label_cartas[i].width()
                    height = self.label_cartas[i].height()
                    if pos_x < int(event.x()) < pos_x + width \
                        and pos_y < int(event.y()) < pos_y + height:
                        self.carta_seleccionada = str(i)
                        break
    
    def esconder_cartas(self):
        self.carta_jugador.setPixmap(QPixmap(os.path.join("sprites", "cartas", "back.png")))
        self.carta_oponente.setPixmap(QPixmap(os.path.join("sprites", "cartas", "back.png")))
        self.seleccionado = False
    
    def set_ganador(self):
        self.ganador = True
    
    def termino_partida(self, nombre):
        self.hide()
        self.senal_mostrar_ventana_final.emit(self.ganador, nombre)
                