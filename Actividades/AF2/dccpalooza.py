from parametros import PROBABILIDAD_EVENTO, PUBLICO_EXITO, PUBLICO_INICIAL, \
                       PUBLICO_TERREMOTO, AFINIDAD_OLA_CALOR, \
                       AFINIDAD_LLUVIA, PUBLICO_OLA_CALOR
from random import random, choice


class DCCPalooza:

    def __init__(self):
        self.artista_actual = ''
        self.__dia = 1
        self.line_up = []
        self.cant_publico = PUBLICO_INICIAL
        self.artistas = []
        self.prob_evento = PROBABILIDAD_EVENTO
        self.suministros = []

    @property
    def dia(self):
        return self.__dia

    @property
    def funcionando(self):
        return self.exito_del_concierto and self.dia <= 3

    @property
    def exito_del_concierto(self):
        return self.cant_publico >= PUBLICO_EXITO

    def imprimir_estado(self):
        print(f"Día: {self.__dia}\nCantidad de Personas: "
              f"{self.cant_publico}\nArtistas:")
        for artista in self.line_up:
            print(f"- {artista.nombre}")

    def ingresar_artista(self, artista):
        self.line_up.append(artista)
        print(f'Se ha ingresado un nuevo artista!!!\n{artista}')

    def asignar_lineup(self):
        self.line_up = []
        for artista in self.artistas:
            if self.dia == artista.dia_presentacion:
                self.ingresar_artista(artista)

    def nuevo_dia(self):
        if self.exito_del_concierto:
            self.__dia += 1
            if self.__dia <= 3:
                print("Comienza un nuevo dia")

    def ejecutar_evento(self):
        if random() < self.prob_evento:
            evento = choice(["Lluvia", "Terremoto", "Ola de calor"])
            if evento == "Lluvia":
                self.artista_actual.afinidad_con_publico -= AFINIDAD_LLUVIA
                print(f"Ha tocado lluvia. La afinidad con el publico a bajado a {self.artista_actual.afinidad_con_publico}")
            elif evento == "Terremoto":
                self.cant_publico -= PUBLICO_TERREMOTO
                print(f"Ha tocado un terremoto. La cantidad de publico a bajado a {self.cant_publico}")
            else:
                self.artista_actual.afinidad_con_publico -= AFINIDAD_OLA_CALOR
                self.cant_publico -= PUBLICO_OLA_CALOR
                print(f"Ha tocado una ola de calor. La afinidad con el publico a bajado a {self.artista_actual.afinidad_con_publico}")
                print(f"Además, la cantidad de publico a bajado a {self.cant_publico}")