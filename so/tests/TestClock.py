
import unittest

from clases.ReadyQueuePriority import ReadyQueuePriority
from clases.WaitingQueue import WaitingQueue 
from clases.QueuesManager import QueuesManager
from clases.Cpu import Cpu
from clases.Disk import Disk
from clases.FIFO import FIFO
from clases.FIFO import FIFO
from clases.Instruction import Instruction
from clases.IrqHandler import IrqHandler
from clases.Kernel import Kernel
from clases.Memory import Memory
from clases.MemoryManager import MemoryManager
from clases.Program import Program
from clases.Window import Window


class Test(unittest.TestCase):
    
    kernel=None
    cpu=None
    disk=None
    memory=None
    memoryManager=None
    queuesManager=None
    instruction=None
    window=None
    program=None


    def setUp(self):
        self.window=Window()
        self.instruction=Instruction('hola',self.window)
        self.program=Program('cacho',self.instruction)
        self.disk=Disk()
        self.disk.addProgram(self.program)
        self.memory = Memory(20)
        self.readyQueue = ReadyQueuePriority()
        self.waitingQueue = WaitingQueue()
        self.queuesManager = QueuesManager(self.readyQueue,self.waitingQueue)
        self.politicaFIFO = FIFO(self.queuesManager)
        self.irqHandler = IrqHandler(self.politicaFIFO)
        self.memoryManager = MemoryManager(self.memory)
        self.cpu = Cpu(self.memoryManager,self.irqHandler)
        self.kernel=Kernel(self.cpu,self.disk,self.memoryManager,self.queuesManager)


    def testClockCycle(self):
        self.assertTrue(self.kernel.getClock().is_alive())
        self.assertTrue(self.kernel.loadProgram('cacho'))
        self.assertTrue(self.kernel.runProgram('cacho'))
        self.cpu.fetch()
        self.assertEquals(self.window.getCantContents(),1)
       
        

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
