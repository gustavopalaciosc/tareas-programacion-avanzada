"""
Modulo contiene la implementación principal del servidor
"""
import json
import socket
import threading
from logica import Logica


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.logica = Logica(self)
        self.id_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.sockets = {}
        self.iniciar_servidor()

    def iniciar_servidor(self):
        """
        Crea el socket, lo enlaza y comienza a escuchar
        """
        # TODO: Completado por estudiante
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.log(f"Escuchando en host {self.host} y puerto {self.port}")
        self.comenzar_a_aceptar()







    def comenzar_a_aceptar(self):
        """
        Crea y comienza el thread encargado de aceptar clientes
        """
        thread = threading.Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()

    def aceptar_clientes(self):
        """
        Es arrancado como thread para de aceptar clientes, este se ejecuta
        siempre que se este conectado y acepta el socket del servidor. Luego
        se crea y comienza a escuchar al cliente. para finalmente aumentar en 1
        el id_cliente.
        """
        # TODO: Completado por estudiante
        while True:
            try:
                socket_cliente, adress = self.socket_servidor.accept()
                self.log(f"Conexcion aceptada desde: {adress}")

                thread_cliente = threading.Thread(target=self.escuchar_cliente, 
                args=(self.id_cliente, socket_cliente), 
                daemon=True)

                thread_cliente.start()
                self.sockets[self.id_cliente] = socket_cliente
                self.id_cliente += 1


            except ConnectionError as error:
                self.log(f"Fallo en la conexion. Error {error}")



        
    def escuchar_cliente(self, id_cliente, socket_cliente):
        """
        Ciclo encargado de escuchar a cada cliente de forma individual, esta
        funcion se ejecuta siempre que el servidor este conectado, recibe el
        socket del cliente y si hay un mensaje, lo procesa con la funcion
        instanciada en la logica.
        """
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        # TODO: Completado por estudiante
        try:
            mensaje = self.recibir_mensaje(socket_cliente)
            
            if not mensaje:
                raise ConnectionResetError
            
            respuesta = self.logica.procesar_mensaje(mensaje, socket_cliente)

            if respuesta:
                self.enviar_mensaje(respuesta, socket_cliente)
                self.notificar_otros_usuarios(id_cliente, respuesta)



        except ConnectionError as error:
            self.log(f"Fallo en la conexion. Error {error}")
            self.log(f"Cerrando conexion de cliente {id_cliente}")
            self.eliminar_cliente(self.id_cliente, socket_cliente)




    def notificar_otros_usuarios(self, id_cliente_nuevo, respuesta):
        if "usuarios" not in respuesta:
            # Solo me ejecuto si está la key "usuarios" en respuesta
            return

        for socket in self.sockets:
            if socket != id_cliente_nuevo:
                self.enviar_mensaje({
                    "comando": "respuesta_actualizar_usuarios",
                    "usuarios": respuesta["usuarios"]
                }, self.sockets[socket])

    def recibir_mensaje(self, socket_cliente):
        """
        Recibe un mensaje del cliente, lo DECODIFICA usando el protocolo
        establecido y lo des-serializa retornando un diccionario.
        """
        # TODO: Completado por estudiante
        largo_mensaje_bytes = socket_cliente.recv(4)
        # Decodificar largo del mensaje
        largo_mensaje = int.from_bytes(largo_mensaje_bytes, byteorder="little")
        # Recibir mensaje
        bytes_mensaje = bytearray()

        while len(bytes_mensaje) < largo_mensaje:
            tamano_chunk = min(largo_mensaje - len(bytes_mensaje), 64)
            bytes_mensaje += socket_cliente.recv(tamano_chunk)

        # Decodificar mensaje
        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje
        








    def enviar_mensaje(self, mensaje, socket_cliente) -> None:
        """
        Recibe una instruccion,
        lo CODIFICA usando el protocolo establecido y lo envía al cliente
        """
        # TODO: Completado por estudiante
        mensaje_codificado = self.codificar_mensaje(mensaje)
        largo_mensaje = len(mensaje_codificado).to_bytes(4, 'little')

        socket_cliente.sendall(largo_mensaje + mensaje_codificado)







    def enviar_archivo(self, socket_cliente, ruta):
        """
        Recibe una ruta a un archivo a enviar y los separa en chunks de 8 kb
        """
        with open(ruta, "rb") as archivo:
            chunk = archivo.read(8000)
            largo = len(chunk)
            while largo > 0:
                chunk = chunk.ljust(8000, b"\0")  # Padding
                msg = {
                    "comando": "chunk",
                    "argumentos": {"largo": largo, "contenido": chunk.hex()},
                    "ruta": ruta,
                }
                self.enviar_mensaje(msg, socket_cliente)
                chunk = archivo.read(8000)
                largo = len(chunk)

    def eliminar_cliente(self, id_cliente, socket_cliente):
        """
        Elimina un cliente del diccionario de clientes conectados
        """
        try:
            # Cerramos el socket
            self.log(f"Borrando socket del cliente {id_cliente}.")
            socket_cliente.close()
            self.sockets.pop(id_cliente, None)
            self.logica.eliminar_nombre(id_cliente)
            usuarios = ",".join(self.logica.usuarios.values())
            self.notificar_otros_usuarios(id_cliente, {"usuarios": usuarios})

        except KeyError as e:
            self.log(f"ERROR: {e}")

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            return mensaje_bytes
        except json.JSONDecodeError:
            self.log("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        # TODO: Completado por estudiante

        try:
            mensaje_decodificado = json.loads(mensaje_bytes)
            return mensaje_decodificado

        except json.JSONDecodeError:
            self.log("No se pudo decodificar el mensaje")
            return dict()






    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")
