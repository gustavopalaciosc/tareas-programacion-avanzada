from lista_entrenadores import lista_entrenadores
from random import choice, random
from funciones import beneficio_victoria


class LigaProgramon:
    def __init__(self):
        self.entrenadores = lista_entrenadores()
        self.perdedores = []
        self.entrenadores_totales = lista_entrenadores()
        self.ronda_actual = 1
        self.campeon = None
        self.mi_entrenador = None
         
    def resumen_campeonato(self):
        print(f"\n{' ' * 20} Resumen Campeonato {' ' * 20}")
        print("-" * 65)
        print(f"Participantes: {self.nombres_entrenadores()}")
        print(f"Ronda actual: {self.ronda_actual}")
        print(f"Entrenadores que siguen en competencia: {self.nombres_entrenadores_competencia()}")

    def simular_ronda(self, programon_entrenador):
        ganadores = []
        print(f"{' ' * 27}Ronda {self.ronda_actual}{' ' * 26}")
        print("-" * 60)
        print(f"Has elegido para luchar a {programon_entrenador.nombre}")
        if self.ronda_actual != 4:
            for i in range(0, int(8/self.ronda_actual) - 1):
                jugador_uno = choice(self.entrenadores)
                self.entrenadores.remove(jugador_uno)
                jugador_dos = choice(self.entrenadores)
                self.entrenadores.remove(jugador_dos)

                programon_uno = choice(jugador_uno.programones)
                programon_dos = choice(jugador_dos.programones)

                punto_uno = programon_uno.luchar(programon_dos.tipo)
                punto_dos = programon_dos.luchar(programon_uno.tipo)

                print(f"{jugador_uno.nombre} usando al programon {programon_uno.nombre}, \
se enfrenta a {jugador_dos.nombre} usando al programon {programon_dos.nombre}")

                if punto_uno > punto_dos:
                    print(f"{jugador_uno.nombre} a ganado la batalla")
                    beneficio_victoria(programon_uno)
                    jugador_uno.energia = 100
                    ganadores.append(jugador_uno)
                    self.perdedores.append(jugador_dos)
                elif punto_uno < punto_dos:
                    print(f"{jugador_dos.nombre} a ganado la batalla")
                    beneficio_victoria(programon_dos)
                    jugador_dos.energia = 100
                    ganadores.append(jugador_dos)
                    self.perdedores.append(jugador_uno)
                else:
                    valor = random()
                    if valor >= 0.5:
                        print(f"{jugador_uno.nombre} a ganado la batalla")
                        beneficio_victoria(programon_uno)
                        jugador_uno.energia = 100
                        ganadores.append(jugador_uno)
                        self.perdedores.append(jugador_dos)
                    else:
                        print(f"{jugador_dos.nombre} a ganado la batalla")
                        beneficio_victoria(programon_dos)
                        jugador_dos.energia = 100
                        ganadores.append(jugador_dos)
                        self.perdedores(jugador_uno)

            rival = choice(self.entrenadores[0].programones)
            mi_puntaje = programon_entrenador.luchar(rival.tipo)
            puntaje_rival = rival.luchar(programon_entrenador.tipo)
            print(f"Usando a {programon_entrenador.nombre} te enfrentas a \
{self.entrenadores[0].nombre} usando al programon {rival.nombre}")

            if mi_puntaje > puntaje_rival:
                print("Has ganado la batalla")
                beneficio_victoria(programon_entrenador)
                self.mi_entrenador.energia = 100
                self.perdedores.append(self.entrenadores[0])
                del self.entrenadores[0]
            elif mi_puntaje < puntaje_rival:
                print("Has perdido la batalla")
                self.mi_entrenador.en_juego = False
            else:
                valor = random()
                if valor >= 0.5:
                    print("Has ganado la batalla")
                    beneficio_victoria(programon_entrenador)
                    self.mi_entrenador.energia = 100
                    self.perdedores.append(self.entrenadores[0])
                    del self.entrenadores[0]                 
                elif valor < 0.5:
                    print("Has perdido la batalla")
                    self.mi_entrenador.en_juego = False
            
            self.ronda_actual += 1
            self.entrenadores = ganadores
        
        elif self.ronda_actual == 4:
            rival = choice(self.entrenadores[0].programones)
            mi_puntaje = programon_entrenador.luchar(rival.tipo)
            puntaje_rival = rival.luchar(programon_entrenador.tipo)
            print(f"Usando a {programon_entrenador.nombre} te enfrentas a \
{self.entrenadores[0].nombre} usando al programon {rival.nombre}")

            if mi_puntaje > puntaje_rival:
                print("\n¡FELICITACIONES! Has ganado el Dccampeonato Programon")
                print("Finalmente te convertiste en un entrenador programon")
                self.perdedores.append(self.entrenadores[0])
                del self.entrenadores[0]
            elif mi_puntaje < puntaje_rival:
                print("Has perdido la batalla")
                
            else:
                valor = random()
                if valor >= 0.5:
                    print("¡FELICITACIONES! Has ganado el Dccampeonato Programon")
                    print("Finalmente te convertiste en un entrenador programon")
                    self.perdedores.append(self.entrenadores[0])
                    del self.entrenadores[0]                 
                elif valor < 0.5:
                    print("Has perdido la batalla")

            self.campeon = self.mi_entrenador
            self.mi_entrenador.en_juego = False

    def nombres_entrenadores(self):
        nombres = f"{self.mi_entrenador.nombre}, "
        largo = len(self.entrenadores_totales)
        for i in range(0, largo - 1):
            nombres += f"{self.entrenadores_totales[i].nombre}, "
        nombres += self.entrenadores_totales[largo - 1].nombre
        return nombres

    def nombres_entrenadores_competencia(self):
        nombres = f"{self.mi_entrenador.nombre}, "
        largo = len(self.entrenadores)
        for i in range(0, largo):
            if self.entrenadores[i] not in self.perdedores:
                nombres += f"{self.entrenadores[i].nombre}, "
        nombres = nombres[:-2] 
        return nombres

