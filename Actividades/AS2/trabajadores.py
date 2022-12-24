from time import sleep
from threading import Thread

from centro_urbano import CentroUrbano

from parametros import ENERGIA_RECOLECTOR, ORO_RECOLECTADO, \
    TIEMPO_RECOLECCION, TIEMPO_CONSTRUCCION, ORO_CHOZA


# Completar
class Recolector(Thread):

    def __init__(self, nombre: str, centro_urbano: CentroUrbano) -> None:
        super().__init__()
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.energia = ENERGIA_RECOLECTOR
        self.oro = 0
        self.daemon = True
        # Completar

    def run(self) -> None:
        self.trabajar()
        self.ingresar_oro()
        self.dormir()

    def log(self, mensage: str) -> None:
        print(f"El recolector {self.nombre}: {mensage}")

    def trabajar(self):
        while self.energia > 0:
            self.oro += ORO_RECOLECTADO
            self.log(F"Ha recolectado {ORO_RECOLECTADO} de oro")
            self.energia -= 1
            sleep(TIEMPO_RECOLECCION)
        
            


    def ingresar_oro(self) -> None:
        with self.centro_urbano.lock_oro:
            self.log(f"Depositando {self.oro} de oro en centro urbano")
            self.centro_urbano.oro += self.oro
            self.oro = 0
            self.log(f"Cantidad de oro en el centro urbano: {self.centro_urbano.oro}")
        

    def dormir(self) -> None:
        self.log("ha terminado su turno, procede a mimir")


# Completar
class Constructor(Thread):

    def __init__(self, nombre, centro_urbano: CentroUrbano) -> None:
        super().__init__()
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.daemon = True
        # Completar

    def run(self) -> None:
        while self.retirar_oro():
            self.log("está construyendo una choza de bárbaros")
            sleep(TIEMPO_CONSTRUCCION)
            self.construir_choza()
        self.log("terminó su trabajo por el día")

    def log(self, mensage: str) -> None:
        print(f"El constructor {self.nombre}: {mensage}")

    def retirar_oro(self) -> bool:
        with self.centro_urbano.lock_oro:
            if self.centro_urbano.oro >= ORO_CHOZA:
                self.centro_urbano.oro -= ORO_CHOZA
                self.log(f"Se ha retirado exitosamente {ORO_CHOZA} de oro del centro urbano")
                return True
            else:
                self.log(f"No se tiene la cantidad de oro suficiente para construir una choza")
                return False


    def construir_choza(self) -> None:
        with self.centro_urbano.lock_chozas:
            self.centro_urbano.chozas += 1
            sleep(TIEMPO_CONSTRUCCION)
            self.log(f"Se ha agregado una choza al centro urbano. Total de chozas:\
 {self.centro_urbano.chozas}")


