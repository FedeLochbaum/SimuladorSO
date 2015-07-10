import unittest

from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from Irq.IrqHandler import IrqHandler
from Program.Pcb import Pcb
from SchedullingAndQueuesManager.FIFO import FIFO
from SchedullingAndQueuesManager.FIFOReadyQueue import FIFOReadyQueue
from SchedullingAndQueuesManager.IoWaitingQueue import IoWaitingQueue
from SchedullingAndQueuesManager.QueuesManager import QueuesManager
from SchedullingAndQueuesManager.ReadyQueuePriority import ReadyQueuePriority
from SchedullingAndQueuesManager.RoundRobin import RoundRobin
from SchedullingAndQueuesManager.WaitingQueue import WaitingQueue
from clases.Cpu import Cpu
from clases.MemoryManager import MemoryManager


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
    
    temp=None
    temp2=None
    cpu=None
    memory=None
    memoryManager=None
    irqHandler=None
    irqHandler2=None
     
    def setUp(self):
        self.memory=PhysicalMemoryContinuedAllocation(20)
        self.memoryManager=MemoryManager(self.memory)
        
        self.colaReadyFifo = FIFOReadyQueue()
        self.colaReadyPrioridad = ReadyQueuePriority()
         
        self.colaWaiting = WaitingQueue()
        self.ioWaitingQueue =IoWaitingQueue() 
         
        self.adminDecolaReadyPrioridad = QueuesManager(self.colaReadyPrioridad,self.colaWaiting,self.ioWaitingQueue)
        self.adminDeColasConcolaReadyFifo = QueuesManager(self.colaReadyFifo,self.colaWaiting,self.ioWaitingQueue)
        
        self.politicaFifo = FIFO(self.adminDeColasConcolaReadyFifo)
        self.politicaFifoPrioridad =FIFO(self.adminDecolaReadyPrioridad)
        self.politicaRRPrioridad = RoundRobin(3,self.adminDecolaReadyPrioridad)
        self.politicaRoundRobin = RoundRobin(3,self.adminDeColasConcolaReadyFifo)
        
        self.irqHandler=IrqHandler(self.politicaRoundRobin)
        self.irqHandler2=IrqHandler(self.politicaRRPrioridad)
        self.cpu=Cpu(self.memoryManager,self.irqHandler)

        
        
      
        
 
        
        
        
        
        
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
        self.assertEqual(self.politicaFifoPrioridad.next().getPriorityReal(),5)
        self.assertEqual(self.politicaFifoPrioridad.next().getPriorityReal(),4)
        self.assertEqual(self.politicaFifoPrioridad.next().getPriorityReal(),2)
    
    def testNextPoliticaConReadyPrioridadRoundRobin(self):    
        self.colaReadyPrioridad.put(Pcb('proceso',1,0,1,0,22))
        self.colaReadyPrioridad.put(Pcb('proceso1',1,0,1,0,2))
        self.colaReadyPrioridad.put(Pcb('proceso4',1,0,1,0,4))
        self.colaReadyPrioridad.put(Pcb('proceso2',1,0,1,0,5))
        
        #con politicaRoundRobin con prioridad
        self.assertEqual(self.politicaRRPrioridad.next().getPriorityReal(),22)
        self.assertEqual(self.politicaRRPrioridad.next().getPriorityReal(),5)
        self.assertEqual(self.politicaRRPrioridad.next().getPriorityReal(),4)
        self.assertEqual(self.politicaRRPrioridad.next().getPriorityReal(),2)
        
        
        
if __name__ == "__main__":
    unittest.main()        