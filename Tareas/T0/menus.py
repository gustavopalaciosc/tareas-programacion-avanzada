from partida import Partida, PartidaEmpezada
from os import listdir
from ranking_puntajes import ranking_puntajes
from tablero import print_tablero



class MenuInicio():
    
    def __init__(self, menu_juego):
        self.opciones = {"1": self.crear_partida, "2": self.cargar_partida, "3": self.ver_ranking, "0": self.salir}
        self.menu_juego = menu_juego

    def run(self):
        while True:
            print("*" * 19)
            print("*** Menu Inicio ***")
            print("*" * 19)
            print("[1] Crear Partida")
            print("[2] Cargar Partida")
            print("[3] Ver Ranking Puntajes")
            print("[0] Salir")
            entrada = input("Seleccione una opcion: ")
            opcion = self.opciones.get(entrada)
            if opcion:
                break
            else:
                print("\n¡Opción invalida! Debes elegir un número valido (0, 1, 2 o 3)\n")

        return opcion()
    
    def crear_partida(self):
        nombre = input("Ingrese un nombre de usuario: ")

        while True:
            largo = int(input("Ingrese el largo del tablero. Este debe ser un número entre 3 y 15: "))
            if (3 <= largo <= 15):
                break

            else:
                print("¡Debes seleccionar un numero entre 3 y 15!")

        while True:
            ancho = int(input("Ingrese el ancho del tablero. Este debe ser un número entre 3 y 15: "))
            if (3 <= ancho <= 15):
                break

            else:
                print("¡Debes seleccionar un numero entre 3 y 15!")
                    
        partida = Partida(nombre, largo, ancho)
        self.menu_juego.inicio_partida(partida)
        self.menu_juego.run()
        return self.run() #Cuando el usuario salga del menu de juego, vuelve al menu de inicio

    def cargar_partida(self):
        usuarios = listdir("partidas")
        if len(usuarios) != 0:
            print("Partidas disponibles: ")
            for nombre in range(0, len(usuarios)):
                usuarios[nombre] = usuarios[nombre][:-4]
                print(usuarios[nombre])
            print("\n")
        
            while True:
                usuario = input("Ingrese el nombre de usuario de la partida a cargar: ")
                if usuario in usuarios:
                    break

                else:
                    print("Ingrese un usuario valido!\n")

            file = open(f"partidas/{usuario}.txt",encoding="utf-8")
            a = file.readlines()[0].split(";")
            a[3] = list(a[3])
            a[4] = list(a[4])
            partida = PartidaEmpezada(usuario, int(a[1]), int(a[2]), a[3], a[4], int(a[5]), int(a[6]))
            file.close()
            print(f"Partida de {usuario}:")
            print(f"- Numero de bestias: {a[5]}")
            print(f"- Casillas descubiertas: {a[6]}")
            print("\n")
            self.menu_juego.inicio_partida(partida)
            self.menu_juego.run()
            return self.run()

        else:
            print("\nActualmente no hay partidas guardadas\n")
            return self.run()

    def ver_ranking(self):
        if len(open("puntajes.txt", "r", encoding="utf-8").readlines()) != 0:
            print("\nEl ranking actual de puntajes es el siguiente: ")
            ranking_puntajes()
            print("\n")
        
        else:
            print("\nActualmente no hay puntajes guardados\n")
            
        return self.run()
        
    def salir(self):
        print("¡Gracias por jugar! Nos vemos pronto.")


class MenuJuego():

    def __init__(self):   
        self.opciones = {"1": self.descubrir_sector, "2": self.guardar_partida, "3": self.salir_guardar, "4": self.salir_noguardar, "5": self.ver_tablero}
        self.partida = None
        self.partida_guardada = False
    
    def inicio_partida(self, partida):
        self.partida = partida
       
    def run(self):
        while True:
            print("*" * 21)
            print("*** Menu de Juego ***")
            print("*" * 21)
            print("[1] Descubrir sector")
            print("[2] Guardar partida")
            print("[3] Salir y guardar partida")
            print("[4] Salir sin guardar")
            print("[5] Ver tablero")
            entrada = input(f"Selecciona una opcion {self.partida.usuario}: ")
            opcion = self.opciones.get(entrada)

            if opcion:
                break

            else:
                print("\n¡Opción invalida! Debes elegir un número valido (1, 2, 3 o 4)\n")

        return opcion()

    def descubrir_sector(self):
        self.partida.descubre_sector()
        if self.partida.vivo:
            self.run()

        else:
            pass

    def guardar_partida(self):
        print("Guardando partida...")
        self.partida.guardar()
        self.run()

    def salir_guardar(self):
        print(f"\nPartida de {self.partida.usuario} guardada con exito\n")
        self.partida.guardar()
        print(f"Tu puntaje actual es {self.partida.calcular_puntaje()}")
        self.partida = None
        print("Volviendo al menu principal...\n")

    def salir_noguardar(self):
        print(f"\nFin a la partida de {self.partida.usuario}\n")
        print(f"Tu puntaje actual es {self.partida.calcular_puntaje()}. Puede que este puntaje no quede guardado.")
        self.partida = None
        print("Saliendo sin guardar...\n")
    
    def ver_tablero(self):
        print("\n")
        print_tablero(self.partida.tablero_jugador, utf8=False)
        print("\n")
        self.run()

        
            