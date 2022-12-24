import socket
import json
import sys
from threading import Thread
from PyQt5.QtCore import QObject, pyqtSignal
from cripto import encriptar, desencriptar
from funciones import read_json


class Cliente(QObject):
    senal_mostrar_ventana_inicio = pyqtSignal()
    senal_procesar_comando = pyqtSignal(dict)
    def __init__(self):
        super().__init__()
        self.host = read_json("host")
        self.port = read_json("port")
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start_client(self):
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.thread_listen_server()
            self.senal_mostrar_ventana_inicio.emit()

        except ConnectionError as error:
            print(f"Error de conexion: revise que el servidor este concectado. {error}")
            self.socket_cliente.close()
        
    def thread_listen_server(self):
        thread_escuchar_server = Thread(target=self.escuchar_server)
        thread_escuchar_server.start()
    
    def escuchar_server(self):
        while True:
            try:
                mensaje = self.recibir_mensaje()
                self.senal_procesar_comando.emit(mensaje)

            except ConnectionError as error:
                print("Error de conexion.", error)
                break
    
    def recibir_mensaje(self):
        mensaje_final = bytearray()
        largo = int.from_bytes(self.socket_cliente.recv(4), byteorder='big')

        while largo >= 32:
            num_bloque_bytes = self.socket_cliente.recv(4)
            num_bloque = int.from_bytes(num_bloque_bytes, byteorder='little')
            bloque = self.socket_cliente.recv(32)
            mensaje_final += bloque
            largo -= 32
        
        if largo != 0:
            num_bloque_bytes = self.socket_cliente.recv(4)
            num_bloque = int.from_bytes(num_bloque_bytes, byteorder='little')
            bloque = self.socket_cliente.recv(32)
            mensaje_final += bloque[0:largo]
        mensaje_final = self.decodificar_mensaje(desencriptar(mensaje_final))
        
        return mensaje_final
    
    def enviar_comando(self, comando):
        pos = 1
        comando = encriptar(bytearray(self.codificar_mensaje(comando)))

    
        mensaje_bytes = bytearray(comando)
        largo = len(mensaje_bytes)
        largo_bytes = largo.to_bytes(4, byteorder='big')
        self.socket_cliente.sendall(bytearray(largo_bytes))

        if largo <= 32:
            num_bloque = pos.to_bytes(4, byteorder='little')
            self.socket_cliente.sendall(num_bloque + mensaje_bytes + b'\x00' * (32 - largo))
            
        else:
            while largo > 32:

                num_bloque = pos.to_bytes(4, byteorder='little')
                bytes_mensaje = mensaje_bytes[32 * (pos - 1): 32 * pos]
                self.socket_cliente.sendall(num_bloque + bytes_mensaje)
                largo -= 32
                pos += 1

            num_bloque = pos.to_bytes(4, byteorder='little')
            bytes_mensaje = mensaje_bytes[32 * (pos - 1): (32 * (pos - 1) + largo)]
            self.socket_cliente.sendall(num_bloque + bytes_mensaje)
            
    def codificar_mensaje(self, comando):
        json_serializado = json.dumps(comando)
        comando_codificado = json_serializado.encode('utf-8')
        return comando_codificado
    
    def decodificar_mensaje(self, comando):
        comando_decodificado = comando.decode('utf-8')
        comando_deserializado = json.loads(comando_decodificado)
        return comando_deserializado

    
    
    
    


        







    
        