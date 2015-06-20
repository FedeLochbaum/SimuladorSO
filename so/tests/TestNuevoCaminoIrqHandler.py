
import unittest

from clases.Cpu import Cpu
from clases.FIFO import FIFO
from clases.FIFOReadyQueue import FIFOReadyQueue
from clases.InstructionCpu import InstructionCpu
from clases.IoWaitingQueue import IoWaitingQueue
from clases.IrqHandler import IrqHandler
from clases.Memory import Memory
from clases.MemoryManager import MemoryManager
from clases.Pcb import Pcb
from clases.QueuesManager import QueuesManager
from clases.WaitingQueue import WaitingQueue
from clases.Window import Window


class Test(unittest.TestCase):

    cpu=None
    pcb=None
    irqHandler=None
    routine=None
    memory=None
    memoryManager=None
    instruction=None
    window=None
    
    def setUp(self):
        self.window=Window()
        self.instruction=InstructionCpu('holaaaa',self.window)
        self.memory=Memory(10)
        self.memory.put(0, self.instruction)
        self.memoryManager=MemoryManager(self.memory)
        self.colaReadyFifo = FIFOReadyQueue()
        self.colaWaiting = WaitingQueue()
        self.ioWaitingQueue =IoWaitingQueue() 
        self.adminDeColasConcolaReadyFifo = QueuesManager(self.colaReadyFifo,self.colaWaiting,self.ioWaitingQueue)
        self.politicaFifo = FIFO(self.adminDeColasConcolaReadyFifo)
        self.irqHandler=IrqHandler(self.politicaFifo)
        self.pcb=Pcb('asd',1,0,0,0)
        self.cpu=Cpu(self.memoryManager,self.irqHandler)
        self.cpu.setProcess(self.pcb)
        
        
        


    def tearDown(self):
        self.cpu=None
        self.pcb=None
        self.irqHandler=None
        self.routine=None
        self.memory=None
        self.memoryManager=None


    def testHandleIrqKill(self):
        self.cpu.fetch()
        #falta funcionalidad de ahndle real de todas als irqs


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHandle']
    unittest.main()