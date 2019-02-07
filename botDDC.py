import requests
import threading
from re import search
from time import sleep

def vote():
    h = {
        'Host': 'df.diariodecuyo.com.ar',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.diariodecuyo.com.ar/especiales/fiesta-nacional-del-sol-2019/votacion-reina.html',
        'Origin': 'https://www.diariodecuyo.com.ar',
        'DNT': '1',
        'Connection': 'close',
    }

    url = 'https://df.diariodecuyo.com.ar/frontally/deportista2016/fnds/FNDS.php?departamentoSel=Ana+Paula+Vilanova+de+Valle+F%C3%A9rtil'
    res = requests.get(url,headers=h)
    try:
        resultados = search('Gracias por votar',res.text).group()
    except Exception as e:
        print('[-] DDC: ',e)
        return res.status_code,e 
    return res.status_code,resultados

class Th(threading.Thread):
    def __init__(self,Id,printRes,cant):
        threading.Thread.__init__(self)
        self.Id = Id
        self.printRes = printRes
        self.cant = cant
    
    def printResultados(self,resultados):
        print('DDC: ',resultados)

    def run(self):
        ts.append(self)
        code,resultados = vote()
        if code != 200:
            sleep(5)
            code,resultados = vote()
        if resultados and self.printRes and self.Id%self.cant == 0: self.printResultados(resultados)
            
def main(printStatus,printRes,cant=10):
    global ts
    ts = []
    for Id in range(1,cant+1):
        thread = Th(Id,printRes,cant)
        thread.start()
        sleep(5)
    if printStatus:print('DDC OK... +%d'%cant)

if __name__ == "__main__":
    main(True,True,cant=2)