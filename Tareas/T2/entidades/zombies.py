from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from os import path
import parametros as p


class Zombie(QLabel):

    def __init__(self, parent, pos_inicial):
        super().__init__(parent)
        self._vida = p.VIDA_ZOMBIE
        self.dano = p.DANO_MORDIDA
        self.velocidad = p.VELOCIDAD_ZOMBIE / 1000
        self.comiendo = False
        self.vivo = True
        self.ralentizado = False
        self.ventana = parent
        

        self.setScaledContents(True)
        self.setGeometry(pos_inicial[0], pos_inicial[1], 100, 130)
        self.set_timers(pos_inicial)
        
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self._vida = 0
            self.vivo = False
            self.hide()
            self.timer_comer.stop()
            self.timer_moverse.stop()
        else:
            self._vida = valor
    
    def set_timers(self, pos):
        self.timer_moverse = QTimer(self)
        self.timer_moverse.setInterval(500)
        self.timer_moverse.timeout.connect(self.moverse)
        self.timer_comer = QTimer(self)
        self.timer_comer.setInterval(p.INTERVALO_TIEMPO_MORDIDA)

        if pos[1] == 150:
            self.timer_comer.timeout.connect(self.ventana.comer_arriba)
        
        elif pos[1] == 250:
            self.timer_comer.timeout.connect(self.ventana.comer_abajo)
 
    def iniciar_timer(self):
        self.timer_moverse.start()
        self.show()

    def moverse(self):
        self.x()
        self.y()
        self.move(self.x() - int(self.velocidad), self.y())
        
    def pausa(self):
        if self.vivo:
            if self.timer_moverse.isActive():
                self.comiendo = False
            
                self.timer_moverse.stop()
            else:
                self.comiendo = True
                self.timer_comer.stop()
    
    def reanudar(self):
        if self.vivo:
            if self.comiendo:
                self.timer_comer.start()
            else:
                self.timer_moverse.start()
        
     
class ZombieClasico(Zombie):
    
    def __init__(self, parent, pos_inicial):
        super().__init__(parent, pos_inicial)     
        ruta_imagen = path.join(p.PATH_ZOMBIES, "Caminando", "zombieNicoWalker_1.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)
     
    def iniciar_timer(self):
        return super().iniciar_timer()
    
    def moverse(self):
        return super().moverse()


class ZombieRapido(Zombie):
    
    def __init__(self, parent, pos_inicial):
        super().__init__(parent, pos_inicial)
        self.velocidad = int(p.VELOCIDAD_ZOMBIE * 1.5) / 1000

        ruta_imagen = path.join(p.PATH_ZOMBIES, "Caminando", "zombieHernanRunner_1.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)
    
    def iniciar_timer(self):
        return super().iniciar_timer()
    
    def moverse(self):
        return super().moverse()



        