from heapq import heappush, heappop, heapify
from queue import Queue
from clases.PcbPriority import PcbPriority


class ReadyQueuePriority:
    def __init__(self):
        self.ready = []

    def put(self,elemet):
        self.ready.append((elemet.getPriority(), elemet))
        heapify (self.ready)

    def next(self):
        resultado = heappop(self.ready)[1]
        #self.envejecerHeap()
        return resultado
    
    def envejecerHeap(self):
        for  item  in  self.ready:
            item[0] = item[0]-1 ##esto no anda.. asique lo comento arriba
    
i = ReadyQueuePriority()
i.put(PcbPriority('proceso',1,0,1,0,22))
i.put(PcbPriority('proceso',1,0,1,0,1))
i.put(PcbPriority('proceso',1,0,1,0,3))
i.put(PcbPriority('proceso',1,0,1,0,4))
i.put(PcbPriority('proceso',1,0,1,0,2))
i.put(PcbPriority('proceso',1,0,1,0,5))
print (i.get().getPriority())
print (i.get().getPriority())
print (i.get().getPriority())
print (i.get().getPriority())
print (i.get().getPriority())          
