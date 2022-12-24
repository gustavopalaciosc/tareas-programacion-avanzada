import json
from os.path import join


def read_json(llave):
    ruta = join("parametros.json")
    with open(ruta, "r", encoding="UTF-8") as file:
        data = json.load(file)
    valor = data[llave]
    return valor