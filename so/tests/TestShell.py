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
from clases.WaitingQueue import WaitingQueue


class Test(unittest.TestCase):


    def setUp(self):
        
        self.memory=PhysicalMemoryContinuedAllocation(20)
        self.memoryManager=MMUContinuedAllocation(self.memory)
        
        self.colaReadyFifo = FIFOReadyQueue()
         
        self.colaWaiting = WaitingQueue()
        self.ioWaitingQueue =IoWaitingQueue() 
         
        self.adminDeColasConcolaReadyFifo = QueuesManager(self.colaReadyFifo,self.colaWaiting,self.ioWaitingQueue)
        
        self.politicaFifo = FIFO(self.adminDeColasConcolaReadyFifo)
       
        
        self.irqHandler=IrqHandler(self.politicaFifo)
        
        self.cpu=Cpu(self.memoryManager,self.irqHandler)
        
        
       
        self.disk=Disk()
        self.kernel=Kernel(self.cpu,self.disk,self.irqHandler)
        self.shell=Shell(self.kernel)


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()