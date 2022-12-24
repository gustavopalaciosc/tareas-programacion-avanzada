def cont_enemigos(tablero):
    ancho = len(tablero)
    largo = len(tablero[0])
    for fila in range(0, ancho):
        for elemento in range(0, largo):
            count = 0
            if tablero[fila][elemento] != 'N':
                if fila-1 >= 0:
                    if elemento - 1 >= 0:
                        if tablero[fila - 1][elemento - 1] == 'N':
                            count += 1                      
                    if elemento + 1 < largo:
                        if tablero[fila - 1][elemento + 1] == 'N':
                            count += 1
                    if tablero[fila - 1][elemento] == 'N':
                        count += 1
                if fila + 1 < ancho:
                    if elemento - 1 >= 0:
                        if tablero[fila + 1][elemento - 1] == 'N':
                            count += 1                   
                    if elemento + 1 < largo:
                        if tablero[fila + 1][elemento + 1] == 'N':
                            count += 1
                    if tablero[fila + 1][elemento] == 'N':
                        count += 1                
                if elemento + 1 < largo:
                    if tablero[fila][elemento + 1] == 'N':
                        count += 1                
                if elemento - 1 >= 0:
                    if tablero[fila][elemento - 1] == 'N':
                        count += 1  
                                       
                tablero[fila][elemento] = str(count)
    return tablero








                
                


        
