import unittest

from AsignacionContinua.MMUContinuedAllocation import MMUContinuedAllocation
from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from clases.Cpu import Cpu
from clases.Disk import Disk
from clases.FIFO import FIFO
from clases.FIFOReadyQueue import FIFOReadyQueue
from clases.IoWaitingQueue import IoWaitingQueue
from clases.IrqHandler import IrqHandler
from clases.Kernel import Kernel
from clases.QueuesManager import QueuesManager
from clases.Shell import Shell
from clases.WaitingQueue import WaitingQueue
from clases.MemoryManager import MemoryManager
from clases.CommandHandler import CommandHandler


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
        
        
       
        self.disk=Disk()
        self.kernel=Kernel(self.cpu,self.disk,self.irqHandler)
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