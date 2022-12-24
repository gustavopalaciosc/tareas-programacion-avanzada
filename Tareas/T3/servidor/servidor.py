import socket
import json
from threading import Thread
from logica_servidor import LogicaServidor
from cripto import encriptar, desencriptar
from funciones import read_json

class Servidor:
    def __init__(self):
        self.host = read_json("host")
        self.port = read_json("port")
        self.sockets = {}
        self.id_jugador = 0
        self.logica = LogicaServidor(self)
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start_server(self):
        #Anclar y escuchar
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.port}: {self.host}")

        #Comenzar a aceptar clientes
        thread_aceptar_clientes = Thread(target=self.accept_clients, daemon=True)
        thread_aceptar_clientes.start()
        
    def accept_clients(self):
        while True:
            try:
                socket_cliente, address = self.socket_server.accept()
                print(f"Escuchando cliente desde direccion {address}")
                
                if self.lleno():
                    print("Cliente rechazado")
                    self.rechazar_cliente(socket_cliente)
                
                else:       
                    self.aceptar_cliente(socket_cliente)

            except ConnectionError:
                print("Error al aceptar al cliente")
    
    def aceptar_cliente(self, socket_cliente):

        self.sockets[self.id_jugador] = socket_cliente
        thread_escuchar_cliente = Thread(target=self.listen_client,
                     args=(self.id_jugador , socket_cliente),
                     daemon=True)
        thread_escuchar_cliente.start()
        self.id_jugador += 1

    def rechazar_cliente(self, socket_cliente):
        socket_cliente.close()
    
    def desconectar_cliente(self, id_cliente):
        del self.sockets[id_cliente]
    
    #Escuchar Cliente
    def listen_client(self, id_jugador, socket_cliente):
        while True:
            try:
                mensaje = self.recibir_mensaje(socket_cliente)
                respuesta = self.logica.procesar_comando(id_jugador, mensaje)
                if respuesta:
                    self.enviar_respuesta(respuesta, socket_cliente)
                    self.enviar_respuesta_general(respuesta, id_jugador)
      
            except ConnectionError:
                self.desconectar_usuario(id_jugador)
                break

    def recibir_mensaje(self, socket_cliente):
        mensaje_final = bytearray()
        largo = int.from_bytes(socket_cliente.recv(4), byteorder='big')

        while largo >= 32:
            num_bloque = socket_cliente.recv(4)
            bloque = socket_cliente.recv(32)
            mensaje_final += bloque
            largo -= 32
        
        if largo != 0:
            num_bloque = socket_cliente.recv(4)
            bloque = socket_cliente.recv(32)
            mensaje_final += bloque[0:largo]
        mensaje_final = self.decodificar_mensaje(desencriptar(mensaje_final))
        
        return mensaje_final

    def enviar_respuesta(self, mensaje, socket_cliente):
        pos = 1
        comando = encriptar(bytearray(self.codificar_mensaje(mensaje)))

        mensaje_bytes = bytearray(comando)
        largo = len(mensaje_bytes)
        largo_bytes = largo.to_bytes(4, byteorder='big')
        socket_cliente.sendall(bytearray(largo_bytes))

        if largo <= 32:
            num_bloque = pos.to_bytes(4, byteorder='little')
            socket_cliente.sendall(num_bloque + mensaje_bytes + b'\x00' * (32 - largo))
            
        else:
            while largo > 32:

                num_bloque = pos.to_bytes(4, byteorder='little')
                bytes_mensaje = mensaje_bytes[32 * (pos - 1): 32 * pos]
                socket_cliente.sendall(num_bloque + bytes_mensaje)
                largo -= 32
                pos += 1

            num_bloque = pos.to_bytes(4, byteorder='little')
            bytes_mensaje = mensaje_bytes[32 * (pos - 1): (32 * (pos - 1) + largo)]
            socket_cliente.sendall(num_bloque + bytes_mensaje)
    
    def enviar_respuesta_general(self, respuesta, id_jugador):

        mensaje = self.logica.procesar_comando_otros_usuarios(respuesta)
        if mensaje:
            for id in self.sockets: 
                if id != id_jugador:
                    self.enviar_respuesta(mensaje, self.sockets[id])
        else:
            pass
                
    def desconectar_usuario(self, id_jugador):
        socket_cliente = self.socket_server[id_jugador]
        socket_cliente.close()
        del self.sockets[id_jugador]
        self.logica.nombres.remove(self.logica.usuarios[id_jugador])
        del self.logica.usuarios[id_jugador]

        respuesta = {"comando": "adversario_desconectado"}

        self.enviar_respuesta_general(respuesta)
    
    def decodificar_mensaje(self, mensaje):
        mensaje_decode = mensaje.decode('utf-8')
        json_deserializado = json.loads(mensaje_decode)
        return json_deserializado 
    
    def codificar_mensaje(self, mensaje):
        mensaje_serializado = json.dumps(mensaje)
        mensaje_codificado = mensaje_serializado.encode('utf-8')
        return mensaje_codificado
    
    def lleno(self):
        if len(self.sockets) >= 2:
            return True
        else:
            return False
        
    
    
            
    





