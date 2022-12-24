from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from os import path
import parametros as p

class Guisante(QLabel):

    def __init__(self, parent):
        super().__init__(parent)
        
        self.setScaledContents(True)
        self.show()
        self.timer_move()
    
    def timer_move(self):
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.mover)
        self.timer.start()
    
    def mover(self):
        self.move(self.x() + 5, self.y())
    
    def esconder(self):
        self.hide()


class GuisanteClasico(Guisante):
    def __init__(self, parent, x_axis, y_axis):
        super().__init__(parent)
        self.setGeometry(x_axis + 50, y_axis, 50, 50)
        ruta_imagen = path.join(p.PATH_ELEMENTOS_JUEGO, "guisante_1.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)


class GuisanteHielo(Guisante):
    def __init__(self, parent,  x_axis, y_axis):
        super().__init__(parent)
        self.setGeometry(x_axis + 50, y_axis, 50, 50)
        ruta_imagen = path.join(p.PATH_ELEMENTOS_JUEGO, "guisanteHielo_1.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)



