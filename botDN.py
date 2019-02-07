import requests
import threading
from re import findall,search
from time import sleep

def vote():
    h = {
        'Host': 'www.damenoticias.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.damenoticias.com/encuesta/1068-fns-reinas-votacion',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'close',
    }
    d = "criterio=&criterio=&EncuestaId=1068&class=&accion=&Page=https%3A%2F%2Fwww.damenoticias.com%2F%2Fencuesta%2F1068-fns-reinas-votacion&method=btn_poll_vote&Module=ModPolls&ModuleMethod=&ProductId=&SITE_URL_COMMON=https%3A%2F%2Fwww.damenoticias.com%2Fwebsite_ver2%2Fcommon%2Fwww%2F&PATH_URL_MRW=https%3A%2F%2Fwww.damenoticias.com%2F&SITE_URL_ADMIN=https%3A%2F%2Fwww.damenoticias.com%2Fadmin%2F&p=&modal_view=&pattern=&url_params=&row_id=enc_1068_3077&row_status=&AMBIENTE=FRONT&login_opts=&edit_layout=&ContentId=&ContentType=&news_comment=&news_read=&NoticiaGaleriaId=&NoticiaEvento=&sortable_orders=&section_id=&piwik_api_url=PIWIK_API_URL&FB_APP_ID=1205329242853132&GA_ID=&DFP_ID=117626542&ModuleAjax=&grid_items=&paywall_status=&post_ajax=1"
    url = 'https://www.damenoticias.com/encuesta/1068-fns-reinas-votacion'
    try:
        res = requests.post(url,headers=h,data=d)
    except Exception as e:
        print('[-] DN %s'%e, 'Esperando 5 segundos...')
        sleep(5)
        res = requests.post(url,headers=h,data=d)
    try:
        resultados = findall('(?si)(?P<departamento>(?<=\<h3 \>).+?(?=\<\\\/h3))(?:.*?)(?P<porcentaje>(?<=voto_resultado\\\\">)\d+%(?=\<\\\\/span>))',res.text)
        resultados = list(set(resultados))
    except Exception as e:
        print('[-] DN %s'%e)
        return res.status_code,e 
    return res.status_code,resultados

class Th(threading.Thread):
    def __init__(self,Id,printRes,cant):
        threading.Thread.__init__(self)
        self.Id = Id
        self.printRes = printRes
        self.cant = cant

    def printResultados(self,resultados):
        resultados.sort(key=lambda x: int(search('\d+',x[1]).group()))
        for x,y in resultados:
            print('{}:\t{}'.format(y,x))
    
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
        sleep(5)
    if printStatus:print('DN OK... +%d'%cant)

if __name__ == "__main__":
    main(True,True,cant=2)
