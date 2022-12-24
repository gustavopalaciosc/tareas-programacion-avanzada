"""
En este archivo se completan las funciones que son utilizadas para
la creación de la lista de reproducción
"""
from functools import reduce

from usuario import Usuario


def filtrar_prohibidos(iterar_canciones, artista_prohibido):
    """
    Debe filtrar todas canciones que contengan temas prohibidos
    :param artista_prohibido: artista prohibido del usuario
    :param iterar_canciones: iterador sobre lista de canciones
    :return: filter
    """
    # Debes completar esta función
    filtro_prohibidos = filter(lambda x: artista_prohibido not in x.artistas, iterar_canciones)
    return filtro_prohibidos


def calcular_afinidades(catalogo_canciones, usuario: Usuario):
    """
    La función debe calcular las afinidades según preferencias del usuario.
    El map retorna tuplas, donde el primer valor es la canción,
    y el segundo valor la afinidad.
    :param usuario: Usuario para quien se crearán las afinidades
    :param catalogo_canciones: zip que retorna canciones
    :return: mapeo que retorna tuplas.
    """
    # Debes completar esta función
    afinidad = map(lambda x: (x.nombre, usuario.calcular_afinidad(x)), catalogo_canciones)
    return afinidad
    
    
    


def encontrar_canciones_comunes(usuarios_mix_party):
    """
    La función debe encontrar las canciones comunes entre las favoritas
    de cada usuario, y retornar un set que las contenga.
    :param usuarios_mix_party: lista de usuarios que conforman la mix party
    :return: interseccion de las peliculas favoritas de cada usuario
    """
    # Debes completar esta función
    lista_canciones_fav = [x.canciones_favoritas for x in usuarios_mix_party]
    lista_de_listas = map(lambda x: x.canciones_favoritas, usuarios_mix_party)
    interseccion = reduce(lambda x, y: x & y, lista_de_listas )
    return interseccion


def encontrar_usuario_mas_afin(usuario, otros_usuarios):
    """
    Esta función debe encontrar el usuario con mayor compatibilidad.
    Debe primero filtrar usuarios que no tengan el mismo artista_prohibido,
    y luego encontrar aquél con quien tenga mayor compatibilidad
    :param usuario: usuario para quien se encontrará un amigue
    :param otros_usuarios: el resto de los usuarios de DCCanciones
    :return: Usuario más compatible
    """
    # Debes completar esta función

    filtro_prohibido = filter(lambda x: x.artista_prohibido == usuario.artista_prohibido, otros_usuarios)
    afinidad = reduce(lambda x, y: x if x + usuario > y + usuario else y, filtro_prohibido)

    return afinidad

    



if __name__ == "__main__":

    usuario = Usuario("gus",1,"standly")
    otros_usuarios = [Usuario("roberto", 2, "standly"),
     Usuario("Calvo", 1, "standly"),
     Usuario("Eugenio", 12, "chayanne")]
    
    encontrar_usuario_mas_afin(usuario, otros_usuarios)



    
