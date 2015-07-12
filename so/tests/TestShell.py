import unittest

from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from Irq.IrqHandler import IrqHandler
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
from clases.MemoryManager import MemoryManager


class Test(unittest.TestCase):


    def setUp(self):
        
        self.memory=PhysicalMemoryContinuedAllocation(20)
        self.memoryManager=MemoryManager(self.memory)
        
        self.colaReadyFifo = FIFOReadyQueue()
         
        self.colaWaiting = WaitingQueue()
        self.ioWaitingQueue =IoWaitingQueue() 
         
        self.adminDeColasConcolaReadyFifo = QueuesManager(self.colaReadyFifo,self.colaWaiting,self.ioWaitingQueue)
        
        self.politicaFifo = FIFO(self.adminDeColasConcolaReadyFifo)
       
        
        self.irqHandler=IrqHandler(self.politicaFifo)
        
        self.cpu=Cpu(self.memoryManager,self.irqHandler)
        
        
        self.clock=Clock(self.cpu)
        self.disk=Disk()
        self.kernel=Kernel(self.cpu,self.disk,self.irqHandler,self.clock)
        self.commandHandler=CommandHandler()
        self.shell=Shell(self.kernel,self.commandHandler)


    def tearDown(self):
        pass


    def testComandHelp(self):
        expected='Bienvenido a la ayuda del Sistema Operativo, tiene los siguientes comando disponibles:\n-help\n-?\n-load\n'
        actual=self.shell.readCommand('?')
        self.assertEqual(expected,actual)
        actual=self.shell.readCommand('help')
        self.assertEqual(expected,actual)
        actual=self.shell.readCommand('man')
        self.assertEqual(expected,actual)
        
        expected=3
        actual=self.shell.successCommandCount()
        self.assertEqual(expected,actual)
        
        expected='?'
        actual=self.shell.getSuccessCommands()[0]
        
        self.assertEqual(expected,actual)
        
        expected='help'
        actual=self.shell.getSuccessCommands()[1]
        
        self.assertEqual(expected,actual)
        
        expected='man'
        actual=self.shell.getSuccessCommands()[2]
        
        self.assertEqual(expected,actual)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()