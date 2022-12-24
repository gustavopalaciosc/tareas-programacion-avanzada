"""
Modulo contiene implementación principal del cliente
"""
from PyQt5.QtCore import pyqtSignal, QObject
import socket
import json
from threading import Thread


class Cliente(QObject):
    senal_mostrar_ventana_carga = pyqtSignal()
    senal_manejar_mensaje = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()
            self.senal_mostrar_ventana_carga.emit()

        except ConnectionError as e:
            print(f"\n-ERROR: El servidor no está inicializado. {e}-")
        except ConnectionRefusedError as e:
            print(f"\n-ERROR: No se pudo conectar al servidor.{e}-")

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        # TODO: Completado por estudiante
        try:
            while self.conectado:
                mensaje = self.recibir()
                if mensaje:
                    self.senal_manejar_mensaje.emit(mensaje)

        except ConnectionError as error:
            print("Error: el servidor se a desconectado.", error)




    def recibir(self):
        """
        Se encarga de recibir lis mensajes del servidor.
        """
        # TODO: Completado por estudiante
        largo_mensaje_bytes = self.socket_cliente.recv(4)
        largo_mensaje= int.from_bytes(largo_mensaje_bytes, byteorder='little')
        bytes_mensaje = bytearray()

        while len(bytes_mensaje) < largo_mensaje:
            tamano_chunk = min(largo_mensaje - len(bytes_mensaje), 64)
            bytes_mensaje +=  self.socket_cliente.recv(tamano_chunk)
        
        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje

    def enviar(self, mensaje):
        """
        Envía un mensaje a un cliente.
        """
        # TODO: Completado por estudiante
        bytes_mensaje = self.codificar_mensaje(mensaje)

        largo_mensaje_bytes = len(bytes_mensaje).to_bytes(4, byteorder='little')
        self.socket_cliente.sendall(largo_mensaje_bytes + bytes_mensaje)




    def codificar_mensaje(self, mensaje):
        # TODO: Completado por estudiante

        try:

            mensaje_codificado = json.dumps(mensaje)
            mensaje_bytes = mensaje_codificado.encode()
            return mensaje_bytes
        
        except json.JSONDecodeError:
            print("Error: no se pudo codificar el mensaje")
            return b""






    def decodificar_mensaje(self, mensaje_bytes):
        try:
            mensaje = json.loads(mensaje_bytes)
            return mensaje
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}
