
import unittest

from clases.Cpu import Cpu
from clases.Disk import Disk
from clases.FIFO import FIFO
from clases.FIFOReadyQueue import FIFOReadyQueue
from clases.InstructionCpu import InstructionCpu
from clases.InstructionIO import InstructionIO
from clases.IoWaitingQueue import IoWaitingQueue
from clases.Irq import Irq
from clases.IrqHandler import IrqHandler
from clases.Memory import Memory
from clases.MemoryManager import MemoryManager
from clases.Pcb import Pcb
from clases.Program import Program
from clases.QueuesManager import QueuesManager
from clases.Resource import Resource
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
    disk=None
    program1=None
    program2=None
    ioInstruction=None
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.ioInstruction=InstructionIO('hola io',Resource.scanner)
        self.program1=Program('asd','1')
        self.program2=Program('asd2','2')
        self.disk=Disk()
        self.disk.addProgram(self.program1)
        self.disk.addProgram(self.program2)
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
        self.pcb=Pcb('asd',1,0,1,0)
        self.cpu=Cpu(self.memoryManager,self.irqHandler)
        self.cpu.setProcess(self.pcb)
        
        
        


    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.cpu=None
        self.pcb=None
        self.irqHandler=None
        self.routine=None
        self.memory=None
        self.memoryManager=None


    def testHandleIrqKill(self):
        self.irqHandler.handle(Irq.kill, self.cpu)
        self.assertEqual(self.cpu.pcb,None)
        self.assertEqual(self.cpu.instructionsInMemoryCount(),0)
    
    def testHandleIrqTimeout(self):
        self.irqHandler.handle(Irq.timeOut, self.cpu)
        self.assertEqual(self.colaReadyFifo.next(), None)
        self.assertEqual(self.cpu.pcb,self.pcb)
        self.assertEqual(self.cpu.instructionsInMemoryCount(),1)
        
    def testHandleIrqnewProcess(self):
        self.irqHandler.handle(Irq.newProcess, self.cpu, self.program2)
        self.assertEqual(self.cpu.instructionsInMemoryCount(),2)
        self.assertEqual(self.cpu.pcb,self.pcb)
        self.assertEqual(self.colaReadyFifo.pcbCount(), 1)
        
    def testHandleIrqIO(self):
        self.memory.put(0, self.ioInstruction)
        self.irqHandler.handle(Irq.io, self.cpu)
        self.assertEqual(self.cpu.getActualInstruction().getResource(),Resource.scanner)
        self.assertEqual(self.cpu.getPcb(),None)
        
        
        
        
        
    
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHandle']
    unittest.main()