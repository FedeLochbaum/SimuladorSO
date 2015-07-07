
import unittest

from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from clases.Cpu import Cpu
from clases.FIFO import FIFO
from clases.Instruction import Instruction
from clases.InstructionCpu import InstructionCpu
from clases.IoWaitingQueue import IoWaitingQueue
from clases.Irq import Irq
from clases.IrqHandler import IrqHandler
from clases.MemoryManager import MemoryManager
from clases.Pcb import Pcb
from clases.PhysicalMemory import PhysicalMemory
from clases.QueuesManager import QueuesManager
from clases.ReadyQueuePriority import ReadyQueuePriority
from clases.WaitingQueue import WaitingQueue 
from clases.Window import Window


class TestCpu(unittest.TestCase):
    cpu=None
    window=None
    inst=None
    mem=None
    pcb=None

    def setUp(self):
        self.pcb=Pcb('proceso',1,0,1,0)
        self.pcb2=Pcb('proceso2',2,0,1,0)
        self.pcb3=Pcb('proceso3',3,0,1,0)
        self.mem=PhysicalMemoryContinuedAllocation(20)
        self.readyQueue = ReadyQueuePriority()
        self.ioWaitingQueue =IoWaitingQueue()
        self.readyQueue.put(self.pcb2)
        self.readyQueue.put(self.pcb3)
        self.waitingQueue = WaitingQueue()
        self.queuesManager = QueuesManager(self.readyQueue,self.waitingQueue,self.ioWaitingQueue)
        self.politicaFIFO = FIFO(self.queuesManager)
        self.irqHandler = IrqHandler(self.politicaFIFO)
        self.memoryManager = MemoryManager(self.mem)
        self.cpu=Cpu(self.memoryManager,self.irqHandler)
        self.inst=InstructionCpu('hola',self.cpu)
        self.mem.put(0, self.inst)
        
        

    def tearDown(self):
        self.cpu=None
        self.window=None
        self.inst=None
        self.mem=None
        self.pcb=None


    def testFetch(self):
        self.cpu.setProcess(self.pcb)
        self.cpu.fetch()
        
        self.assertEqual(self.pcb.getPc(),1)
        self.assertEqual(self.cpu.getIrqHandler().cantIrqs(),1)
        self.assertTrue(self.cpu.getIrqHandler().get(Irq.kill)!=None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()