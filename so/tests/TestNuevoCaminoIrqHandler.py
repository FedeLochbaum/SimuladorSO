
import unittest

from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from IO.Resource import Resource
from IO.Window import Window
from Irq.Irq import Irq
from Irq.IrqHandler import IrqHandler
from Program.InstructionCpu import InstructionCpu
from Program.InstructionIO import InstructionIO
from Program.Pcb import Pcb
from Program.Program import Program
from SchedullingAndQueuesManager.FIFO import FIFO
from SchedullingAndQueuesManager.FIFOReadyQueue import FIFOReadyQueue
from SchedullingAndQueuesManager.IoWaitingQueue import IoWaitingQueue
from SchedullingAndQueuesManager.QueuesManager import QueuesManager
from SchedullingAndQueuesManager.WaitingQueue import WaitingQueue
from clases.Cpu import Cpu
from clases.Disk import Disk
from clases.MemoryManager import MemoryManager


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
        self.instruction=InstructionCpu('holaaaa')
        self.memory=PhysicalMemoryContinuedAllocation(10)
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
        self.assertEqual( self.irqHandler.cantIrqs(),1)
        self.irqHandler.runIrqs();
        self.assertEqual(self.cpu.pcb,None)
        self.assertEqual(self.cpu.instructionsInMemoryCount(),0)
    
    def testHandleIrqTimeout(self):
        self.irqHandler.handle(Irq.timeOut, self.cpu)
        self.assertEqual( self.irqHandler.cantIrqs(),1)
        self.irqHandler.runIrqs();
        self.assertEqual(self.colaReadyFifo.next(), None)
        self.assertEqual(self.cpu.pcb,self.pcb)
        self.assertEqual(self.cpu.instructionsInMemoryCount(),1)
        
    def testHandleIrqnewProcess(self):
        self.irqHandler.handle(Irq.newProcess, self.cpu, self.program2)
        self.assertEqual( self.irqHandler.cantIrqs(),1)
        self.irqHandler.runIrqs();
        self.assertEqual(self.cpu.instructionsInMemoryCount(),2)
        self.assertEqual(self.cpu.pcb,self.pcb)
        self.assertEqual(self.colaReadyFifo.pcbCount(), 1)
        
    def testHandleIrqIO(self):
        self.memory.put(0, self.ioInstruction)
        self.irqHandler.handle(Irq.io, self.cpu,self.ioInstruction)
        self.assertEqual( self.irqHandler.cantIrqs(),1)
        self.irqHandler.runIrqs();
        self.cpu.actualInstruction=self.ioInstruction
        expected=self.cpu.getActualInstruction().getResource()
        actual=Resource.scanner
        self.assertEqual(expected,actual)
        expected=self.cpu.getPcb()
        actual=None
        self.assertEqual(expected,actual)
        
    def testHandleIrqIoFinish(self):
        self.memory.put(0, self.ioInstruction)
        self.irqHandler.handle(Irq.ioFinish, self.cpu)
        self.assertEqual( self.irqHandler.cantIrqs(),1)
        self.irqHandler.runIrqs();
        self.assertEqual(self.colaReadyFifo.pcbCount(), 1)
        self.assertEqual(self.colaReadyFifo.first(), self.pcb)
        
        
        
        
        
    
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHandle']
    unittest.main()