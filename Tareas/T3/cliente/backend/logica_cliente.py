from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from funciones import read_json


class LogicaCliente(QObject):
    senal_enviar_comando = pyqtSignal(dict)
    senal_mostar_ventana_inicio = pyqtSignal()
    senal_cerrar_ventana_inicio = pyqtSignal()
    senal_abrir_ventana_espera = pyqtSignal()
    senal_set_nombre_ventana_espera = pyqtSignal(str, bool)
    senal_nombre_rechazado = pyqtSignal()
    senal_cerrar_ventana_espera = pyqtSignal()
    senal_abrir_ventana_juego = pyqtSignal(str, str)
    senal_actualizar_tiempo = pyqtSignal(int)
    senal_set_cartas = pyqtSignal(dict)
    senal_set_carta_oponente = pyqtSignal(dict)
    senal_set_mazo_ganador = pyqtSignal(bool, dict)
    senal_esconder_cartas = pyqtSignal()
    senal_terminar_partida = pyqtSignal(str)
    senal_set_ganador = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.nombre_usuario = None
        self.id = None
        self.nombre_contrincante = None
        self.timer_espera = QTimer()
        self.timer_espera.setInterval(1000)
        self.timer_espera.timeout.connect(self.actualizar_tiempo_espera)
        self.timer_reinicio_cartas = QTimer()
        self.timer_reinicio_cartas.setInterval(read_json("TIEMPO_REINICIO_CARTAS"))
        self.timer_reinicio_cartas.setSingleShot(True)
        self.timer_reinicio_cartas.timeout.connect(self.esconder_cartas_jugadores)
        self.timer_terminar_partida = QTimer()
        self.timer_terminar_partida.setInterval(read_json("TIEMPO_TERMINAR_PARTIDA"))
        self.timer_terminar_partida.setSingleShot(True)
        self.timer_terminar_partida.timeout.connect(self.terminar_partida)
        self.tiempo_espera = read_json("CUENTA_REGRESIVA_INICIO")
        
    def mostrar_ventana_inicio(self):
        self.senal_mostar_ventana_inicio.emit()
    
    def recibir_nombre(self, nombre):
        """
        Recibe el nombre de usuario ingresado en la ventana inicial.
        Luego la envia como comando al servidor para ser verificado
        """
        mensaje = {"comando": "set_name", "name": nombre}
        self.senal_enviar_comando.emit(mensaje)
    
    def procesar_comando(self, comando):
        #Procesamiento de nombre
        if comando['comando'] == 'set_name':
            self.procesar_nombre(comando)
        
        elif comando['comando'] == 'actualizar_datos_espera':
            nombres = comando['nombres']
            for name in nombres:
                if name != self.nombre_usuario:
                    self.senal_set_nombre_ventana_espera.emit(name, False)
                    self.nombre_contrincante = name
                
                    if self.nombre_usuario != None:
                        self.timer_espera.start()
        
        elif comando['comando'] == 'usuario_desconectado':
            self.timer_espera.stop()
            self.tiempo_espera = read_json("CUENTA_REGRESIVA_INICIO")
        
        elif comando['comando'] == 'set_inicial_cartas':
            self.senal_set_cartas.emit(comando['cartas'])
        

        elif comando['comando'] == 'termino_ronda':
            if comando['ganador'] == self.nombre_usuario:
                self.senal_set_cartas.emit(comando['mazo_ganador'])
                self.senal_set_carta_oponente.emit(comando['carta_perdedora'])
                self.senal_set_mazo_ganador.emit(True, comando['carta_ganadora'])
                if comando['victoria']:
                    self.senal_set_ganador.emit()
            else:
                self.senal_set_cartas.emit(comando['mazo_perdedor'])
                self.senal_set_carta_oponente.emit(comando['carta_ganadora'])
                self.senal_set_mazo_ganador.emit(False, comando['carta_ganadora'])
            
            if comando['victoria']:
                self.timer_terminar_partida.start()
            else:
                self.timer_reinicio_cartas.start()
            
        else:
            pass
    
    def procesar_nombre(self, comando):
        if comando['estado'] == 'aceptado':
                self.nombre_usuario = comando['nombre']
                self.id = comando['id_cliente']
                self.senal_cerrar_ventana_inicio.emit()
                self.senal_set_nombre_ventana_espera.emit(self.nombre_usuario, True)
                self.senal_abrir_ventana_espera.emit()

                if len(comando['otros_nombres']) > 1:
                    for nombre in comando['otros_nombres']:
                        if nombre != self.nombre_usuario:
                            self.nombre_contrincante = nombre
                            self.senal_set_nombre_ventana_espera.emit(
                                self.nombre_contrincante, False)
                    self.timer_espera.start()
                    
        elif comando['estado'] == 'rechazado':
            self.senal_nombre_rechazado.emit()
    
    def actualizar_tiempo_espera(self):
        if self.tiempo_espera == 0:
            self.senal_actualizar_tiempo.emit(self.tiempo_espera)
            self.timer_espera.stop()
            self.senal_cerrar_ventana_espera.emit()
            self.senal_abrir_ventana_juego.emit(self.nombre_usuario, self.nombre_contrincante)
            self.senal_enviar_comando.emit({'comando': 'comenzar_juego'})
        
        else:
            self.senal_actualizar_tiempo.emit(self.tiempo_espera)
            self.tiempo_espera -= 1
    
    def esconder_cartas_jugadores(self):
        self.senal_esconder_cartas.emit()
    
    def terminar_partida(self):
        self.senal_terminar_partida.emit(self.nombre_usuario)


        
    

    



    

    

        

    



    
