from heapq import heappush, heappop, heapify
from queue import Queue

from clases.Pcb import Pcb


class ReadyQueuePriority:
    def __init__(self):
        self.ready = []

    def put(self,elemet):
        self.ready.append([elemet.getPriority(), elemet])
        heapify (self.ready)

   
    
    def next(self):
        resultado = heappop(self.ready)[1]
        self.envejecerHeap()
        return resultado
    
    def envejecerHeap(self):
        for  i,(priority,item)  in  enumerate(self.ready):
            self.ready[i]=[priority-1,item]

    
i = ReadyQueuePriority()
i.put(Pcb('proceso',1,0,1,0,22))
i.put(Pcb('proceso',1,0,1,0,22))
i.put(Pcb('proceso',1,0,1,0,1))
i.put(Pcb('proceso',1,0,1,0,3))
i.put(Pcb('proceso',1,0,1,0,4))
i.put(Pcb('proceso',1,0,1,0,2))
i.put(Pcb('proceso',1,0,1,0,5))

print (i.next().getPriority())
print (i.next().getPriority())
print (i.next().getPriority())
print (i.next().getPriority())
print (i.next().getPriority())          
