import os
def eliminar_partida(usuario):
    os.remove(f"partidas/{usuario}.txt")

