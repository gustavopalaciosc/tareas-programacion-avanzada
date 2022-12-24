from abc import ABC, abstractmethod
from random import randint
from parametros import MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA,\
MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO

class Programon(ABC):
    def __init__(self, nombre, nivel, tipo, vida, ataque, defensa, velocidad):
        self.nombre = nombre
        self._nivel = int(nivel)
        self._experiencia = 0
        self.tipo = tipo
        self._vida = int(vida)
        self._ataque = int(ataque)
        self._defensa = int(defensa)
        self._velocidad = int(velocidad)
        self.tipo_debil = None
        self.tipo_fuerte = None

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        if valor > 100:
            self._nivel = 100
        elif valor < 0:
            self._nivel = 0
        else:
            self._nivel = valor
    
    @property 
    def experiencia(self):
        return self._experiencia
    
    @experiencia.setter
    def experiencia(self, valor):
        if self.nivel == 100:
            self._experiencia = 0
        else:
            if valor >= 100:
                self.nivel += 1
                self._experiencia = valor - 100
                if self.nivel == 100:
                    self._experiencia = 0
                self.vida += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
                self.ataque += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
                self.defensa += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
                self.velocidad += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            else:
                self._experiencia = valor
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, valor):
        if valor > 255:
            self._vida = 255
        elif valor < 1:
            self._vida = 1
        else:
            self._vida = valor
    
    @property
    def ataque(self):
        return self._ataque
    
    @ataque.setter
    def ataque(self, valor):
        if valor > 190:
            self._ataque = 190
        elif valor < 5:
            self._ataque = 5
        else:
            self._ataque = valor

    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, valor):
        if valor > 200:
            self._velocidad = 200
        elif valor < 5:
            self._velocidad = 5
        else:
            self._velocidad = valor
    
    @property
    def defensa(self):
        return self._defensa
    
    @defensa.setter
    def defensa(self, valor):
        if valor > 250:
            self._defensa = 250
        elif valor < 5:
            self._defensa = 5
        else:
            self._defensa = valor
    

    @abstractmethod
    def entrenamiento(self):
        if self.nivel < 100:
            aumento_experiencia = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
            print(f"Has entrenado a {self.nombre} y ha quedado MAMADISIMO.")
            print(f"Su experiencia a aumentado en {aumento_experiencia}")
            self.experiencia += aumento_experiencia
            print(f"Nivel de tu programon: {self.nivel}")
        else:
            print("Tu programon ya es nivel 100. Los entrenamientos ya no hacen efecto")
            
        

    @abstractmethod
    def luchar(self, tipo):
        ventaja_tipo = 0
        if tipo == self.tipo_fuerte:
            ventaja_tipo = 1
        elif tipo == self.tipo_debil:
            ventaja_tipo = -1
        
        puntaje_de_victoria = max(0, self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15 +\
             self.defensa * 0.15 + self.velocidad * 0.2 + ventaja_tipo * 40)
        return puntaje_de_victoria


class Planta(Programon):
    def __init__(self, nombre, nivel, tipo, vida, ataque, defensa, velocidad):
        super().__init__(nombre, nivel, tipo, vida, ataque, defensa, velocidad)
        self.tipo_fuerte = "agua"
        self.tipo_debil = "fuego"

    def entrenamiento(self):
        return super().entrenamiento()

    def luchar(self, tipo):
        return super().luchar(tipo)


class Fuego(Programon):
    def __init__(self, nombre, nivel, tipo, vida, ataque, defensa, velocidad):
        super().__init__(nombre, nivel, tipo, vida, ataque, defensa, velocidad)
        self.tipo_fuerte = "planta"
        self.tipo_debil = "agua"

    def entrenamiento(self):
        return super().entrenamiento()

    def luchar(self, tipo):
        return super().luchar(tipo)


class Agua(Programon):
    def __init__(self, nombre, nivel, tipo, vida, ataque, defensa, velocidad):
        super().__init__(nombre, nivel, tipo, vida, ataque, defensa, velocidad)
        self.tipo_fuerte = "fuego"
        self.tipo_debil = "planta"

    def entrenamiento(self):
        return super().entrenamiento()

    def luchar(self, tipo):
        return super().luchar(tipo)



