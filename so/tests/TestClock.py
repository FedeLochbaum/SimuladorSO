
import unittest

from clases.Clock import Clock
from clases.Cpu import Cpu
from clases.FIFO import FIFO
from clases.Instruction import Instruction
from clases.InstructionCpu import InstructionCpu
from clases.IoWaitingQueue import IoWaitingQueue
from clases.Irq import Irq
from clases.IrqHandler import IrqHandler
from clases.Memory import Memory
from clases.MemoryManager import MemoryManager
from clases.Pcb import Pcb
from clases.QueuesManager import QueuesManager
from clases.ReadyQueuePriority import ReadyQueuePriority
from clases.Resource import Resource
from clases.WaitingQueue import WaitingQueue 
from clases.Window import Window


class Test(unittest.TestCase):
    
   
    cpu=None
    memory=None
    memoryManager=None
    queuesManager=None
    instructionCpu=None
    window=None
    pcb=None
    clock=None


    def setUp(self):
        self.pcb=Pcb('proceso',1,0,1,0)
        self.memory = Memory(20)
        self.readyQueue = ReadyQueuePriority()
        self.ioWaitingQueue = IoWaitingQueue()
        self.waitingQueue = WaitingQueue()
        self.queuesManager = QueuesManager(self.readyQueue,self.waitingQueue,self.ioWaitingQueue)
        self.politicaFIFO = FIFO(self.queuesManager)
        self.irqHandler = IrqHandler(self.politicaFIFO)
        self.memoryManager = MemoryManager(self.memory)
        self.cpu = Cpu(self.memoryManager,self.irqHandler)
        self.cpu.setProcess(self.pcb)
        self.instruction=InstructionCpu('hola',self.cpu)
        self.memory.put(0, self.instruction)
        self.clock=Clock(self.cpu)
        


    def testClockCycle(self):
        self.clock.notifyObservers()
        self.assertEqual(self.pcb.getPc(),1)
        self.assertEqual(self.cpu.getIrqHandler().cantIrqs(),1)
        self.assertEqual(self.cpu.getIrqHandler().get(0), Irq.kill)
       
        

    def tearDown(self):
        self.kernel=None
        self.cpu=None
        self.disk=None
        self.memory=None
        self.memoryManager=None
        self.queuesManager=None
        self.instruction=None
        self.window=None
        self.program=None


    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
