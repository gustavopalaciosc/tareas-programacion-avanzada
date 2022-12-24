from objetos import Baya, Pocion, Caramelo

def lista_objetos():
    objetos = []
    archivo_objetos = open("objetos.csv", "r", encoding="utf-8").readlines()
    for i in range(1, len(archivo_objetos)):
        objeto = archivo_objetos[i].split(",")
        objeto[1] = objeto[1].strip()
        if objeto[1] == "caramelo":
            objetos.append(Caramelo(objeto[0], objeto[1]))
        elif objeto[1] == "pocion":
            objetos.append(Pocion(objeto[0], objeto[1]))
        else:
            objetos.append(Baya(objeto[0], objeto[1]))
    return objetos

def lista_bayas():
    objetos = lista_objetos()
    bayas = []
    for objeto in objetos:
        if objeto.tipo == "baya":
            bayas.append(objeto)
    return bayas


def lista_pociones():
    objetos = lista_objetos()
    pociones = []
    for objeto in objetos:
        if objeto.tipo == "pocion":
            pociones.append(objeto)
    return pociones

def lista_caramelos():
    objetos = lista_objetos()
    caramelos = []
    for objeto in objetos:
        if objeto.tipo == "caramelo":
            caramelos.append(objeto)
    return caramelos



