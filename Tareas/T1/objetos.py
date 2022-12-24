from abc import ABC, abstractmethod
from parametros import PROB_EXITO_BAYA, PROB_EXITO_CARAMELO, PROB_EXITO_POCION,\
     GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO, GASTO_ENERGIA_POCION, AUMENTO_DEFENSA
from random import randint

class Objeto(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.costo = None
        self.prob_exito = None

    @abstractmethod
    def aplicar_objeto(self, programon):
        print(f"Programon beneficiado: {programon.nombre}")
        print(f"Objeto utilizado: {self.nombre} (Tipo {self.tipo})")


class Baya(Objeto):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.costo = GASTO_ENERGIA_BAYA
        self.prob_exito = PROB_EXITO_BAYA
        
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        aumento_vida = randint(1, 10)
        print(f"Aumento vida: {aumento_vida}")
        print(f"La vida subio de {programon.vida} a {programon.vida + aumento_vida}")
        programon.vida += aumento_vida


class Pocion(Objeto):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.costo = GASTO_ENERGIA_POCION
        self.prob_exito = PROB_EXITO_POCION    
    
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        aumento_ataque = randint(1, 7)
        print(f"Aumento ataque: {aumento_ataque}")
        print(f"El ataque subio de {programon.ataque} a {programon.ataque + aumento_ataque}")
        programon.ataque += aumento_ataque


class Caramelo(Baya, Pocion):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.costo = GASTO_ENERGIA_CARAMELO
        self.prob_exito = PROB_EXITO_CARAMELO
    
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        print(f"Aumento defensa: {AUMENTO_DEFENSA}")
        print(f"La defensa subio de {programon.defensa} a {programon.defensa + AUMENTO_DEFENSA}")
        programon.defensa += AUMENTO_DEFENSA


        