from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # COMPLETAR
        self.logo = QLabel(self)
        self.logo.setGeometry(50, 50, 350, 250)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        username_label = QLabel('Ingresa tu nombre de usuario:', self)
        username_label.move(30, 300)
        self.input_usuario = QLineEdit('', self)
        self.input_usuario.move(260, 300)

        password_label = QLabel('Ingresa tu contraseña:', self)
        password_label.move(30, 350)
        self.input_password = QLineEdit('', self)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.move(260, 350)

        self.boton_inicio = QPushButton('Empezar juego!',self)
        self.boton_inicio.move(180, 400)

        layout_principal = QVBoxLayout()
        layout_imagen = QHBoxLayout()
        layout_formulario = QVBoxLayout()
        layout_boton = QHBoxLayout()

        layout_formulario.addWidget(username_label)
        layout_formulario.addWidget(self.input_usuario)
        layout_formulario.addWidget(password_label)
        layout_formulario.addWidget(self.input_password)
        layout_imagen.addWidget(self.logo)
        layout_boton.addWidget(self.boton_inicio)
        layout_principal.addLayout(layout_imagen)
        layout_principal.addLayout(layout_formulario)
        layout_principal.addLayout(layout_boton)

        self.setLayout(layout_principal)



        self.boton_inicio.clicked.connect(self.enviar_login)


    def enviar_login(self):
        # COMPLETAR
        self.senal_enviar_login.emit(self.input_usuario.text(), self.input_password.text())

    def recibir_validacion(self, valid, errores):
        # COMPLETAR
        if valid:
            self.hide()
        else:
            if "usuario" in errores:
                self.input_usuario.setText("")
                self.input_usuario.setPlaceholderText("Usuario invalido")
            if "contraseña" in errores:
                self.input_password.setText("")
                self.input_password.setPlaceholderText("Contraseña invalida")
            