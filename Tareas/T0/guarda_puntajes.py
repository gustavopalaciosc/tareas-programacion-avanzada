
def guarda_puntajes(usuario, puntaje):
    """
    Funcion para guardar puntaje de partida nueva
    """
    puntajes = open("puntajes.txt", "r", encoding="utf-8")
    puntos = puntajes.readlines()
    for i in range(0, len(puntos)):
        if puntos[i].split(",")[0] == usuario:
            del puntos[i]
            break
    puntos.append(f"{usuario},{puntaje}\n")
    puntajes.close()
    puntajes = open("puntajes.txt", "w", encoding="utf-8")
    for puntaje in puntos:
        puntajes.write(puntaje)
    puntajes.close()


def sobreescribir_puntaje(usuario, puntaje):
    """
    Funcion para guardar puntaje de partida cargada
    """
    puntajes = open("puntajes.txt", "r", encoding="utf-8")
    puntos = puntajes.readlines()
    for i in range(0, len(puntos)):
        if puntos[i].split(",")[0] == usuario:
            puntos[i] = f"{usuario},{puntaje}\n"
            break
    puntajes.close()
    puntajes = open("puntajes.txt", "w", encoding="utf-8")
    for puntaje in puntos:
        puntajes.write(puntaje)
    puntajes.close()


def eliminar_puntaje(usuario):
    """
    Funcion para eliminar un puntaje
    """
    puntajes = open("puntajes.txt", "r", encoding="utf-8")
    puntos = puntajes.readlines()
    for i in range(0, len(puntos)):
        if puntos[i].split(",")[0] == usuario:
            del puntos[i]
            break
    puntajes.close()
    puntajes = open("puntajes.txt", "w", encoding="utf-8")
    for puntaje in puntos:
        puntajes.write(puntaje)
    puntajes.close()

