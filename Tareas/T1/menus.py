from abc import ABC, abstractmethod
from sys import exit
from funciones import len_csv_file, print_entrenadores, dict_entrenadores
from ligaprogramon import LigaProgramon
from parametros import ENERGIA_ENTRENAMIENTO

class Menu(ABC):
    def __init__(self, opciones):
        self.opciones = opciones
    
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def salir(self):
        print("\n¡Muchas gracias por jugar! Nos vemos pronto")
        exit()


class MenuInicio(Menu):
    def __init__(self):
        self.num_entrenadores = len_csv_file('entrenadores.csv')
        super().__init__({"1": self.empezar_juego, f"{self.num_entrenadores}": self.salir})
        self.liga_programon = None
        

    def run(self):
        self.liga_programon = LigaProgramon()
        while True:
            print("\n       *** Menu de inicio ***       ")
            print("-" * 45)
            print_entrenadores()
            print(f"[{self.num_entrenadores}] Salir")
            entrada = input("Eliga una opcion: ")
            opcion = self.opciones.get(entrada)
            if entrada == f"{self.num_entrenadores}":
                break           
            else:
                if entrada.isdigit():
                    if ( 1 <= int(entrada) <= self.num_entrenadores):
                        print("Has elegido a un entrenador")
                        opcion = self.empezar_juego
                        entrenador = dict_entrenadores()[entrada] 
                        for i in self.liga_programon.entrenadores:
                            if i.nombre == entrenador:
                                self.liga_programon.mi_entrenador = i
                                self.liga_programon.entrenadores.remove(i)
                                break
                        break
                    else:
                        print("Opcion invalida!")
                else:
                    print("Opcion invalida!")           
        return opcion()
                
    def empezar_juego(self):
        menu_crear_objeto = MenuCrearObjeto(self.liga_programon)
        menu_entrenamiento = MenuEntrenamiento(self.liga_programon)
        menu_estado_entrenador = MenuEstadoEntrenador(self.liga_programon)
        menu_simulacion = MenuSimulacion(self.liga_programon)
        menu_utilizar_objeto = MenuUtilizarObjeto(self.liga_programon)
        menu_entrenador = MenuEntrenador(menu_entrenamiento, menu_simulacion, menu_crear_objeto,\
             menu_utilizar_objeto, menu_estado_entrenador, self.liga_programon)
        menu_entrenador.run()
        self.run()
    
    def salir(self):
        return super().salir()
    
    

class MenuEntrenador(Menu):
    def __init__(self, menu_entrenamiento, menu_simulacion_ronda, menu_crear_objeto,\
        menu_utilizar_objeto, menu_estado_entrenador, liga_programon):
        super().__init__({"1": self.entrenamiento, "2": self.simular_ronda,\
                          "3": self.resumen_campeonato, "4": self.crear_objeto,\
                          "5": self.utilizar_objeto, "6": self.estado_entrenador,\
                          "7": self.volver, "8": self.salir})
        self.menu_entrenamiento = menu_entrenamiento
        self.menu_simulacion_ronda = menu_simulacion_ronda
        self.menu_crear_objeto = menu_crear_objeto
        self.menu_utilizar_objeto = menu_utilizar_objeto
        self.menu_estado_entrenador = menu_estado_entrenador
        self.liga_programon = liga_programon
        
    
    def run(self):
        if self.liga_programon.mi_entrenador.en_juego:
            while True:
                print("\n  *** Menu Entrenador ***  ")
                print("-" * 27)
                print("[1] Entrenamiento")
                print("[2] Simular ronda")
                print("[3] Resumen campeonato")
                print("[4] Crear objeto")
                print("[5] Utilizar objeto")
                print("[6] Estado entrenador")
                print("[7] Volver")
                print("[8] Salir")
                entrada = input("Selecione una opcion: ")
                opcion = self.opciones.get(entrada)
                if opcion:
                    break
                else:
                    print("\n¡Opcion invalida! Debe elegir un numero entre 1 y 8\n")

            return opcion()
        else:
            print("\nPartida terminada. Muchas gracias por jugar\n")
            pass
    
    def entrenamiento(self):
        self.menu_entrenamiento.run()
        self.run()

    def simular_ronda(self):
        self.menu_simulacion_ronda.run()
        self.run()

    def resumen_campeonato(self):
        self.liga_programon.resumen_campeonato()
        self.run()

    def crear_objeto(self):
        self.menu_crear_objeto.run()
        self.run()

    def utilizar_objeto(self):
        self.menu_utilizar_objeto.run()
        self.run()

    def estado_entrenador(self):
        self.menu_estado_entrenador.run()
        return self.run()

    def volver(self):
        pass

    def salir(self):
        return super().salir()


class MenuEntrenamiento(Menu):
    def __init__(self, liga_programon):
        self.liga_programon = liga_programon
        n_programones = len(self.liga_programon.mi_entrenador.programones)
        super().__init__({f"{n_programones + 1}": self.volver, f"{n_programones + 2}": self.salir})
        
    def run(self):
        n_programones = len(self.liga_programon.mi_entrenador.programones)
        if self.liga_programon.mi_entrenador.energia >= ENERGIA_ENTRENAMIENTO:
            while True:
                print("\n *** Menu de entrenamiento ***  ")
                print("-" * 32)
                for n in range(1, n_programones + 1):
                    print(f"[{n}] {self.liga_programon.mi_entrenador.programones[n - 1].nombre}")
                print(f"[{n_programones + 1}] Volver")
                print(f"[{n_programones + 2}] Salir")

                entrada = input("Eliga una opcion: ")
                if entrada.isdigit():
                    if 1 <= int(entrada) <= n_programones:
                        break
                    elif (n_programones + 1) <= int(entrada) <= (n_programones + 2):
                        opcion = self.opciones.get(entrada)
                        break
                    else:
                        print("\nOpcion invalida\n")
                else:
                    print("\nOpcion invalida\n")
            
            if 1 <= int(entrada) <= n_programones:
                self.liga_programon.mi_entrenador.programones[int(entrada) - 1].entrenamiento()
                self.liga_programon.mi_entrenador.energia -= ENERGIA_ENTRENAMIENTO
            else:
                return opcion()
        else:
            print("\nNo tienes energia suficiente para entrenar a tus programones")

    def volver(self):
        pass

    def salir(self):
        return super().salir()



class MenuSimulacion(Menu):
    def __init__(self, liga_programon):
        self.liga_programon = liga_programon
        largo = len(self.liga_programon.mi_entrenador.programones)
        super().__init__({f"{largo + 1}": self.volver, f"{largo + 2}": self.salir})

    def run(self):
        largo =  len(self.liga_programon.mi_entrenador.programones)
        while True:
            print("\n  *** Elige tu luchador ***    ")
            print(31 * "-")
            for i in range(1, largo + 1):
                print(f"[{i}] {self.liga_programon.mi_entrenador.programones[i - 1].nombre}")
            print(f"[{largo + 1}] Volver")
            print(f"[{largo + 2}] Salir")

            entrada = input("Eliga una opcion: ")
            opcion = self.opciones.get(entrada)
            if entrada.isdigit():
                if 1 <= int(entrada) <= (largo + 2): 
                    break
                else:
                    print("Opcion invalida")
            else:
                print("Opcion invalida")
        
        if 1 <= int(entrada) <= largo:
            return self.simular(self.liga_programon.mi_entrenador.programones[int(entrada) - 1])
        else:
            return opcion()
    
    def simular(self, programon_entrenador):
        self.liga_programon.simular_ronda(programon_entrenador)
    
    def volver(self):
        pass

    def salir(self):
        return super().salir()


class MenuCrearObjeto(Menu):
    def __init__(self, liga_programon):
        super().__init__({"1": self.crear_objeto, "2": self.crear_objeto, "3": self.crear_objeto,\
             "4": self.volver, "5": self.salir})
        self.liga_programon = liga_programon
    
    def run(self):
        while True:
            print("\n  *** Menu Objetos ***    ")
            print(26 * "-")
            print("[1] Baya")
            print("[2] Pocion")
            print("[3] Caramelo")
            print("[4] Volver")
            print("[5] Salir")
            entrada = input("Eliga una opcion: ")
            opcion = self.opciones.get(entrada)

            if opcion:
                break
            else:
                print("Opcion invalida")
        
        if 1 <= int(entrada) <= 3:
            return opcion(entrada)
        else:
            return opcion()
    
    def crear_objeto(self, tipo):
        self.liga_programon.mi_entrenador.crear_objeto(tipo)

    def volver(self):
        pass

    def salir(self):
        return super().salir()


class MenuUtilizarObjeto(Menu):
    def __init__(self, liga_programon):
        self.liga_programon = liga_programon
        
    def run(self):
        n_objetos = len(self.liga_programon.mi_entrenador.objetos)
        if n_objetos == 0:
            print("\nNo tienes ningun objeto para usar")
        else:
            while True:
                print("\n  *** Objetos disponibles ***   ")
                print(32 * "-")
                for i in range(1, n_objetos + 1):
                    print(f"[{i}] {self.liga_programon.mi_entrenador.objetos[i - 1].nombre}")
                print(f"[{n_objetos + 1}] Volver")
                print(f"[{n_objetos + 2}] Salir")

                entrada = input("Eliga una opcion: ")

                if entrada.isdigit():
                    if 1 <= int(entrada) <= n_objetos:
                        opcion = self.utilizar_objeto
                        break
                    elif int(entrada) == (n_objetos + 1):
                        opcion = self.volver
                        break
                    elif int(entrada) == (n_objetos + 2):
                        opcion = self.salir
                        break
                    else:
                        print("\nOpcion invalida\n")
                else:
                    print("\nOpcion invalida\n")
            
            if 1 <= int(entrada) <= n_objetos:
                return opcion(int(entrada) - 1)
            else:
                return opcion()

    def utilizar_objeto(self, entrada):
        mi_objeto = self.liga_programon.mi_entrenador.objetos[entrada]
        print(f"Has elegido utilizar {mi_objeto.nombre}")
        while True:
            print("Elige el programon al que le quieres aplicar el objeto: ")
            for i in range(0, len(self.liga_programon.mi_entrenador.programones)):
                print(f"[{i + 1}] {self.liga_programon.mi_entrenador.programones[i].nombre}")
            opcion = input("Eliga una opcion: ")
            if opcion.isdigit():
                if int(opcion) - 1 in range(0, len(self.liga_programon.mi_entrenador.programones)):
                    mi_objeto.aplicar_objeto(self.liga_programon.mi_entrenador.programones[int(opcion) - 1])
                    del self.liga_programon.mi_entrenador.objetos[entrada]
                    break
                else:
                    print("\nOpcion invalida\n")
            else:
                print("\nOpcion invalida\n")

    def volver(self):
        pass

    def salir(self):
        return super().salir()


class MenuEstadoEntrenador(Menu):
    def __init__(self, liga_progamon):
        super().__init__({"1": self.volver, "2": self.salir})
        self.liga_programon = liga_progamon
    
    def run(self):
        while True:
            self.liga_programon.mi_entrenador.estado_entrenador()
            print("[1] Volver")
            print("[2] Salir")    
            entrada = input("Eliga una opcion: ")
            opcion = self.opciones.get(entrada)
            if opcion:
                break
            else:
                print("\n¡Opcion invalida!\n")    
        return opcion()

    def volver(self):
        pass

    def salir(self):
        return super().salir()
