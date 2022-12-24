import sys
from PyQt5.QtWidgets import QApplication

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_post_juego import VentanaPostJuego
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_juego import VentanaJuego

from backend.logica_inicio import LogicaInicio
from backend.logica_principal import LogicaPrincipal
from backend.logica_juego import LogicaJuego
from backend.logica_ranking import LogicaRanking



if __name__ == "__main__":
    app = QApplication([])

    #Frontend
    ventana_inicio = VentanaInicio()
    ventana_ranking = VentanaRanking()
    ventana_principal = VentanaPrincipal()
    ventana_juego = VentanaJuego()
    ventana_post_juego = VentanaPostJuego()
    

    #Backend
    logica_inicio = LogicaInicio()
    logica_principal = LogicaPrincipal()
    logica_juego = LogicaJuego()
    logica_ranking = LogicaRanking()
    



    #Señales Inicio
    ventana_inicio.senal_enviar_usuario.connect(logica_inicio.confirmar_usuario)
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.comprobar_usuario)
    ventana_inicio.senal_ver_ranking.connect(ventana_ranking.mostrar_ventana)
    ventana_ranking.senal_volver.connect(ventana_inicio.mostrar_ventana)
    logica_inicio.senal_abrir_juego.connect(ventana_principal.mostrar_ventana)
    ventana_inicio.senal_enviar_usuario.connect(ventana_post_juego.set_usuario)

    #Señales ranking
    ventana_ranking.senal_calcular_ranking.connect(logica_ranking.calcular_ranking)
    logica_ranking.senal_enviar_ranking.connect(ventana_ranking.set_ranking)


    #Señales principal
    ventana_principal.senal_elegir_cancha.connect(logica_principal.check_cancha)
    logica_principal.senal_enviar_validacion.connect(ventana_principal.recibir_validacion)
    ventana_principal.senal_empezar_juego.connect(ventana_juego.setear_escenario)
    logica_principal.senal_enviar_datos.connect(logica_juego.set_datos_inicio)
    ventana_juego.senal_iniciar_juego.connect(logica_juego.iniciar_juego)
    ventana_juego.senal_setear_planta.connect(logica_juego.set_planta)
    logica_juego.senal_cargar_datos.connect(ventana_juego.setear_datos)

    ventana_juego.senal_comer_arriba.connect(logica_juego.ataque_arriba)
    ventana_juego.senal_comer_abajo.connect(logica_juego.ataque_abajo)
    logica_juego.senal_generar_sol_ventana.connect(ventana_juego.generar_sol)
    ventana_juego.senal_generar_sol.connect(logica_juego.generar_soles)
    ventana_juego.senal_verificar_click_sol.connect(logica_juego.verificar_click_sol)
    ventana_juego.senal_enviar_sol_girasol.connect(logica_juego.guardar_soles_girasol)

    ventana_juego.senal_pausar_juego.connect(logica_juego.pausar)
    ventana_juego.senal_reanudar_juego.connect(logica_juego.reanudar)
    ventana_juego.senal_cheatcode_sol.connect(logica_juego.cheatcode_sol)
    ventana_juego.senal_cheatcode_kil.connect(logica_juego.terminar_ronda)
    ventana_juego.senal_avanzar.connect(logica_juego.terminar_ronda)
    ventana_juego.senal_guardar_puntaje.connect(ventana_post_juego.guardar_puntaje)


    #Señales post-ronda
    logica_juego.senal_termino_ronda.connect(ventana_post_juego.mostrar_ventana)
    logica_juego.senal_termino_ronda_ventana.connect(ventana_juego.termino_ronda)
    ventana_post_juego.senal_nueva_ronda.connect(ventana_juego.empezar_nueva_ronda)











    ventana_inicio.show()
    sys.exit(app.exec_())