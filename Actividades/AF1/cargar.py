# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
from collections import namedtuple


def cargar_platos(ruta_archivo: str) -> list:
    Plato = namedtuple("Platos", ['nombre', 'categoria', 'tiempo', 'precio', 'ingredientes'])
    mis_platos = open(ruta_archivo, encoding="utf-8").readlines()
    ans = []
    
    for p in mis_platos:
        mip = p.split(",")
        mip[2] = int(mip[2])
        mip[3] = int(mip[3])
        mip[4] = mip[4].split(";")
        mip[4][-1] = mip[4][-1].strip()
        mip[4] = set(mip[4])
        ans.append(Plato(mip[0], mip[1], mip[2], mip[3], mip[4]))
    
    return ans
        




    


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    ingredientes = open(ruta_archivo, encoding="utf-8").readlines()
    dict_ing = {}

    for i in ingredientes:
        dato = i.split(",")
        dict_ing[dato[0]] = int(dato[1])
    
    return dict_ing

    

