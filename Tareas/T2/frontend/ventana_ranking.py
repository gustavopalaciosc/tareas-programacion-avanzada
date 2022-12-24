from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import os
import sys

window_name, base_class = uic.loadUiType(os.path.join('frontend',\
     'assets', 'uifiles', 'ui-ventana-ranking.ui'))

class VentanaRanking(window_name, base_class):
    senal_volver = pyqtSignal()
    senal_calcular_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        


    def init_gui(self):
        self.boton_volver.clicked.connect(self.volver)
        
    
    def set_ranking(self, rank):
        nombres = list(rank.keys())
        largo = len(nombres)
        if largo > 0:
            self.nombre_uno.setText(nombres[0])
            self.puntaje_uno.setText(str(rank[nombres[0]]))
            if largo > 1:
                self.nombre_dos.setText(nombres[1])
                self.puntaje_dos.setText(str(rank[nombres[1]]))
                if largo > 2:
                    self.nombre_tres.setText(nombres[2])
                    self.puntaje_tres.setText(str(rank[nombres[2]]))
                    if largo > 3:
                        self.nombre_cuatro.setText(nombres[3])
                        self.puntaje_cuatro.setText(str(rank[nombres[3]]))
                        if largo > 4:
                            self.nombre_cinco.setText(nombres[4])
                            self.puntaje_cinco.setText(str(rank[nombres[4]]))

    
    def mostrar_ventana(self):
        self.senal_calcular_ranking.emit()
        self.show()
    
    def volver(self):
        self.senal_volver.emit()
        self.nombre_uno.setText("")
        self.puntaje_uno.setText("")
        self.nombre_dos.setText("")
        self.puntaje_dos.setText("")
        self.nombre_tres.setText("")
        self.puntaje_tres.setText("")
        self.nombre_cuatro.setText("")
        self.puntaje_cuatro.setText("")
        self.nombre_cinco.setText("")
        self.puntaje_cinco.setText("")

        self.hide()






if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaRanking()
    ventana.show()
    sys.exit(app.exec_())