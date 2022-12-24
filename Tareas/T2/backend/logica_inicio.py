from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaInicio(QObject):
    senal_respuesta_validacion = pyqtSignal(bool)
    senal_abrir_juego = pyqtSignal()
    senal_enviar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def confirmar_usuario(self, usuario):
        valid = True
        if usuario.isalnum() and ' ' not in usuario:
            if p.MIN_CARACTERES <= len(usuario) <= p.MAX_CARACTERES:
                pass 
        else:
            valid = False
        
        self.senal_respuesta_validacion.emit(valid)

        if valid:
            self.senal_enviar_usuario.emit(usuario)
            self.senal_abrir_juego.emit()
            
            


