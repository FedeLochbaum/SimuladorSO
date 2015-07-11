import unittest


from IO.Printer import Printer
from IO.Scanner import Scanner
from IO.Window import Window
from Irq.IrqHandler import IrqHandler
from Paginacion.CpuPaginacion import CpuPaginacion
from Paginacion.MMUPaginacion import MMUPaginacion
from Paginacion.PhysicalMemory import PhysicalMemory
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
from clases.Disk import Disk
from clases.Kernel import Kernel


class Test(unittest.TestCase):


    def setUp(self):
        
        self.memory=PhysicalMemory(20)
        self.mmuPaginacion=MMUPaginacion(self.memory)
        
        self.colaReadyFifo = FIFOReadyQueue()
         
        self.colaWaiting = WaitingQueue()
        self.ioWaitingQueue =IoWaitingQueue() 
         
        self.adminDeColasConcolaReadyFifo = QueuesManager(self.colaReadyFifo,self.colaWaiting,self.ioWaitingQueue)
        
        self.politicaFifo = FIFO(self.adminDeColasConcolaReadyFifo)
       
        
        self.irqHandler=IrqHandler(self.politicaFifo)
        
        self.cpu=CpuPaginacion(self.memoryManager,self.irqHandler)
        
        
        self.disk=Disk()
        self.kernel=Kernel(self.cpu,self.disk,self.irqHandler)
        self.commandHandler=CommandHandler()
        self.shell=Shell(self.kernel,self.commandHandler)
        
        self.window = Window()
        self.scanner = Scanner()
        self.printer = Printer()
        
        instruction1=InstructionIO('hello',self.window)
        instruction2=InstructionIO('hello',self.scanner)
        instruction3=InstructionCpu('hello',self.window)
        instruction4=InstructionIO('hello',self.printer)
        instruction5=InstructionCpu('hello',self.window)
        instruction6=InstructionCpu('hello',self.window)
        
        self.program1 = Program('program1',instruction2,instruction1,instruction3)
        self.disk.addProgram(self.program1)
        
        self.program2 = Program('program2',instruction4,instruction1,instruction2,instruction5)
        self.disk.addProgram(self.program2)
        
        self.program3 = Program('program3',instruction1,instruction2,instruction3,instruction4,instruction5,instruction6)
        self.disk.addProgram(self.program3)
        



    def TestLoadProgram(self):
        self.kernel.loadProgram("program1")
        self.kernel.loadProgram("program2")
        self.kernel.loadProgram("program3")
        self.assertTrue(True)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
