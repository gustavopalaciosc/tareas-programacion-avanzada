from cartas import get_penguins


class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.cartas = get_penguins()
        self.mazo_triunfo = []
        self.carta_seleccionada = None
        self.key_carta_seleccionada = None
    
    def verificar_victoria(self):
        todos_distintos = self.verificar_todos_distintos()
        todos_iguales = self.verificar_todos_iguales()

        if todos_distintos or todos_iguales:
            return True
        else:
            return False

    def verificar_todos_distintos(self):
        elementos = []
        for carta in self.mazo_triunfo:
            elementos.append(carta['elemento'])
        
        if 'fuego' in elementos and 'agua' in elementos and 'nieve' in elementos:
            return True
        
        else:
            return False

    def verificar_todos_iguales(self):
        elementos = []
        for carta in self.mazo_triunfo:
            elementos.append(carta['elemento'])
        
        if elementos.count('fuego') == 3\
             or elementos.count('nieve') == 3\
                 or elementos.count('agua') == 3:
            return True
        else:
            return False
        
    def descartar_carta(self):
        carta = self.cartas.pop(self.key_carta_seleccionada)
        self.cartas[self.key_carta_seleccionada] = carta
    
    def eliminar_carta_ganadora(self):
        carta = self.carta_seleccionada
        self.mazo_triunfo.append(carta)
        del self.cartas[self.key_carta_seleccionada]

    