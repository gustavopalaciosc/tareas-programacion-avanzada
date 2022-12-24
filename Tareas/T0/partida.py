from eliminar_partida import eliminar_partida
from parametros import PROB_BESTIA, POND_PUNT
import random
from math import ceil
from tablero import print_tablero
from verificador_coordenadas import verificar_cordenadas
from contabilizador_enemigos import cont_enemigos
from guarda_puntajes import guarda_puntajes, sobreescribir_puntaje, eliminar_puntaje


class Partida():
    """
    Clase para instanciar partidas nuevas.
    """
    def __init__(self, usuario, largo, ancho):
        self.usuario = usuario
        self.largo = largo
        self.ancho = ancho
        self.vivo = True
        self.tablero = []
        self.tablero_jugador = []
        self.n_bestias = ceil(self.largo * self.ancho * PROB_BESTIA)
        self.casillas_descubiertas = 0
        self.partida_guardada = False
        dim = self.largo * self.ancho
        elementos = list(self.n_bestias * 'N') + list((dim - self.n_bestias) * ' ')
        random.shuffle(elementos)

        for i in range(0, self.ancho):
            self.tablero.append(elementos[(self.largo * i):(self.largo * (i + 1))])
            self.tablero_jugador.append(list(self.largo * ' '))
            
        self.tablero = cont_enemigos(self.tablero)
        
    def descubre_sector(self):    
        while True:
            print("\n")
            print_tablero(self.tablero_jugador, utf8=False)
            print("\n")
            coordenadas = input("Eliga las coordenadas de la casilla a\
 descubrir(formato letra-numero, por ejemplo a1): ")

            if len(coordenadas) == 0:
                print("Ingrese coordenadas validas!\n")

            elif verificar_cordenadas(coordenadas, self.largo, self.ancho):
                letras = "ABCDEFGHIJKLMNO"

                if self.tablero[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())] != 'N':

                    if self.tablero_jugador[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())] == ' ':
                        self.tablero_jugador[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())]\
                         = self.tablero[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())]
                        print_tablero(self.tablero_jugador, utf8=False) 
                        self.casillas_descubiertas += 1

                        if self.casillas_descubiertas == (self.ancho * self.largo) - self.n_bestias:
                            print("¡FELICITACIONES! HAS GANADO\n")
                            print_tablero(self.tablero, utf8=False)
                            print(f"\nTu puntaje obtenido es de {self.calcular_puntaje()} puntos.\n")
                            self.vivo = False
                            guarda_puntajes(self.usuario, self.calcular_puntaje())
                            try:
                                eliminar_partida(self.usuario)
                            except FileNotFoundError:
                                pass
                        break
                    else:
                        print("¡Esa casilla ya ha sido descubierta!")
                                
                elif self.tablero[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())] == 'N':
                    self.tablero_jugador[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())] = 'N'
                    print_tablero(self.tablero_jugador, utf8=False) 
                    print("¡Te has topado con una bestia que esta MAMADISIMA! Has perdido D;")
                    print_tablero(self.tablero, utf8=False)
                    self.vivo = False
                    try:
                        eliminar_partida(self.usuario)
                        eliminar_puntaje(self.usuario)
                    except:
                        pass
                    break            
            
            else:
                print("Ingrese coordenadas validas!\n")
        
    def guardar(self):
        mipartida = open(f"partidas/{self.usuario}.txt", "w", encoding="utf-8")
        tablero = ""
        tablero_jugador = ""
        for fila in range(0, self.ancho):
            for i in range(0, self.largo):
                tablero += self.tablero[fila][i]
                tablero_jugador += self.tablero_jugador[fila][i]
        mipartida.write(f"{self.usuario};{self.largo};{self.ancho};{tablero};\
{tablero_jugador};{self.n_bestias};{self.casillas_descubiertas}")
        mipartida.close()
        
        if self.partida_guardada:
            sobreescribir_puntaje(self.usuario, self.calcular_puntaje())

        else:
            guarda_puntajes(self.usuario, self.calcular_puntaje())
        self.partida_guardada = True

    def calcular_puntaje(self):
        puntaje = self.casillas_descubiertas * self.n_bestias * POND_PUNT
        return puntaje


class PartidaEmpezada():
    """
    Clase para instanciar partidas cargadas.
    """
    def __init__(self, usuario, largo, ancho, tablero, tablero_jugador, n_bestias, casillas_descubiertas):
        self.usuario = usuario
        self.largo = largo
        self.ancho = ancho
        self.vivo = True
        self.tablero = []
        self.tablero_jugador = []
        self.n_bestias = n_bestias
        self.casillas_descubiertas = casillas_descubiertas

        for i in range(0, self.ancho):
                self.tablero.append(list(tablero)[(self.largo * i):(self.largo * (i + 1))])
                self.tablero_jugador.append(list(tablero_jugador)[(self.largo * i):(self.largo * (i + 1))])

    def descubre_sector(self):        
        while True:
            print("\n")
            print_tablero(self.tablero_jugador, utf8=False)
            print("\n")
            coordenadas = input("Eliga las coordenadas de la casilla a\
 descubrir(formato letra-numero, por ejemplo a1): ")

            if len(coordenadas) == 0:
                print("Ingrese coordenadas validas!\n")

            elif verificar_cordenadas(coordenadas, self.largo, self.ancho):
                letras = "ABCDEFGHIJKLMNO"

                if self.tablero[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())] != 'N':

                    if self.tablero_jugador[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())] == ' ':
                        self.tablero_jugador[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())]\
                         = self.tablero[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())]
                        print_tablero(self.tablero_jugador, utf8=False) 
                        self.casillas_descubiertas += 1

                        if self.casillas_descubiertas == (self.ancho * self.largo) - self.n_bestias:
                            print("¡FELICITACIONES! HAS GANADO\n")
                            print_tablero(self.tablero, utf8=False)
                            print(f"\nTu puntaje obtenido es de {self.calcular_puntaje()} puntos.\n")
                            self.vivo = False
                            sobreescribir_puntaje(self.usuario, self.calcular_puntaje())                           
                            eliminar_partida(self.usuario)
                        break

                    else:
                        print("¡Esa casilla ya ha sido descubierta!")
                
                elif self.tablero[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())] == 'N':
                    self.tablero_jugador[int(coordenadas[1:])][letras.index(coordenadas[0].capitalize())] = 'N'
                    print_tablero(self.tablero_jugador, utf8=False) 
                    print("¡Te has topado con una bestia que esta MAMADISIMA! Has perdido D;")
                    print_tablero(self.tablero, utf8=False)
                    self.vivo = False
                    eliminar_partida(self.usuario)
                    eliminar_puntaje(self.usuario)
                    break 
                                  
            else:
                print("Ingrese coordenadas validas!\n")

    def guardar(self):
        mipartida = open(f"partidas/{self.usuario}.txt", "w", encoding="utf-8")
        tablero = ""
        tablero_jugador = ""
        for fila in range(0, self.ancho):
            for i in range(0, self.largo):
                tablero += self.tablero[fila][i]
                tablero_jugador += self.tablero_jugador[fila][i]
        mipartida.write(f"{self.usuario};{self.largo};{self.ancho};{tablero};\
{tablero_jugador};{self.n_bestias};{self.casillas_descubiertas}")
        mipartida.close()
        sobreescribir_puntaje(self.usuario, self.calcular_puntaje())
    
    def calcular_puntaje(self):
        puntaje = self.casillas_descubiertas * self.n_bestias * POND_PUNT
        return puntaje

        








        

    

    
