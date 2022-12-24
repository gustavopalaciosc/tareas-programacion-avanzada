from backend.cliente import Cliente
from backend.logica_cliente import LogicaCliente
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_espera import VentanaEspera
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_final import VentanaFinal
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":


    app = QApplication(sys.argv)
    
    #frontend
    ventana_inicio = VentanaInicio()
    ventana_espera = VentanaEspera()
    ventana_juego = VentanaJuego()
    ventana_final = VentanaFinal()


    #backend
    cliente = Cliente()
    logica_cliente = LogicaCliente()





    cliente.senal_mostrar_ventana_inicio.connect(
        logica_cliente.mostrar_ventana_inicio)

    logica_cliente.senal_mostar_ventana_inicio.connect(
        ventana_inicio.mostrar_ventana)

    ventana_inicio.senal_enviar_nombre.connect(
        logica_cliente.recibir_nombre)

    logica_cliente.senal_enviar_comando.connect(
        cliente.enviar_comando)

    cliente.senal_procesar_comando.connect(
        logica_cliente.procesar_comando)

    logica_cliente.senal_cerrar_ventana_inicio.connect(
        ventana_inicio.cerrar_ventana)
    
    logica_cliente.senal_set_nombre_ventana_espera.connect(
        ventana_espera.set_jugador
    )

    logica_cliente.senal_abrir_ventana_espera.connect(
        ventana_espera.mostrar_ventana)

    logica_cliente.senal_abrir_ventana_juego.connect(
        ventana_juego.mostrar_ventana
    )

    logica_cliente.senal_cerrar_ventana_espera.connect(
        ventana_espera.cerrar_ventana
    )

    logica_cliente.senal_nombre_rechazado.connect(
        ventana_inicio.set_nombre_invalido
    )

    logica_cliente.senal_actualizar_tiempo.connect(
        ventana_espera.actualizar_tiempo_espera
    )

    logica_cliente.senal_set_cartas.connect(
        ventana_juego.set_cartas
    )

    ventana_juego.senal_seleccionar_carta.connect(
        cliente.enviar_comando
    )

    logica_cliente.senal_set_carta_oponente.connect(
        ventana_juego.set_carta_oponente
    )
    
    logica_cliente.senal_set_mazo_ganador.connect(
        ventana_juego.set_mazo_ganador
    )

    logica_cliente.senal_esconder_cartas.connect(
        ventana_juego.esconder_cartas
    )

    logica_cliente.senal_terminar_partida.connect(
        ventana_juego.termino_partida
    )

    logica_cliente.senal_set_ganador.connect(
        ventana_juego.set_ganador
    )

    ventana_juego.senal_mostrar_ventana_final.connect(
        ventana_final.mostrar_ventana
    )

    ventana_final.senal_abrir_ventana_inicio.connect(
        ventana_inicio.mostrar_ventana
    )

    

    cliente.start_client()

    sys.exit(app.exec_())
