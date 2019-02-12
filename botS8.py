import requests
import threading
from re import findall,search
from time import sleep
from random import randint

def vote():
    callback = str(randint(0,1000000000)).zfill(9)
    h = {
        'Host': 'www.sanjuan8.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.sanjuan8.com/contenidos/fiesta-nacional-del-sol-2019.html',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'close',
    }

    d = "idSurvey=1609&idOption=4648"
    url = 'https://www.sanjuan8.com/_post/lacapital/survey_submit.php?undefined&callback=jQuery11120054644219908464686_1549{}'.format(callback)
    try:
        res = requests.post(url,headers=h,data=d)
    except Exception as e:
        print('[-] S8 %s'%e, 'Esperando 5 segundos...')
        sleep(5)
        res = requests.post(url,headers=h,data=d)
    try:
        resultados = search('(?<={"status":")ok(?="})',res.text).group()
    except Exception as e:
        print(e)
        return res.status_code,e 
    return res.status_code,resultados

class Th(threading.Thread):
    def __init__(self,Id,printRes,cant):
        threading.Thread.__init__(self)
        self.Id = Id
        self.printRes = printRes
        self.cant = cant

    def printResultados(self,resultados):
        print('S8: ',resultados.upper())
    
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
    if printStatus:print('S8 OK... +%d'%cant)

if __name__ == "__main__":
    main(True,True,cant=2)