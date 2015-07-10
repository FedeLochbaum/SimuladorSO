
import unittest

from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from Irq.Irq import Irq
from Irq.IrqHandler import IrqHandler
from Program.InstructionCpu import InstructionCpu
from Program.Pcb import Pcb
from SchedullingAndQueuesManager.FIFO import FIFO
from SchedullingAndQueuesManager.IoWaitingQueue import IoWaitingQueue
from SchedullingAndQueuesManager.QueuesManager import QueuesManager
from SchedullingAndQueuesManager.ReadyQueuePriority import ReadyQueuePriority
from SchedullingAndQueuesManager.WaitingQueue import WaitingQueue
from clases.Cpu import Cpu
from clases.MemoryManager import MemoryManager


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
        self.inst=InstructionCpu('hola')
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