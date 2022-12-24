
from parametros import AUMENTAR_VIDA_PLANTA, AUMENTAR_ATAQUE_FUEGO, AUMENTAR_VELOCIDAD_AGUA


def dict_entrenadores():
    entrenadores = open("entrenadores.csv", "r", encoding="utf-8").readlines()
    entrenadores_dict = {}
    for i in range(1, len(entrenadores)):
        entrenadores_dict[str(i)] = entrenadores[i].split(',')[0]
    return entrenadores_dict

def print_entrenadores():
    entrenadores = open("entrenadores.csv", "r", encoding="utf-8").readlines()
    for i in range(1, len(entrenadores)):
        print(f"[{i}] {entrenadores[i].split(',')[0]}")


def len_csv_file(filename):
    file = open(filename, "r", encoding="utf-8").readlines()
    return len(file)

def print_objetos(entrenador):
    objetos = ""
    for i in range(0, len(entrenador.objetos) - 1):
        objetos += f"{entrenador.objetos[i].nombre}, "
    objetos += entrenador.objetos[len(entrenador.objetos) - 1].nombre
    return objetos

def beneficio_victoria(programon):
    if programon.tipo == "planta":
        programon.vida += AUMENTAR_VIDA_PLANTA
        print(f"La vida del programon {programon.nombre} a aumentado en {AUMENTAR_VIDA_PLANTA}")
    elif programon.tipo == "agua":
        programon.velocidad += AUMENTAR_VELOCIDAD_AGUA
        print(f"La velocidad del programon {programon.nombre} a aumentado en \
{AUMENTAR_VELOCIDAD_AGUA}")
    else:
        programon.ataque += AUMENTAR_ATAQUE_FUEGO
        print(f"El ataque del programon {programon.nombre} a aumentado en {AUMENTAR_ATAQUE_FUEGO}")

        





