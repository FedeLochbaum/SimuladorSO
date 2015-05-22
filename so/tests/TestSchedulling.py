import unittest

from clases import ReadyQueuePriority
from clases import WaitingQueue
from clases import QueuesManager
from clases import FIFO
from clases import RoundRobin
from clases import Pcb
from clases.FIFORadyQueue import FIFOReadyQueue
from clases.PcbPriority import PcbPriority


class Test(unittest.TestCase):
    
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
        self.politicaRoundRobin = RoundRobin(self.adminDeColasConcolaReadyFifo)
         
        self.politicaFifoPrioridad =FIFO(self.adminDeColasConcolaReadyFifo)
        self.politicaRRPrioridad = RoundRobin(self.adminDeColasConcolaReadyFifo)
        
        
        
        
    def testNextPoliticaConReadyFifo(self):
        self.colaReadyFifo.put(Pcb('proceso',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso1',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso4',1,0,1,0))
        self.colaReadyFifo.put(Pcb('proceso2',1,0,1,0))
        
        self.assertEqual(self.politicaFifo.next().getName(),"proceso")
        self.assertEqual(self.politicaFifo.next().getName(),"proceso1")
        self.assertEqual(self.politicaFifo.next().getName(),"proceso4")
        self.assertEqual(self.politicaFifo.next().getName(),"proceso2")
        
        self.assertEqual(self.politicaRoundRobin.next().getName(),"proceso")
        self.assertEqual(self.politicaRoundRobin.next().getName(),"proceso1")
        self.assertEqual(self.politicaRoundRobin.next().getName(),"proceso4")
        self.assertEqual(self.politicaRoundRobin.next().getName(),"proceso2")
        
    def testNextPoliticaConReadyPrioridad(self):
        self.colaReadyPrioridad.put(PcbPriority('proceso',1,0,1,0,22))
        self.colaReadyPrioridad.put(PcbPriority('proceso1',1,0,1,0,2))
        self.colaReadyPrioridad.put(PcbPriority('proceso4',1,0,1,0,4))
        self.colaReadyPrioridad.put(PcbPriority('proceso2',1,0,1,0,5))
        
        self.assertEqual(self.politicaFifoPrioridad.next().getPriority(),22)
        self.assertEqual(self.politicaFifoPrioridad.next().getPriority(),5)
        self.assertEqual(self.politicaFifoPrioridad.next().getPriority(),4)
        self.assertEqual(self.politicaFifoPrioridad.next().getPriority(),2)
        
        self.assertEqual(self.politicaRRPrioridad.next().getPriority(),22)
        self.assertEqual(self.politicaRRPrioridad.next().getPriority(),5)
        self.assertEqual(self.politicaRRPrioridad.next().getPriority(),4)
        self.assertEqual(self.politicaRRPrioridad.next().getPriority(),2)
        
        
        
if __name__ == "__main__":
    unittest.main()        