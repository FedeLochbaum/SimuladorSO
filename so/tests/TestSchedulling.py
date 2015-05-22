import unittest

from clases.Cpu import Cpu
from clases.Memory import Memory
from clases.FIFO import FIFO
from clases.FIFOReadyQueue import FIFOReadyQueue
from clases.Pcb import Pcb
from clases.QueuesManager import QueuesManager
from clases.ReadyQueuePriority import ReadyQueuePriority
from clases.RoundRobin import RoundRobin
from clases.WaitingQueue import WaitingQueue


class Test(unittest.TestCase):
    cpu=Cpu(Memory(10))
    adminDeColasConcolaReadyFifo = None
    adminDecolaReadyPrioridad = None
    
    colaReadyFifo = None
    colaReadyPrioridad = None 
    
    colaWaiting = None
    
    politicaFifo = None
    politicaRoundRobin =  None
     
    politicaFifoPrioridad = None
    politicaRRPrioridad = None
    
     
     
    def setUp(self):
        self.colaReadyFifo = FIFOReadyQueue()
        self.colaReadyPrioridad = ReadyQueuePriority()
         
        self.colaWaiting = WaitingQueue()
         
        self.adminDecolaReadyPrioridad = QueuesManager(self.colaReadyPrioridad,self.colaWaiting)
        self.adminDeColasConcolaReadyFifo = QueuesManager(self.colaReadyFifo,self.colaWaiting)
        
 
        self.politicaFifo = FIFO(self.adminDeColasConcolaReadyFifo)
        self.politicaRoundRobin = RoundRobin(3,self.adminDeColasConcolaReadyFifo,self.cpu)
         
        self.politicaFifoPrioridad =FIFO(self.adminDecolaReadyPrioridad)
        self.politicaRRPrioridad = RoundRobin(3,self.adminDecolaReadyPrioridad,self.cpu)
        
        
        
        
    def testNextPoliticaConReadyFifo(self):
        
        self.colaReadyFifo.put(Pcb('proceso',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso1',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso4',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso2',1,0,1,0))
        
        #con politicaFifo Simple
        self.assertEqual(self.politicaFifo.next().getName(),"proceso")
        self.assertEqual(self.politicaFifo.next().getName(),"proceso1")
        self.assertEqual(self.politicaFifo.next().getName(),"proceso4")
        self.assertEqual(self.politicaFifo.next().getName(),"proceso2")
        
        
    def testNextPoliticaConReadyRoundRobin(self):
        
        self.colaReadyFifo.put(Pcb('proceso',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso1',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso4',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso2',1,0,1,0))
        
        #con politica RoundRobin Simple
        self.assertEqual(self.politicaRoundRobin.next().getName(),"proceso")
        self.assertEqual(self.politicaRoundRobin.next().getName(),"proceso1")
        self.assertEqual(self.politicaRoundRobin.next().getName(),"proceso4")
        self.assertEqual(self.politicaRoundRobin.next().getName(),"proceso2")
            
    def testNextPoliticaConReadyPrioridadFifo(self):
        self.colaReadyPrioridad.put(Pcb('proceso',1,0,1,0,22))
        self.colaReadyPrioridad.put(Pcb('proceso1',1,0,1,0,2))
        self.colaReadyPrioridad.put(Pcb('proceso4',1,0,1,0,4))
        self.colaReadyPrioridad.put(Pcb('proceso2',1,0,1,0,5))
        
        #con politicaFifo con prioridad
        self.assertEqual(self.politicaFifoPrioridad.next().getPriorityReal(),22)
        self.assertEqual(self.politicaFifoPrioridad.next().getPriorityReal(),4)
        self.assertEqual(self.politicaFifoPrioridad.next().getPriorityReal(),3)
        self.assertEqual(self.politicaFifoPrioridad.next().getPriorityReal(),1)
    
    def testNextPoliticaConReadyPrioridadRoundRobin(self):    
        self.colaReadyPrioridad.put(Pcb('proceso',1,0,1,0,22))
        self.colaReadyPrioridad.put(Pcb('proceso1',1,0,1,0,2))
        self.colaReadyPrioridad.put(Pcb('proceso4',1,0,1,0,4))
        self.colaReadyPrioridad.put(Pcb('proceso2',1,0,1,0,5))
        
        #con politicaRoundRobin con prioridad
        self.assertEqual(self.politicaRRPrioridad.next().getPriorityReal(),22)
        self.assertEqual(self.politicaRRPrioridad.next().getPriorityReal(),4)
        self.assertEqual(self.politicaRRPrioridad.next().getPriorityReal(),3)
        self.assertEqual(self.politicaRRPrioridad.next().getPriorityReal(),1)
        
        
        
if __name__ == "__main__":
    unittest.main()        