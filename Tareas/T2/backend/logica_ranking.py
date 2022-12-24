from PyQt5.QtCore import QObject, pyqtSignal

class LogicaRanking(QObject):
    senal_enviar_ranking = pyqtSignal(dict)
    def __init__(self):
        super().__init__()

    
    def calcular_ranking(self):
        ans = {}
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
        for i in range(0, min(5, len(valores))):
            for name in orden:
                if orden[name] == valores[i]:
                    ans[name] = valores[i]
            count += 1
        
        self.senal_enviar_ranking.emit(ans)
        
        
        
        
        
        
        
        

        
        

    
    