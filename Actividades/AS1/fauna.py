from random import randint
from parametros import INCREMENTO_FEROCIDAD, MAX_EX_CARNIVORO, MAX_EX_HERVIBORO, \
                        MIN_EX_CARNIVORO, MIN_EX_HERVIBORO, INCREMENTO_ADORABILIDAD, \
                        GAN_CARNIVORO, GAN_HERBIVORO
from abc import ABC, abstractmethod
from random import randint


# MODIFICAR
class Animal(ABC):

    # MODIFICAR
    def __init__(self, especie, **kwargs):
        self.especie = especie
        self.ganancia_actual = 0

    # MODIFICAR
    @abstractmethod
    def alimentarse(self):
        pass

    # MODIFICAR
    @abstractmethod
    def exhibicion(self):
        pass

    def __str__(self):
        return f"Animal de especie {self.especie}"


# MODIFICAR
class Carnivoro(Animal):

    # MODIFICAR
    def __init__(self, ferocidad, **kwargs):
        super().__init__(**kwargs)
        self.ferocidad = ferocidad
        self.ganancia_actual += GAN_CARNIVORO

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        self.ferocidad += INCREMENTO_FEROCIDAD
        print(f"Animal {self.especie} se come un kilogramo de Carne")

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        ponderador = randint(MIN_EX_CARNIVORO, MAX_EX_CARNIVORO)
        self.ganancia_actual += self.ferocidad * ponderador


# MODIFICAR
class Herbivoro(Animal):

    # MODIFICAR
    def __init__(self, adorabilidad, **kwargs):
        super().__init__(**kwargs)
        self.adorabilidad = adorabilidad
        self.ganancia_actual += GAN_HERBIVORO

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        self.adorabilidad += INCREMENTO_ADORABILIDAD
        print(f"Animal {self.especie} se come un kilogramo de Vegetales")

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        ponderador = randint(MIN_EX_HERVIBORO, MAX_EX_HERVIBORO)
        self.ganancia_actual += self.adorabilidad * ponderador 



# MODIFICAR
class Omnivoro(Carnivoro, Herbivoro):

    # MODIFICAR
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()

