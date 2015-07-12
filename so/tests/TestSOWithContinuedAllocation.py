import unittest

from AsignacionContinua.BestFit import BestFit
from AsignacionContinua.MMUContinuedAllocation import MMUContinuedAllocation
from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from IO.Printer import Printer
from IO.Resource import Resource
from IO.Scanner import Scanner
from IO.Window import Window
from Irq.IrqHandler import IrqHandler
from Program.InstructionCpu import InstructionCpu
from Program.InstructionIO import InstructionIO
from Program.Program import Program
from SchedullingAndQueuesManager.FIFO import FIFO
from SchedullingAndQueuesManager.FIFOReadyQueue import FIFOReadyQueue
from SchedullingAndQueuesManager.IoWaitingQueue import IoWaitingQueue
from SchedullingAndQueuesManager.QueuesManager import QueuesManager
from SchedullingAndQueuesManager.WaitingQueue import WaitingQueue
from Shell.CommandHandler import CommandHandler
from Shell.Shell import Shell
from clases.Clock import Clock
from clases.Cpu import Cpu
from clases.Disk import Disk
from clases.Kernel import Kernel


class TestSOWithContinuedAllocation(unittest.TestCase):


    def setUp(self):
        
        self.memory=PhysicalMemoryContinuedAllocation(20)
        self.routineBestFit = BestFit()
        self.mmuContinuedAllocation=MMUContinuedAllocation(self.memory,self.routineBestFit)
        
        self.colaReadyFifo = FIFOReadyQueue()
         
        self.colaWaiting = WaitingQueue()
        self.ioWaitingQueue =IoWaitingQueue() 
         
        self.adminDeColasConcolaReadyFifo = QueuesManager(self.colaReadyFifo,self.colaWaiting,self.ioWaitingQueue)
        
        self.politicaFifo = FIFO(self.adminDeColasConcolaReadyFifo)
       
        
        self.irqHandler=IrqHandler(self.politicaFifo)
        
        self.cpu=Cpu(self.mmuContinuedAllocation,self.irqHandler)
        
        
        self.disk=Disk()
        self.clock=Clock(self.cpu)
        self.kernel=Kernel(self.cpu,self.disk,self.irqHandler,self.clock)
        self.commandHandler=CommandHandler()
        self.shell=Shell(self.kernel,self.commandHandler)
        
        self.window = Window()
        self.scanner = Scanner()
        self.printer = Printer()
        
        instruction1=InstructionIO('hello',Resource.window)
        instruction2=InstructionIO('hello',Resource.scanner)
        instruction3=InstructionCpu('hello',self.cpu)
        instruction4=InstructionIO('hello',Resource.printer)
        instruction5=InstructionCpu('hello',self.cpu)
        instruction6=InstructionCpu('hello',self.cpu)
        
        self.program1 = Program('program1',instruction2,instruction1,instruction3)
        self.disk.addProgram(self.program1)
        
        self.program2 = Program('program2',instruction4,instruction1,instruction2,instruction5)
        self.disk.addProgram(self.program2)
        
        self.program3 = Program('program3',instruction1,instruction2,instruction3,instruction4,instruction5,instruction6)
        self.disk.addProgram(self.program3)
        



    def testLoadProgram(self):
        self.kernel.loadProgram("program1")
        
        self.assertEqual(self.irqHandler.cantIrqs(),1)
        ## FIRST CYLCE
        self.clock.notifyCycle()
        self.assertEqual(self.irqHandler.cantIrqs(),0)
        self.assertEqual(self.colaReadyFifo.first().getName(),self.program1.getName())
        
        self.kernel.loadProgram("program2")
        
        self.assertEqual(self.irqHandler.cantIrqs(),1)
        
        ## SECOND CYCLE
        self.clock.notifyCycle()
        self.assertEqual(self.irqHandler.cantIrqs(),0)
        self.assertEqual(self.colaReadyFifo.first().getName(),self.program2.getName())
        self.assertEquals(self.cpu.getPcb().getName(),self.program1.getName())
        
        ##THIRD CYLCE
        
        ##USER MODE
        self.clock.notifyUserMode()
        self.assertEqual(self.irqHandler.cantIrqs(),1)
        self.assertEqual(self.colaReadyFifo.first().getName(),self.program2.getName())
        self.assertEquals(self.cpu.getPcb().getName(),self.program1.getName())
        
        ##KERNEL MODE
        self.clock.notifyKernelMode()
        self.assertEqual(self.irqHandler.cantIrqs(),0)
        self.assertEqual(self.colaReadyFifo.first(),None)
        self.assertEquals(self.cpu.getPcb().getName(),self.program2.getName())
        self.assertEqual(self.scanner.get(0)[0].getName(),self.program1.getName())
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
