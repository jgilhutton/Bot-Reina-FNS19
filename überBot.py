import botDDC,botDN,botDLP,botDM,botZONDA,botS8,botDH
import threading
from time import sleep
from sys import argv

tanda = 1
ts = []
botList = [botDN,botZONDA,botDDC,botDLP,botDM,botS8,botDH]

class Th(threading.Thread):
    def __init__(self,Diario):
        threading.Thread.__init__(self)
        self.Diario      = Diario
        self.printStatus = False
        self.printRes    = False
    
    def run(self):
        ts.append(self)
        self.Diario.main(printStatus=self.printStatus,printRes=self.printRes,cant=10)
        
try:
    while True:
        threadDN,threadZONDA,threadDDC,threadDLP,threadDM,threadS8,threadDH = map(Th,botList)
        for thread in [threadDN,threadZONDA,threadDDC,threadDLP,threadDM,threadS8,threadDH]:
            thread.printRes     = True
            thread.printStatus  = True

        callDict = {'all':lambda: [callDict[x]() for x in callDict if x!='all'],'DDC':threadDDC.start,'DN':threadDN.start,'DLP':threadDLP.start,'DM':threadDM.start,'ZONDA':threadZONDA.start,'S8':threadS8.start,'DH':threadDH.start}

        if len(argv) == 1 or not all([callDict.__contains__(x) for x in argv[1:]]):
            print('Argumentos:')
            [print(x) for x in callDict]
            exit()
            
        print('Tanda %d...'%tanda)
        for diario in argv[1:]:
            callDict[diario]()

        for t in ts:
            t.join()
        
        sleep(10)
        tanda+=1
        print('='*50)

except KeyboardInterrupt:
    exit()