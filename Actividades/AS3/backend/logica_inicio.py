from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, set)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario, contrasena):
        # COMPLETAR
        errores = []
        valid = True
        if usuario.isalnum():
            pass
        else:
            valid = False
            errores.append('usuario')
        
        if contrasena in p.CONTRASENAS_PROHIBIDAS:
            valid = False
            errores.append('contraseña')

        errores = set(errores)
        self.senal_respuesta_validacion.emit(valid, errores)

        if valid:
            self.senal_abrir_juego.emit(usuario)