from lista_programones import lista_programones
from lista_objetos import lista_objetos
from entrenador import Entrenador

def lista_entrenadores():
    entrenadores = []
    programones = lista_programones()
    objetos = lista_objetos()
    archivo_entrenadores = open("entrenadores.csv", "r", encoding="utf-8").readlines()
    for i in range(1, len(archivo_entrenadores)):
        datos_entrenador = archivo_entrenadores[i].split(",")
        entrenador = Entrenador(datos_entrenador[0], int(datos_entrenador[2]))

        for programon in programones:
            if programon.nombre in datos_entrenador[1].split(";"):
                entrenador.programones.append(programon)

        for objeto in objetos:
            for objeto_entrenador in datos_entrenador[3].split(";"):
                if objeto_entrenador.strip() == objeto.nombre:
                    entrenador.objetos.append(objeto)

        entrenadores.append(entrenador)

    return entrenadores


        



