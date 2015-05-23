from heapq import heappush, heappop, heapify
from queue import Queue

from clases.Pcb import Pcb


class ReadyQueuePriority:
    def __init__(self):
        self.ready = []

    def put(self,elemet):
        self.ready.append((elemet.getPriority(), elemet))
        heapify (self.ready)

    #def __lt__(self, other):   estoy viendo para cambiar la comprobacion de la prioridad
    #selfPriority = (self.priority, self.pid)   si queres ver si haces andar esto 
    #otherPriority = (other.priority, other.pid) mira esta pregunta https://stackoverflow.com/questions/9292415/i-notice-i-cannot-use-priorityqueue-for-objects#comment11718555_9292415
        #return selfPriority < otherPriority
    
    def next(self):
        resultado = heappop(self.ready)[1]
        self.envejecerHeap()
        return resultado
    
    def envejecerHeap(self):
        for  i,(priority,item)  in  enumerate(self.ready):
            self.ready[i]=(priority-1,item)
    
#i = ReadyQueuePriority()
#i.put(Pcb('proceso',1,0,1,0,22))
#i.put(Pcb('proceso',1,0,1,0,22))
#i.put(Pcb('proceso',1,0,1,0,1))
#i.put(Pcb('proceso',1,0,1,0,3))
#i.put(Pcb('proceso',1,0,1,0,4))
#i.put(Pcb('proceso',1,0,1,0,2))
#i.put(Pcb('proceso',1,0,1,0,5))
#print (i.next().getPriority())
#print (i.next().getPriority())
#print (i.next().getPriority())
#print (i.next().getPriority())
#print (i.next().getPriority())          
