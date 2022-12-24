from programon import Agua, Fuego, Planta

def lista_programones():
    programones = []
    archivo_programones = open("programones.csv", "r", encoding="utf-8").readlines()
    for i in range(1, len(archivo_programones)):
        programon = archivo_programones[i].split(",")
        if programon[1] == "fuego":
            programones.append(Fuego(nombre = programon[0], nivel = programon[2], tipo = programon[1], vida = programon[3], ataque = programon[4], defensa=programon[5], velocidad=programon[6]))
        elif programon[1] == "agua":
            programones.append(Agua(nombre = programon[0], nivel = programon[2], tipo = programon[1], vida = programon[3], ataque = programon[4], defensa=programon[5], velocidad=programon[6]))
        else:
            programones.append(Planta(nombre = programon[0], nivel = programon[2], tipo = programon[1], vida = programon[3], ataque = programon[4], defensa=programon[5], velocidad=programon[6]))
    return programones


