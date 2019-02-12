import botDDC,botDN,botDLP,botDM,botZONDA,botS8,botDH,botTPO
import threading
from time import sleep
from sys import argv

tanda = 1
ts = []
botList = [botDN,botZONDA,botDDC,botDLP,botDM,botS8,botDH,botTPO]

class Th(threading.Thread):
    def __init__(self,Diario):
        threading.Thread.__init__(self)
        self.Diario      = Diario
        self.printStatus = False
        self.printRes    = False
        self.cantidad    = None
    
    def run(self):
        ts.append(self)
        self.Diario.main(printStatus=self.printStatus,printRes=self.printRes,cant=self.cantidad)
        
try:
    while True:
        print('='*50)
        threadDN,threadZONDA,threadDDC,threadDLP,threadDM,threadS8,threadDH,threadTPO = map(Th,botList)

        callDict = {'all':lambda: [callDict[x]() for x in callDict if (x!='all' and not x.isdigit())],'TPO':threadTPO.start,'DDC':threadDDC.start,'DN':threadDN.start,'DLP':threadDLP.start,'DM':threadDM.start,'ZONDA':threadZONDA.start,'S8':threadS8.start,'DH':threadDH.start}
        cantidad = [x for x in filter(lambda x: x.isdigit(),argv)]
        
        for thread in [threadDN,threadZONDA,threadDDC,threadDLP,threadDM,threadS8,threadDH,threadTPO]:
            thread.printRes     = True
            thread.printStatus  = True
            thread.cantidad     = int(cantidad[0]) if cantidad else 10
        
        if len(argv) == 1 or not all([callDict.__contains__(x) for x in argv[1:] if not x.isdigit()]):
            print('Argumentos:')
            [print(x) for x in callDict]
            exit()
            
        print('Tanda %d...'%tanda)
        for diario in filter(lambda x: not x.isdigit(),argv[1:]):
            callDict[diario]()

        for t in ts:
            t.join()

        while True:
            if all([not x.isAlive() for x in ts]): break
            else: sleep(1)
        
        tanda+=1
        if cantidad:
            exit()

except KeyboardInterrupt:
    exit()