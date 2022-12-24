from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from os import path
import parametros as p


class Sol(QLabel):

    def __init__(self, parent, pos_inicial):
        super().__init__(parent)

        self.setGeometry(pos_inicial[0], pos_inicial[1], 50, 50)
        ruta_imagen = path.join(p.PATH_ELEMENTOS_JUEGO, "sol.png")
        self.pixmap_neutro = QPixmap(ruta_imagen)
        self.setPixmap(self.pixmap_neutro)
        self.setScaledContents(True)
        self.show()
    

    
    
