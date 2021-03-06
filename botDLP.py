import requests
import threading
from re import findall,search
from time import sleep

def vote():
    h = {
        'Host': 'www.opinionstage.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.opinionstage.com/polls/2537564/poll',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-CSRF-Token': '9QtMEBIc6mi1anuqvSEMgrEBBFeDQFWtN3s/2zXop1c=',
        'X-Layout': 'multi',
        'Access-Control-Allow-Origin': '*',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'close',
    }
    d = "side_id=1812511&anonymous=0&referrer=https%3A%2F%2Fwww.diariolaprovinciasj.com%2Fsociedad%2F2019%2F2%2F5%2Fvota-en-diario-la-provincia-sj-quien-queres-que-sea-la-proxima-reina-nacional-del-sol-104379.html&os_utm_source=&render=1&user_answer="
    url = 'https://www.opinionstage.com/widgets/api/polls/2537564/cookie_vote'
    res = requests.post(url,headers=h,data=d)
    try:
        resultados = search('¡Gracias por votar!',res.text).group()
    except Exception as e:
        print(e)
        return res.status_code,e 
    return res.status_code,resultados

def getTotalVotes():
    h = {
        'Host': 'www.opinionstage.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.opinionstage.com/polls/2537564/poll',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-CSRF-Token': '9QtMEBIc6mi1anuqvSEMgrEBBFeDQFWtN3s/2zXop1c=',
        'X-Layout': 'multi',
        'Access-Control-Allow-Origin': '*',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'close',
    }
    url = 'https://www.opinionstage.com/widgets/api/polls/2537564/votes'
    res = requests.get(url,headers=h)
    try:
        cantidad = search('(?<={"count":)\d+',res.text).group()
    except Exception as e:
        print('[-] DLP: ',e)
        return res.status_code,e 
    return res.status_code,cantidad  

class Th(threading.Thread):
    def __init__(self,Id,printRes,cant):
        threading.Thread.__init__(self)
        self.Id = Id
        self.printRes = printRes
        self.cant = cant

    def printResultados(self,resultados):
        print('DLP: ',resultados,'Cantidad de votos: ',getTotalVotes()[1])
    
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
        sleep(1)
    if printStatus:print('DLP OK... +%d'%cant)

if __name__ == "__main__":
    main(True,True,cant=2)