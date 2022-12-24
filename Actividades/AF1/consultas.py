# --- EJEMPLO --- #
# [Plato1, Plato2, Plato2, Plato4]
# pasa a ser
# {"Categoria1": [Plato3, Plato2], "Categoria2": [Plato1, Plato4]}
def platos_por_categoria(lista_platos: list) -> dict:
    categories = {'Hamburguesa': [], 'Completos': [], 'Tallarines': [], 'Pescado': [], 'Pizza': []}

    for i in lista_platos:
        categories[i[1]].append(i)
    
    return categories


# Debe devolver los platos que no tengan ninguno de los ingredientes descartados
def descartar_platos(ingredientes_descartados: set, lista_platos: list) -> list:
    platos = []

    for plato in lista_platos:
        for i in ingredientes_descartados:
            if i not in plato[4]:
                platos.append(plato)
                break
    
    return platos



# --- EXPLICACION --- #
# Si el plato necesita un ingrediente que no tiene cantidad suficiente,
# entonces retorna False
#
# En caso que tenga todo lo necesario, resta uno a cada cantidad y retorna True
# NO MODIFICAR
def preparar_plato(plato, ingredientes: dict) -> bool:
    for ingrediente_plato in plato.ingredientes:
        if ingredientes[ingrediente_plato] <= 0:
            return False

    for ingrediente_plato in plato.ingredientes:
        ingredientes[ingrediente_plato] -= 1

    return True


# --- EXPLICACION --- #
# Debe retornar un diccionario que agregue toda la información ...
#  de la lista de platos.
# precio total, tiempo total, cantidad de platos, platos
def resumen_orden(lista_platos: list) -> dict:
    
    orden = {'precio total': 0, 'tiempo total': 0, 'cantidad de platos': 0, 'platos': []}

    for plato in lista_platos:
        orden['precio total'] += plato.precio
        orden['tiempo total'] += plato.tiempo
        orden['cantidad de platos'] += 1
        orden['platos'].append(plato.nombre)

    return orden
        
        

