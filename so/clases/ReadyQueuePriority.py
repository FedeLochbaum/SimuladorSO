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
