from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from entidades.zombies import ZombieClasico, ZombieRapido
from entidades.plantas import PlantaAzul, PlantaClasica, Patata, Girasol
from entidades.soles import Sol
import parametros as p
from random import choice, randint
from aparicion_zombies import intervalo_aparicion

class LogicaJuego(QObject):
    senal_generar_zombies = pyqtSignal(list)
    senal_cargar_datos = pyqtSignal(dict)
    senal_generar_sol_ventana = pyqtSignal()
    senal_termino_ronda = pyqtSignal(bool, dict)
    senal_termino_ronda_ventana = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.dia = None
        self.ponderador_dificultad = None
        self.zombies_carril_arriba = []
        self.zombies_carril_abajo = []
        self.n_zombies_generados = 0
        self.plantas_carril_arriba = {}
        self.plantas_carril_abajo = {}
        self.soles_generados = []
        self.timers = []
        self.soles = p.SOLES_INICIALES
        self.zombies_restantes = p.N_ZOMBIES * 2
        self.zombies_destruidos = 0
        self.nivel = 1
        self.puntaje = 0
        self.puntaje_total = 0

    def set_datos_inicio(self, choice):
        if 'dia' in choice:
            self.dia = True
            self.ponderador_dificultad = p.PONDERADOR_DIURNO
        elif 'noche' in choice:
            self.dia = False
            self.ponderador_dificultad = p.PONDERADOR_NOCTURNO
        
        self.senal_cargar_datos.emit({
            'soles': self.soles,
            'zombies restantes': self.zombies_restantes,
            'zombies destruidos': 0,
            'nivel': 1,
            'puntaje': 0
            })
    
    def crear_zombies(self):
        ventana_juego = self.sender()
        if self.nivel > 1:
            self.zombies_carril_arriba = []
            self.zombies_carril_abajo = []
        for _ in range(0, p.N_ZOMBIES):
            self.zombies_carril_arriba.append(choice([ZombieClasico(ventana_juego,\
            pos_inicial=(1100, 150)), ZombieRapido(ventana_juego, pos_inicial=(1100, 150))]))
            self.zombies_carril_abajo.append(choice([ZombieClasico(ventana_juego,\
            pos_inicial= (1100, 250)), ZombieRapido(ventana_juego, pos_inicial= (1100, 250))]))
    
    def iniciar_juego(self):
        self.crear_zombies()
        self.set_timers()
        self.timer_aparicion_zombies.start()
        self.timer_revisar_ataque_arriba.start()
        self.timer_revisar_ataque_abajo.start()
        self.timer_impacto_arriba.start()
        self.timer_impacto_abajo.start()
        self.timer_actualizar_datos.start()
        self.timer_fin_ronda.start()
        if self.dia:
            self.timer_aparicion_soles.start()
    
    def pausar(self):
        print("Juego pausado")
        if self.n_zombies_generados < p.N_ZOMBIES:
            self.timer_aparicion_zombies.stop()
            for i in range(0, self.n_zombies_generados):
                self.zombies_carril_abajo[i].pausa()
                self.zombies_carril_arriba[i].pausa()
        else:
            for zombie in self.zombies_carril_abajo + self.zombies_carril_arriba:
                zombie.pausa()
        self.timer_revisar_ataque_arriba.stop()
        self.timer_revisar_ataque_abajo.stop()
        self.timer_impacto_arriba.stop()
        self.timer_impacto_abajo.stop()
        self.timer_actualizar_datos.stop()
        self.timer_fin_ronda.stop()
        if self.dia:
            self.timer_aparicion_soles.stop()
        for planta in list(self.plantas_carril_abajo.values())\
             + list(self.plantas_carril_arriba.values()):
            planta.pausa()
    
    def reanudar(self):
        print("juego reanudado")
        if self.n_zombies_generados < p.N_ZOMBIES:
            self.timer_aparicion_zombies.start()
            for i in range(0, self.n_zombies_generados):
                self.zombies_carril_abajo[i].reanudar()
                self.zombies_carril_arriba[i].reanudar()
        else:
            for zombie in self.zombies_carril_abajo + self.zombies_carril_arriba:
                zombie.reanudar()

        self.timer_revisar_ataque_arriba.start()
        self.timer_revisar_ataque_abajo.start()
        self.timer_impacto_arriba.start()
        self.timer_impacto_abajo.start()
        self.timer_actualizar_datos.start()
        self.timer_fin_ronda.start()
        if self.dia:
            self.timer_aparicion_soles.start()
        for planta in list(self.plantas_carril_abajo.values()) +\
             list(self.plantas_carril_arriba.values()):
            planta.reanudar()
        
    def generar_soles(self):
        self.ventana = self.sender()
        pos_x = randint(410, 1030)
        pos_y = randint(50, 540)
        self.soles_generados.append(Sol(self.ventana, (pos_x, pos_y)))

    def generar_soles_ventana(self):
        self.senal_generar_sol_ventana.emit()
    
    def guardar_soles_girasol(self, sol):
        self.soles_generados.append(sol)

    def generar_zombies(self):  
        if self.n_zombies_generados == p.N_ZOMBIES:
            self.timer_aparicion_zombies.stop()    
        else:
            self.zombies_carril_abajo[self.n_zombies_generados].iniciar_timer()
            self.zombies_carril_arriba[self.n_zombies_generados].iniciar_timer()
            self.n_zombies_generados += 1

    def set_timers(self):
        self.timer_aparicion_zombies = QTimer()
        self.timer_aparicion_zombies.setInterval(int(intervalo_aparicion(self.nivel,\
             self.ponderador_dificultad) * 1000))
        self.timer_aparicion_zombies.timeout.connect(self.generar_zombies)
        self.timer_revisar_ataque_arriba = QTimer()
        self.timer_revisar_ataque_arriba.setInterval(100)
        self.timer_revisar_ataque_arriba.timeout.connect(self.revisar_ataque_zombie_arriba)
        self.timer_revisar_ataque_abajo = QTimer()
        self.timer_revisar_ataque_abajo.setInterval(100)
        self.timer_revisar_ataque_abajo.timeout.connect(self.revisar_ataque_zombie_abajo)
        self.timer_impacto_arriba = QTimer()
        self.timer_impacto_arriba.setInterval(150)
        self.timer_impacto_arriba.setSingleShot(True)
        self.timer_impacto_arriba.timeout.connect(self.revisar_impacto_guisante_arriba)
        self.timer_impacto_abajo = QTimer()
        self.timer_impacto_abajo.setInterval(150)
        self.timer_impacto_abajo.setSingleShot(True)
        self.timer_impacto_abajo.timeout.connect(self.revisar_impacto_guisante_abajo)
        self.timer_aparicion_soles = QTimer()
        self.timer_aparicion_soles.setInterval(p.INTERVALO_APARICION_SOLES)
        self.timer_aparicion_soles.timeout.connect(self.generar_soles_ventana) 
        self.timer_actualizar_datos = QTimer()
        self.timer_actualizar_datos.setInterval(20)
        self.timer_actualizar_datos.timeout.connect(self.actualizar_datos)
        self.timer_fin_ronda = QTimer()
        self.timer_fin_ronda.setInterval(1000)
        self.timer_fin_ronda.timeout.connect(self.revisar_fin_ronda)
    
    def actualizar_datos(self):
        self.senal_cargar_datos.emit({
            "soles": self.soles,
            "zombies restantes": self.zombies_restantes,
            "zombies destruidos": self.zombies_destruidos,
            "nivel": self.nivel,
            "puntaje": self.puntaje
            })
 
    def revisar_ataque_zombie_arriba(self):
        for zombie in self.zombies_carril_arriba:
            for planta in list(self.plantas_carril_arriba.values()):
                if planta.x() + 30 < zombie.x() < planta.x() + 55:
                    if planta.viva:
                        if zombie.timer_moverse.isActive():
                            zombie.timer_moverse.stop()
                        if not zombie.timer_comer.isActive():
                            zombie.timer_comer.start()
                    else:
                        if not zombie.timer_moverse.isActive():
                            zombie.timer_moverse.start()
                        if zombie.timer_comer.isActive():
                            zombie.timer_comer.stop()
                    
    def revisar_ataque_zombie_abajo(self):
        for zombie in self.zombies_carril_abajo:
            for planta in list(self.plantas_carril_abajo.values()):
                if planta.x() + 25 < zombie.x() < planta.x() + 55:
                    if planta.viva:
                        if zombie.timer_moverse.isActive():
                            zombie.timer_moverse.stop()
                        if not zombie.timer_comer.isActive():
                            zombie.timer_comer.start()
                    else:
                        if not zombie.timer_moverse.isActive():
                            zombie.timer_moverse.start()
                        if zombie.timer_comer.isActive():
                            zombie.timer_comer.stop()
                            
    def ataque_arriba(self):
        for zombie in self.zombies_carril_arriba:
            for planta in list(self.plantas_carril_arriba.values()):
                if zombie.vivo:
                    if planta.x() + 25 < zombie.x() < planta.x() + 55:            
                        planta.vida -= zombie.dano
                       
    def ataque_abajo(self):
        for zombie in self.zombies_carril_abajo:
            for planta in list(self.plantas_carril_abajo.values()):
                if zombie.vivo:
                    if planta.x() + 25 < zombie.x() < planta.x() + 55:
                        planta.vida -= zombie.dano
                    
    def revisar_impacto_guisante_arriba(self):     
        for planta in self.plantas_carril_arriba.values():
            if planta.ataque:
                for guisante in planta.guisantes_disparados:
                    for zombie in self.zombies_carril_arriba:
                        if zombie.x() < guisante.x() < zombie.x() + 35:
                            if zombie.vivo:
                                zombie.vida -= 5
                                print(zombie.vida)
                                guisante.timer.stop()
                                guisante.hide()
                                if not zombie.vivo:
                                    self.zombies_destruidos += 1
                                    self.zombies_restantes -= 1
                                    if self.dia:
                                        self.puntaje += p.PUNTAJE_ZOMBIE_DIURNO
                                    else:
                                        self.puntaje += p.PUNTAJE_ZOMBIE_NOCTURNO
                                break
        self.timer_impacto_arriba.start()
                        
    def revisar_impacto_guisante_abajo(self):       
        for planta in self.plantas_carril_abajo.values():
            if planta.ataque:
                for guisante in planta.guisantes_disparados:
                    for zombie in self.zombies_carril_abajo:
                        if zombie.x() < guisante.x() < zombie.x() + 35:
                            if zombie.vivo:
                                zombie.vida -= 5
                                guisante.timer.stop()
                                guisante.hide()
                                if not zombie.vivo:
                                    self.zombies_destruidos += 1
                                    self.zombies_restantes -= 1
                                    if self.dia:
                                        self.puntaje += p.PUNTAJE_ZOMBIE_DIURNO
                                    else:
                                        self.puntaje += p.PUNTAJE_ZOMBIE_NOCTURNO
                                break
        self.timer_impacto_abajo.start()
    
    def verificar_click_sol(self, coordenadas):
        for sol in self.soles_generados:
            if (sol.x() < coordenadas[0] < sol.x() + 50) and\
                 (sol.y() < coordenadas[1] < sol.y() + 50):
                if self.dia:
                    self.soles += p.SOLES_POR_RECOLECCION * 2
                else:
                    self.soles += p.SOLES_POR_RECOLECCION
                sol.hide()
                self.soles_generados.remove(sol)
                break
         
    def set_planta(self, tipo, pos_planta, pos):
        ventana_juego = self.sender()
        carril = pos_planta[1]
        elegible = None
        
        if carril == 180:
            if pos in list(self.plantas_carril_arriba.keys()):
                if self.plantas_carril_arriba[pos].viva:
                    elegible = False
                else:
                    del self.plantas_carril_arriba[pos]
                    elegible = True        
            else:
                elegible = True
            
            if elegible:
                if tipo == "girasol":
                    if self.soles >= p.COSTO_GIRASOL:
                        self.plantas_carril_arriba[pos] = Girasol(ventana_juego, pos_planta)
                        self.soles -= p.COSTO_GIRASOL
                elif tipo == "guisante":
                    if self.soles >= p.COSTO_LANZAGUISANTE:
                        self.plantas_carril_arriba[pos] = PlantaClasica(ventana_juego, pos_planta)
                        self.soles -= p.COSTO_LANZAGUISANTE
                elif tipo == "hielo":
                    if self.soles >= p.COSTO_LANZAGUISANTE_HIELO:
                        self.plantas_carril_arriba[pos] = PlantaAzul(ventana_juego, pos_planta)
                        self.soles -= p.COSTO_LANZAGUISANTE_HIELO
                elif tipo == "papa":
                    if self.soles >= p.COSTO_PAPA:
                        self.plantas_carril_arriba[pos] = Patata(ventana_juego, pos_planta)
                        self.soles -= p.COSTO_PAPA
            else:
                print("Posicion invalida")
        elif carril == 280:
            if pos in list(self.plantas_carril_abajo.keys()):
                if self.plantas_carril_abajo[pos].viva:
                    elegible = False
                else:
                    del self.plantas_carril_abajo[pos]
                    elegible = True       
            else:
                elegible = True

            if elegible:
                if tipo == "girasol":
                    if self.soles >= p.COSTO_GIRASOL:
                        self.plantas_carril_abajo[pos] = Girasol(ventana_juego, pos_planta)
                        self.soles -= p.COSTO_GIRASOL
                elif tipo == "guisante":
                    if self.soles >= p.COSTO_LANZAGUISANTE:
                        self.plantas_carril_abajo[pos] = PlantaClasica(ventana_juego, pos_planta)
                        self.soles -= p.COSTO_LANZAGUISANTE
                elif tipo == "hielo":
                    if self.soles >= p.COSTO_LANZAGUISANTE_HIELO:
                        self.plantas_carril_abajo[pos] = PlantaAzul(ventana_juego, pos_planta)
                        self.soles -= p.COSTO_LANZAGUISANTE_HIELO
                elif tipo == "papa":
                    if self.soles >= p.COSTO_PAPA:
                        self.plantas_carril_abajo[pos] = Patata(ventana_juego, pos_planta)
                        self.soles -= p.COSTO_PAPA
            else:
                print("Posicion invalida")

    def revisar_fin_ronda(self):
        if self.zombies_restantes == 0:
            print("has ganado")
            self.pausar()
            self.timer_fin_ronda.stop()
            self.puntaje_total += self.puntaje + self.puntaje * self.ponderador_dificultad
            self.senal_termino_ronda.emit(True, {'ronda': self.nivel,
            'zombies': self.zombies_destruidos,
            'soles': self.soles, 'puntaje': self.puntaje, 'puntaje total': self.puntaje_total})
            self.senal_termino_ronda_ventana.emit()
            self.nivel += 1
            self.soles = p.SOLES_INICIALES
            self.puntaje = 0
            self.n_zombies_generados = 0
            self.zombies_destruidos = 0   
            self.zombies_restantes = p.N_ZOMBIES * 2
            for planta in list(self.plantas_carril_abajo.values()) +\
                 list(self.plantas_carril_arriba.values()):
                planta.esconder()
            for sol in self.soles_generados:
                sol.hide()
            self.soles_generados = []
            self.plantas_carril_abajo = {}
            self.plantas_carril_arriba = {}
            self.senal_cargar_datos.emit({
            'soles': str(self.soles),
            'zombies restantes': str(self.zombies_restantes),
            'zombies destruidos': "0",
            'nivel': self.nivel,
            'puntaje': "0"
            })
        else:
            for zombie in self.zombies_carril_abajo + self.zombies_carril_arriba:
                if zombie.x() < 330:
                    print("has perdido")
                    self.pausar()
                    self.timer_fin_ronda.stop()
                    self.puntaje_total += self.puntaje
                    self.senal_termino_ronda.emit(False, {'ronda': self.nivel,
                    'zombies': self.zombies_destruidos,
                    'soles': self.soles, 'puntaje': self.puntaje,
                    'puntaje total': self.puntaje_total})
                    self.senal_termino_ronda_ventana.emit()
    
    def cheatcode_sol(self):
        self.soles += p.SOLES_EXTRA

    def terminar_ronda(self):
        for zombie in self.zombies_carril_abajo + self.zombies_carril_arriba:
            if zombie.vivo:
                zombie.vida = 0
                self.zombies_destruidos += 1
                self.zombies_restantes -= 1
        
                if self.dia:
                    self.puntaje += p.PUNTAJE_ZOMBIE_DIURNO
                else:
                    self.puntaje += p.PUNTAJE_ZOMBIE_NOCTURNO
            
        
         
                    


        


    

    













