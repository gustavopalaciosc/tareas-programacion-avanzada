from funciones import print_objetos
from random import choice, random
from lista_objetos import lista_bayas, lista_caramelos, lista_pociones
from parametros import GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO, GASTO_ENERGIA_POCION
from beautifultable import BeautifulTable

class Entrenador:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self._energia = energia
        self.programones = []
        self.objetos = []
        self.en_juego = True

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        if valor > 100:
            self._energia = 100
        elif valor < 0:
            self._energia = 0
        else:
            self._energia = valor

    def estado_entrenador(self):
        print("\n          *** Estado entrenador ***         ")
        print("-" * 44)
        print(f"Nombre: {self.nombre}")
        print(f"Energia: {self.energia}")
        print(f"Objetos: {print_objetos(self)}")
        print("-" * 44)
        print("               Programones                   ")
        print("-" * 44)
        tabla = BeautifulTable()
        tabla.columns.header = ["Nombre", "Tipo", "Nivel", "vida"]
        for programon in self.programones:
            tabla.rows.append([str(programon.nombre), str(programon.tipo), str(programon.nivel),\
                 str(programon.vida)])
        print(tabla)


    def crear_objeto(self, tipo):
        if tipo == "1":
            self.crear_objeto_especifico(lista_bayas(), GASTO_ENERGIA_BAYA)
        elif tipo == "2":
            self.crear_objeto_especifico(lista_pociones(), GASTO_ENERGIA_POCION)
        else:
            self.crear_objeto_especifico(lista_caramelos(), GASTO_ENERGIA_CARAMELO)
    
    def crear_objeto_especifico(self, lista_objetos, gasto_energia):
        if self.energia >= gasto_energia:
            objetos = lista_objetos
            mi_objeto = choice(objetos)
            if random() > mi_objeto.prob_exito:
                print(f"Has creado un {mi_objeto.nombre} del tipo {mi_objeto.tipo} exitosamente.")
                self.objetos.append(mi_objeto)
            else:
                print("No se ha podido crear el objeto. La suerte no estuvo de tu lado.")
            self.energia -= gasto_energia
            print(f"Energia utilizada: {gasto_energia}")
        else:
            print("\n¡No tienes energia suficiente para crear el objeto!")


