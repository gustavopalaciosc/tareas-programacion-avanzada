def ranking_puntajes():
    orden = {}
    count = 1
    puntajes = open("puntajes.txt", "r", encoding="utf-8")
    rank = puntajes.readlines()
    puntajes.close()    
    for i in rank:
        orden[i.split(",")[0].strip()] = int(i.split(",")[1])
    valores = list(orden.values())
    valores.sort()
    valores.reverse()   
    for i in range(0, min(10, len(valores))):
        for name in orden:
            if orden[name] == valores[i]:
                print(f"#{count}: {name} ({valores[i]} puntos)")
                del orden[name]
                break
        count += 1
        

    
       

    

print(ranking_puntajes())
