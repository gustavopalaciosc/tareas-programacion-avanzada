"""
En este archivo se encuentra la clase ListaReproduccion, la Iterable que
contiene los videos ordenados
"""


class ListaReproduccion:

    def __init__(self, lista_canciones, usuario, nombre):
        self.lista_canciones = lista_canciones
        self.usuario = usuario
        self.nombre = nombre

    def __iter__(self):
        # Debes completar este método
        return IterarLista(self.lista_canciones.copy())

    def __str__(self):
        return f"Lista de Reproducción de {self.usuario}: {self.nombre}"


class IterarLista:

    def __init__(self, lista_canciones):
        self.lista_canciones = lista_canciones

    def __iter__(self):
        # Debes completar este método
        return self

    def __next__(self):
        # Debes completar este método
        try:
            cancion_siguiente=(
                max(self.lista_canciones, key= lambda x: x[1]))
            self.lista_canciones.remove(cancion_siguiente)
            return cancion_siguiente[0]
        except:
            raise StopIteration
