"""
Logica Servidor
-> Aquí la idea es que se procesen los comandos recibidos para retornar las respuestas, junto con
llevar los datos de la partida en curso.
"""
from entidades.usuario import Usuario
from random import choice


class LogicaServidor:
    def __init__(self, parent):
        self.parent = parent
        self.usuarios = {}
        self.nombres = []

    def procesar_comando(self, id, comando):
        """
        Función encargada de procesar los mensajes recibidos por el servidor
        de los distintos clientes.
        """
        #Set Name
        if comando['comando'] == "set_name":
            return self.set_user(id, comando)
                
        # En otro caso 
        elif comando['comando'] == 'comenzar_juego':
            mensaje = {'comando': 'set_inicial_cartas', 'cartas': self.usuarios[id].cartas}
            return mensaje
        
        elif comando['comando'] == 'carta_seleccionada':
            return self.seleccion_carta(id, comando)

        else:
            return {}
    
    # En base a lo que se envio a un jugador, se le envia un comando al otro jugador
    def procesar_comando_otros_usuarios(self, comando):
        if comando['comando'] == 'set_name':
            respuesta = {'comando': 'actualizar_datos_espera', 'nombres': self.nombres}
            return respuesta

        elif comando['comando'] == 'comenzar_juego':
            return False
        
        elif comando['comando'] == 'termino_ronda':
            return comando
    
    def procesar_nombre(self, nombre):
        if (1 <= len(nombre) <= 10) and nombre.isalnum():
            if nombre not in self.nombres:
                return True
            else:
                return False
        else:
            return False
    
    def set_user(self, id, comando):
        nombre = comando['name']
        if self.procesar_nombre(nombre):
            self.log("-", "Ingresar nombre de usuario valido", f"Nombre {nombre}")
            self.usuarios[id] = Usuario(nombre, id)
            self.nombres.append(nombre)
            self.log(self.usuarios[id].nombre, "Conectarse", "-")
            if len(self.nombres) == 2:
                self.log("-", "Comienza parida", f"Jugadores: {self.nombres}")

            return {'comando': 'set_name',
             'estado': 'aceptado', 
             'nombre': nombre , 
             'id_cliente': id,
             'otros_nombres': self.nombres
             }
            
        else:
            self.log("-", "Ingresar nombre de usuario invalido", f"Nombre {nombre}")
            return {'comando': 'set_name', 
            'estado': 'rechazado'}
  
    def seleccion_carta(self, id, comando):
        index = comando['index_carta']
        key = list(self.usuarios[id].cartas.keys())[index]
        carta_seleccionada = str(key)
        self.usuarios[id].carta_seleccionada = self.usuarios[id].cartas[carta_seleccionada]
        self.usuarios[id].key_carta_seleccionada = key
        self.log(self.usuarios[id].nombre, "Carta lanzada",\
             f"Carta tipo {self.usuarios[id].carta_seleccionada['elemento']}")

        for i in self.usuarios:
            if i != id:
                if self.usuarios[i].carta_seleccionada:
                    
                    ganador = self.verificar_carta_ganadora(self.usuarios[id].carta_seleccionada,\
                         id, self.usuarios[i].carta_seleccionada, i)

                    

                    if ganador == id:
                        carta_ganadora = self.usuarios[id].carta_seleccionada
                        carta_perdedora = self.usuarios[i].carta_seleccionada
                        id_perdedor = i
                        self.usuarios[i].descartar_carta()
                        

                    elif ganador == i:
                        carta_ganadora = self.usuarios[i].carta_seleccionada
                        carta_perdedora = self.usuarios[id].carta_seleccionada
                        id_perdedor = id
                        self.usuarios[id].descartar_carta()
                        

                    # Reseteo de seleccion de carta de ambos jugadores
                    gano = self.usuarios[ganador].verificar_victoria()
                    self.usuarios[id].carta_seleccionada = None
                    self.usuarios[id].key_carta_seleccionada = None
                    self.usuarios[i].carta_seleccionada = None
                    self.usuarios[i].key_carta_seleccionada = None

                    #print(self.usuarios[id].mazo_triunfo)
                    #print(self.usuarios[i].mazo_triunfo)
                    #print(gano)
                    self.log("-", "Fin ronda", f"Ganador: {self.usuarios[ganador].nombre}")
                    if gano:
                        self.log("-", "Termino partida", f"Ganador: {self.usuarios[ganador].nombre}")

                    return {'comando': 'termino_ronda',
                     'ganador': self.usuarios[ganador].nombre, 
                     'mazo_ganador': self.usuarios[ganador].cartas, 
                     'mazo_perdedor': self.usuarios[id_perdedor].cartas,
                     'carta_ganadora': carta_ganadora,
                     'carta_perdedora': carta_perdedora,
                     'victoria': gano} 
                    
        return False

    def verificar_carta_ganadora(self, carta_uno, id_uno, carta_dos, id_dos):
        if carta_uno['elemento'] == carta_dos['elemento']:

            if carta_uno['puntos'] > carta_dos['puntos']:
                self.usuarios[id_uno].eliminar_carta_ganadora()
                return id_uno

            elif carta_uno['puntos'] < carta_dos['puntos']:
                self.usuarios[id_dos].eliminar_carta_ganadora()
                return id_dos

            else:
                ganador = choice([id_uno, id_dos])
                self.usuarios[ganador].eliminar_carta_ganadora()
                
                return ganador

        else:

            if carta_uno['elemento'] == 'agua':

                if carta_dos['elemento'] == 'fuego':
                    self.usuarios[id_uno].eliminar_carta_ganadora()
                    return id_uno

                elif carta_dos['elemento'] == 'nieve':
                    self.usuarios[id_dos].eliminar_carta_ganadora()
                    return id_dos

            elif carta_uno['elemento'] == 'nieve':

                if carta_dos['elemento'] == 'fuego':
                    self.usuarios[id_dos].eliminar_carta_ganadora()
                    return id_dos

                elif carta_dos['elemento'] == 'agua':
                    self.usuarios[id_uno].eliminar_carta_ganadora()
                    return id_uno

            elif carta_uno['elemento'] == 'fuego':

                if carta_dos['elemento'] == 'agua':
                    self.usuarios[id_dos].eliminar_carta_ganadora()
                    return id_dos

                elif carta_dos['elemento'] == 'nieve':
                    self.usuarios[id_uno].eliminar_carta_ganadora()
                    return id_uno

    def log(self, cliente, evento, detalles):
        print(f"Cliente: {cliente} | Evento: {evento} | Detalles: {detalles}")



    
