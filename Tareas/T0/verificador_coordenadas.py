def verificar_cordenadas(coordenadas, largo, ancho):
    letras = "ABCDEFGHIJKLMNO"[0:largo]

    if coordenadas[0].capitalize() in letras and coordenadas[1:].isdigit():
        if 0 <= int(coordenadas[1:]) < ancho:
            return True
        
        else:
            return False
    
    else:
        return False
