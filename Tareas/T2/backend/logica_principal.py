from PyQt5.QtCore import QObject, pyqtSignal

class LogicaPrincipal(QObject):
    senal_enviar_validacion = pyqtSignal(bool, set)
    senal_enviar_datos = pyqtSignal(set)

    def __init__(self):
        super().__init__()
    

    def check_cancha(self, dia, noche):
        valid = True
        choice = []
        if dia and noche:
            valid = False

        elif not dia and not noche:
            valid = False
        
        else:
            if dia:
                choice.append("dia")
            elif noche:
                choice.append("noche")
        
        self.senal_enviar_validacion.emit(valid, set(choice))
        self.senal_enviar_datos.emit(set(choice))
        
