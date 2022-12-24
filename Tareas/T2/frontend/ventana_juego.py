from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
import os
import parametros as p
from entidades.soles import Sol 

window_name, base_class = uic.loadUiType(os.path.join('frontend',\
     'assets', 'uifiles', 'ui-ventana-juego.ui'))

class VentanaJuego(window_name, base_class):
    senal_iniciar_juego = pyqtSignal()
    senal_pausar_juego = pyqtSignal()
    senal_reanudar_juego = pyqtSignal()
    senal_avanzar_juego = pyqtSignal()
    senal_setear_planta = pyqtSignal(str, tuple, int)
    senal_comer_arriba = pyqtSignal()
    senal_comer_abajo = pyqtSignal()
    senal_generar_sol = pyqtSignal()
    senal_verificar_click_sol = pyqtSignal(tuple)
    senal_enviar_sol_girasol = pyqtSignal(Sol)
    senal_cheatcode_sol = pyqtSignal()
    senal_cheatcode_kil = pyqtSignal()
    senal_avanzar = pyqtSignal()
    senal_guardar_puntaje = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.tablero_arriba = {
            "pos1": (390, 180),
            "pos2": (450, 180),
            "pos3": (515, 180),
            "pos4": (585, 180),
            "pos5": (650, 180),
            "pos6": (715, 180),
            "pos7": (775, 180),
            "pos8": (840, 180),
            "pos9": (905, 180),
            "pos10": (970, 180)
        }
        self.tablero_abajo = {
            "pos1": (390, 280),
            "pos2": (450, 280),
            "pos3": (515, 280),
            "pos4": (585, 280),
            "pos5": (650, 280),
            "pos6": (715, 280),
            "pos7": (775, 280),
            "pos8": (840, 280),
            "pos9": (905, 280),
            "pos10": (970, 280)
        }

        self.eleccion_planta = False
        self.started = False
        self.pausa = False 
        self.teclas = []
        self.cheatcode_sol = ["s", "u", "n"]
        self.cheatcode_kil = ["k", "i", "l"]
        self.cheatcode = None
        self.precio_girasol.setText(str(p.COSTO_GIRASOL))
        self.precio_guisantes.setText(str(p.COSTO_LANZAGUISANTE))
        self.precio_hielo.setText(str(p.COSTO_LANZAGUISANTE_HIELO))
        self.precio_papa.setText(str(p.COSTO_PAPA))

    def init_gui(self):
        self.boton_iniciar.clicked.connect(self.iniciar_juego)
        self.boton_avanzar.clicked.connect(self.avanzar)
        self.boton_pausa.clicked.connect(self.pausar)
        self.boton_salir.clicked.connect(self.salir)
    
    def salir(self):
        self.senal_guardar_puntaje.emit()
        self.close()
    
    def setear_datos(self, datos):
        self.label_soles.setText(str(datos['soles']))
        self.label_soles.repaint()
        self.label_puntaje.setText(str(datos['puntaje']))
        self.label_puntaje.repaint()
        self.label_nivel.setText(str(datos['nivel']))
        self.label_nivel.repaint()
        self.label_zombies_destruidos.setText(str(datos['zombies destruidos']))
        self.label_zombies_destruidos.repaint()
        self.label_zombies_restantes.setText(str(datos['zombies restantes']))
        self.label_zombies_restantes.repaint()
    
    def reiniciar_datos(self, ronda):
        self.label_soles.setText(str(p.SOLES_INICIALES))
        self.label_soles.repaint()
        self.label_puntaje.setText("0")
        self.label_puntaje.repaint()
        self.label_nivel.setText(str(ronda))
        self.label_nivel.repaint()
        self.label_zombies_destruidos.setText("0")
        self.label_zombies_destruidos.repaint()
        self.label_zombies_restantes.setText(str(p.N_ZOMBIES * 2))
        self.label_zombies_restantes.repaint()

    def iniciar_juego(self):
        if not self.started and not self.pausa:
            self.senal_iniciar_juego.emit()
            self.started = True
        elif self.started and self.pausa:
            self.senal_reanudar_juego.emit()
            self.pausa = False
    
    def pausar(self):
        if not self.pausa and self.started:
            self.senal_pausar_juego.emit()
            self.pausa = True
        else:
            pass
    
    def avanzar(self):
        if self.started and not self.pausa:

            self.senal_avanzar.emit()
        
    def setear_escenario(self, choice):
        if "dia" in choice:
            self.imagen_fondo_noche.hide()
        elif "noche" in choice:
            self.imagen_fondo_dia.hide()
        
        self.show()
    
    def comer_arriba(self):
        self.senal_comer_arriba.emit()
    
    def comer_abajo(self):
        self.senal_comer_abajo.emit()
    
    def generar_sol(self):
        self.senal_generar_sol.emit()
    
    def generar_sol_girasol(self, sol):
        self.senal_enviar_sol_girasol.emit(sol)
    
    def termino_ronda(self):
        self.hide()
    
    def empezar_nueva_ronda(self, ronda):
        self.started = False
        self.pausa = False
        self.eleccion_planta = False
        self.reiniciar_datos(ronda)
        self.show()

    def keyPressEvent(self, event):
        tecla = event.text()  
        if tecla == "p":
            if not self.pausa and self.started:
                self.senal_pausar_juego.emit()
                self.pausa = True
        else:
            if self.started and not self.pausa:
                if len(self.teclas) > 0:
                    if self.cheatcode == "sun":
                        if tecla in self.cheatcode_sol:
                            if tecla not in self.teclas:
                                self.teclas.append(tecla)
                            else:
                                self.cheatcode = None
                                self.teclas = []
                        else:
                            self.cheatcode = None
                            self.teclas = []
                    elif self.cheatcode == "kil":
                        if tecla in self.cheatcode_kil:
                            if tecla not in self.teclas:
                                self.teclas.append(tecla)
                            else:
                                self.cheatcode = None
                                self.teclas = []
                        else:
                            self.cheatcode = None
                            self.teclas = []

                    if len(self.teclas) == 3:
                        if self.cheatcode == "kil":
                            self.senal_cheatcode_kil.emit()
                            print("kil cheatcode")
                        elif self.cheatcode == "sun":
                            self.senal_cheatcode_sol.emit()
                            print("sun cheatcode")
                        self.teclas = []
                        self.cheatcode = None
                else:
                    if tecla in self.cheatcode_kil:
                        self.cheatcode = "kil"
                        self.teclas.append(tecla)

                    elif tecla in self.cheatcode_sol:
                        self.cheatcode = "sun"
                        self.teclas.append(tecla)
                    
    def mousePressEvent(self, event):
        pos_planta = None
        pos = None
        fuera_de_zona = False
        if self.started and not self.pausa:
            if event.button() == 2:
                if self.eleccion_planta:
                    if (self.frame_pos1_arriba.x() < int(event.x()) < self.frame_pos1_arriba.x()\
                         + self.frame_pos1_arriba.width()) \
                        and (self.frame_pos1_arriba.y() < int(event.y()) <\
                        self.frame_pos1_arriba.y() + self.frame_pos1_arriba.height()):
                        pos_planta = self.tablero_arriba["pos1"]
                        pos = 1

                    elif (self.frame_pos2_arriba.x() < int(event.x()) < self.frame_pos2_arriba.x()\
                         + self.frame_pos2_arriba.width()) \
                        and (self.frame_pos2_arriba.y() < int(event.y()) < \
                            self.frame_pos2_arriba.y() + self.frame_pos2_arriba.height()):
                        pos_planta = self.tablero_arriba["pos2"]
                        pos = 2

                    elif (self.frame_pos3_arriba.x() < int(event.x()) < self.frame_pos3_arriba.x()\
                         + self.frame_pos3_arriba.width()) \
                        and (self.frame_pos3_arriba.y() < int(event.y()) < \
                            self.frame_pos3_arriba.y()\
                             + self.frame_pos3_arriba.height()):
                        pos_planta = self.tablero_arriba["pos3"]
                        pos = 3

                    elif (self.frame_pos4_arriba.x() < int(event.x()) < self.frame_pos4_arriba.x()\
                         + self.frame_pos4_arriba.width()) \
                        and (self.frame_pos4_arriba.y() < int(event.y()) <\
                             self.frame_pos4_arriba.y() + self.frame_pos4_arriba.height()):

                        pos_planta = self.tablero_arriba["pos4"]
                        pos = 4

                    elif (self.frame_pos5_arriba.x() < int(event.x()) < self.frame_pos5_arriba.x()\
                         + self.frame_pos5_arriba.width()) \
                        and (self.frame_pos5_arriba.y() < int(event.y()) <\
                             self.frame_pos5_arriba.y() + self.frame_pos5_arriba.height()):
                        pos_planta = self.tablero_arriba["pos5"]
                        pos = 5

                    elif (self.frame_pos6_arriba.x() < int(event.x()) < self.frame_pos6_arriba.x()\
                         + self.frame_pos6_arriba.width()) \
                        and (self.frame_pos6_arriba.y() < int(event.y()) < \
                            self.frame_pos6_arriba.y() + self.frame_pos6_arriba.height()):
                        pos_planta = self.tablero_arriba["pos6"]
                        pos = 6

                    elif (self.frame_pos7_arriba.x() < int(event.x()) < self.frame_pos7_arriba.x()\
                         + self.frame_pos7_arriba.width()) \
                        and (self.frame_pos7_arriba.y() < int(event.y()) < \
                            self.frame_pos7_arriba.y() + self.frame_pos7_arriba.height()):
                        pos_planta = self.tablero_arriba["pos7"]
                        pos = 7

                    elif (self.frame_pos8_arriba.x() < int(event.x()) < self.frame_pos8_arriba.x()\
                         + self.frame_pos8_arriba.width()) \
                        and (self.frame_pos8_arriba.y() < int(event.y()) < \
                            self.frame_pos8_arriba.y() + self.frame_pos8_arriba.height()):
                        pos_planta = self.tablero_arriba["pos8"]
                        pos = 8

                    elif (self.frame_pos9_arriba.x() < int(event.x()) < self.frame_pos9_arriba.x()\
                         + self.frame_pos9_arriba.width()) \
                        and (self.frame_pos9_arriba.y() < int(event.y()) < \
                            self.frame_pos9_arriba.y() + self.frame_pos9_arriba.height()):
                        pos_planta = self.tablero_arriba["pos9"]
                        pos = 9

                    elif (self.frame_pos10_arriba.x() < int(event.x()) < \
                        self.frame_pos10_arriba.x()\
                         + self.frame_pos10_arriba.width()) \
                        and (self.frame_pos10_arriba.y() < int(event.y()) <\
                             self.frame_pos10_arriba.y() + self.frame_pos10_arriba.height()):
                        pos_planta = self.tablero_arriba["pos10"]
                        pos = 10

                    elif (self.frame_pos1_abajo.x() < int(event.x()) < self.frame_pos1_abajo.x()\
                         + self.frame_pos1_abajo.width()) \
                        and (self.frame_pos1_abajo.y() < int(event.y()) < \
                            self.frame_pos1_abajo.y() + self.frame_pos1_abajo.height()):
                        pos_planta = self.tablero_abajo["pos1"]
                        pos = 1

                    elif (self.frame_pos2_abajo.x() < int(event.x()) < self.frame_pos2_abajo.x()\
                         + self.frame_pos2_abajo.width()) \
                        and (self.frame_pos2_abajo.y() < int(event.y()) < \
                            self.frame_pos2_abajo.y() + self.frame_pos2_abajo.height()):
                        pos_planta = self.tablero_abajo["pos2"]
                        pos = 2

                    elif (self.frame_pos3_abajo.x() < int(event.x()) < self.frame_pos3_abajo.x()\
                         + self.frame_pos3_abajo.width()) \
                        and (self.frame_pos3_abajo.y() < int(event.y()) < \
                            self.frame_pos3_abajo.y() + self.frame_pos3_abajo.height()):
                        pos_planta = self.tablero_abajo["pos3"]
                        pos = 3

                    elif (self.frame_pos4_abajo.x() < int(event.x()) < self.frame_pos4_abajo.x()\
                         + self.frame_pos4_abajo.width()) \
                        and (self.frame_pos4_abajo.y() < int(event.y()) < \
                            self.frame_pos4_abajo.y() + self.frame_pos4_abajo.height()):
                        pos_planta = self.tablero_abajo["pos4"]
                        pos = 4

                    elif (self.frame_pos5_abajo.x() < int(event.x()) < self.frame_pos5_abajo.x()\
                         + self.frame_pos5_abajo.width()) \
                        and (self.frame_pos5_abajo.y() < int(event.y()) < \
                            self.frame_pos5_abajo.y() + self.frame_pos5_abajo.height()):
                        pos_planta = self.tablero_abajo["pos5"]
                        pos = 5

                    elif (self.frame_pos6_abajo.x() < int(event.x()) < self.frame_pos6_abajo.x()\
                         + self.frame_pos6_abajo.width()) \
                        and (self.frame_pos6_abajo.y() < int(event.y()) < \
                            self.frame_pos6_abajo.y() + self.frame_pos6_abajo.height()):
                        pos_planta = self.tablero_abajo["pos6"]
                        pos = 6

                    elif (self.frame_pos7_abajo.x() < int(event.x()) < self.frame_pos7_abajo.x()\
                         + self.frame_pos7_abajo.width()) \
                        and (self.frame_pos7_abajo.y() < int(event.y()) < \
                            self.frame_pos7_abajo.y() + self.frame_pos7_abajo.height()):
                        pos_planta = self.tablero_abajo["pos7"]
                        pos = 7

                    elif (self.frame_pos8_abajo.x() < int(event.x()) < self.frame_pos8_abajo.x()\
                         + self.frame_pos8_abajo.width()) \
                        and (self.frame_pos8_abajo.y() < int(event.y()) < \
                            self.frame_pos8_abajo.y() + self.frame_pos8_abajo.height()):
                        pos_planta = self.tablero_abajo["pos8"]
                        pos = 8

                    elif (self.frame_pos9_abajo.x() < int(event.x()) < self.frame_pos9_abajo.x()\
                         + self.frame_pos9_abajo.width()) \
                        and (self.frame_pos9_abajo.y() < int(event.y()) < \
                            self.frame_pos9_abajo.y() + self.frame_pos9_abajo.height()):
                        pos_planta = self.tablero_abajo["pos9"]
                        pos = 9

                    elif (self.frame_pos10_abajo.x() < int(event.x()) < self.frame_pos10_abajo.x()\
                         + self.frame_pos10_abajo.width()) \
                        and (self.frame_pos10_abajo.y() < int(event.y()) < \
                            self.frame_pos10_abajo.y() + self.frame_pos10_abajo.height()):
                        pos_planta = self.tablero_abajo["pos10"]
                        pos = 10

                    else:
                        fuera_de_zona = True

                    if fuera_de_zona:
                        fuera_de_zona = False
                    else:
                        self.senal_setear_planta.emit(self.eleccion_planta, pos_planta, pos)
                        

                        self.eleccion_planta = False

                else:

                    if (self.frame_girasol.x() < int(event.x()) < self.frame_girasol.x()\
                         + self.frame_girasol.width()) \
                        and (self.frame_girasol.y() < int(event.y()) < \
                            self.frame_girasol.y() + self.frame_girasol.height()):
                        self.eleccion_planta = "girasol"

                    elif (self.frame_guisante.x() < int(event.x()) < self.frame_guisante.x()\
                         + self.frame_guisante.width()) \
                        and (self.frame_guisante.y() < int(event.y()) < \
                            self.frame_guisante.y() + self.frame_guisante.height()):
                        self.eleccion_planta = "guisante"

                    elif (self.frame_hielo.x() < int(event.x()) < self.frame_hielo.x()\
                         + self.frame_hielo.width()) \
                        and (self.frame_hielo.y() < int(event.y()) < \
                            self.frame_hielo.y() + self.frame_hielo.height()):
                        self.eleccion_planta = "hielo"

                    elif (self.frame_papa.x() < int(event.x()) < self.frame_papa.x()\
                         + self.frame_papa.width()) \
                        and (self.frame_papa.y() < int(event.y()) < \
                            self.frame_papa.y() + self.frame_papa.height()):
                        self.eleccion_planta = "papa"
            
            elif event.button() == 1:
                self.senal_verificar_click_sol.emit((int(event.x()), int(event.y())))
                
                

