'''
Created on 15/05/2015

@author: apiorno
'''
import unittest


from clases.Cpu import Cpu
from clases.Disk import Disk

from clases.Kernel import Kernel
from clases.Memory import Memory
from clases.Program import Program
from clases.Window import Window
from clases.Instruction import Instruction
from clases.MemoryManager import MemoryManager




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
        self.memoryManager = MemoryManager(self.memory)
        self.cpu = Cpu(self.memory)
        self.kernel=Kernel(self.cpu,self.disk,self.memoryManager,self.queuesManager)


    def clockCycle(self):
        time.sleep(1)
        assertEquals(self.window.getCantContents(),1)
        time.sleep(1)
        assertEquals(self.window.getCantContents(),1)
        time.sleep(1)
        assertEquals(self.window.getCantContents(),1)
        

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
