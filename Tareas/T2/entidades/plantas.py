from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from os import path
from entidades.guisantes import GuisanteClasico, GuisanteHielo
import parametros as p
from entidades.soles import Sol


class PlantaAtaque(QLabel):

    def __init__(self, parent, pos):
        super().__init__(parent)
        self._vida = p.VIDA_PLANTA
        self.viva = True
        self.ataque = True
        self.setGeometry(pos[0], pos[1], 90, 90)
        self.setScaledContents(True)
        self.show()
        self.set_timers()
        self.guisantes_disparados = []
        self.intervalo_disparos = p.INTERVALO_DISPARO
        
    @property
    def vida(self):
        return self._vida 
    
    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self._vida = 0
            self.viva = False
            self.hide()
            self.timer_disparar.stop()
            self.timer_verificacion_guisantes.stop()
        else:
            self._vida = valor
    
    def set_timers(self):
        self.timer_disparar = QTimer()
        self.timer_disparar.setInterval(p.INTERVALO_DISPARO)
        self.timer_verificacion_guisantes = QTimer()
        self.timer_verificacion_guisantes.setInterval(100)
    
    def verificar_guisantes(self):
        for guisante in self.guisantes_disparados:
            if guisante.x() > 1100 or not guisante.timer.isActive():
                guisante.hide()
                self.guisantes_disparados.remove(guisante)
    
    def pausa(self):
        if self.viva:
            self.timer_disparar.stop()
            self.timer_verificacion_guisantes.stop()
            for guisante in self.guisantes_disparados:
                guisante.timer.stop()
    
    def reanudar(self):
        if self.viva:
            self.timer_disparar.start()
            self.timer_verificacion_guisantes.start()
            for guisante in self.guisantes_disparados:
                guisante.timer.start()
    
    def esconder(self):
        for guisante in self.guisantes_disparados:
            guisante.esconder()
        self.guisantes_disparados = []
        self.hide()
        
                
class Planta(QLabel):

    def __init__(self, parent, pos):
        super().__init__(parent)
        self._vida = p.VIDA_PLANTA
        self.viva = True
        self.ataque = False
        self.setGeometry(pos[0], pos[1], 90, 90)
        self.setScaledContents(True)
        self.show()
    
    def esconder(self):
        self.hide()
        

class PlantaClasica(PlantaAtaque):

    def __init__(self, parent, pos):
        super().__init__(parent, pos) 
        ruta_imagen = path.join(p.PATH_PLANTAS, "lanzaguisantes_1.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)
        self.ventana = parent   
        self.timer_disparar.timeout.connect(self.disparar)
        self.timer_verificacion_guisantes.timeout.connect(self.verificar_guisantes)
        self.timer_disparar.start()
        self.timer_verificacion_guisantes.start()
        
    def disparar(self):
        self.guisantes_disparados.append(GuisanteClasico(self.ventana, self.x(), self.y()))
        
    def verificar_guisantes(self):
        return super().verificar_guisantes()
        

class PlantaAzul(PlantaAtaque):

    def __init__(self, parent, pos):
        super().__init__(parent, pos)     
        ruta_imagen = path.join(p.PATH_PLANTAS, "lanzaguisantesHielo_1.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)
        self.ventana = parent
        self.timer_disparar.timeout.connect(self.disparar)
        self.timer_verificacion_guisantes.timeout.connect(self.verificar_guisantes)
        self.timer_disparar.start()
        self.timer_verificacion_guisantes.start()
    
    def disparar(self):
        self.guisantes_disparados.append(GuisanteHielo(self.ventana, self.x(), self.y()))
    
    def verificar_guisantes(self):
        return super().verificar_guisantes()
    
    
class Girasol(Planta):

    def __init__(self, parent, pos):
        super().__init__(parent, pos)
        self.ventana = parent
        self.soles_generados = []
        ruta_imagen = path.join(p.PATH_PLANTAS, "girasol_1.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)
        self.timer_generar_soles = QTimer()
        self.timer_generar_soles.setInterval(p.INTERVALO_SOLES_GIRASOL)
        self.timer_generar_soles.timeout.connect(self.generar_sol)
        self.timer_generar_soles.start()
    
    @property
    def vida(self):
        return self._vida 
    
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
            self.viva = False
            self.hide()
            self.timer_generar_soles.stop()
        else:
            self._vida = valor

    def generar_sol(self):
        self.ventana.generar_sol_girasol(Sol(self.ventana, (self.x(), self.y())))
    
    def pausa(self):
        if self.viva:
            self.timer_generar_soles.stop()
    
    def reanudar(self):
        if self.viva:
            self.timer_generar_soles.start()
    
    def esconder(self):
        for sol in self.soles_generados:
            sol.hide()
        self.hide()
        
        
class Patata(Planta):

    def __init__(self, parent, pos):
        super().__init__(parent, pos)
        self._vida = p.VIDA_PLANTA * 2
        ruta_imagen = path.join(p.PATH_PLANTAS, "papa_1.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)
    
    @property
    def vida(self):
        return self._vida 
    
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
            self.viva = False
            self.hide()
        else:
            self._vida = valor
    
    def pausa(self):
        pass

    def reanudar(self):
        pass

    def esconder(self):
        return super().esconder()


