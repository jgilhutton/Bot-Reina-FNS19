import requests
import threading
from re import findall,search
from time import sleep

def vote():
    h = {
        'Host': 'www.diariomovil.info',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.diariomovil.info/encuesta/votacion-reina-nacional-del-sol-2019/',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'close',
    }
    d = "totalpoll%5Bid%5D=225601&totalpoll%5Bpage%5D=1&totalpoll%5Bview%5D=vote&totalpoll%5Bchoices%5D%5B%5D=16&totalpoll%5Baction%5D=vote&action=tp_action"
    url = 'https://www.diariomovil.info/wp-admin/admin-ajax.php'
    try:
        res = requests.post(url,headers=h,data=d)
    except Exception as e:
        print('[-] DM %s'%e, 'Esperando 5 segundos...')
        sleep(5)
        res = requests.post(url,headers=h,data=d)
    try:
        resultados = search('¡¡Muchas gracias por votar!!',res.text).group()
    except Exception as e:
        print('[-] DM %s'%e)
        return res.status_code,e 
    return res.status_code,resultados

class Th(threading.Thread):
    def __init__(self,Id,printRes,cant):
        threading.Thread.__init__(self)
        self.Id = Id
        self.printRes = printRes
        self.cant = cant
        
    def printResultados(self,resultados):
        print('DMovil: ',resultados)
    
    def run(self):
        ts.append(self)
        code,resultados = vote()
        if code != 200:
            sleep(5)
            code,resultados = vote()
        if self.printRes and self.Id%self.cant == 0: self.printResultados(resultados)

def main(printStatus,printRes,cant=10):
    global ts
    ts = []
    for Id in range(1,cant+1):
        thread = Th(Id,printRes,cant)
        thread.start()
        sleep(1)
    if printStatus:print('DMovil OK... +%d'%cant)

if __name__ == "__main__":
    main(True,True,cant=2)