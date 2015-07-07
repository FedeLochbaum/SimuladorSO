import unittest

from Paginacion.LogicMemory import LogicMemory
from Paginacion.Page import Page
from clases.InstructionIO import InstructionIO
from clases.Resource import Resource


class Test(unittest.TestCase):


    def setUp(self):
        self.logicMemory=LogicMemory(5)
        self.page1=Page(2)
        self.instruction1=InstructionIO('hola',Resource.printer)
        self.instruction2=InstructionIO('hola',Resource.scanner)
        self.page1.addInstruction(self.instruction1)
        self.page1.addInstruction(self.instruction2)
        


    def tearDown(self):
        pass


    def testPut(self):
        self.logicMemory.put(0,self.page1)
        self.assertEqual(self.logicMemory.get(self.page1), 0)
        self.assertEqual(self.logicMemory.freeSpace, 4)
        
    def testRemove(self):
        self.logicMemory.put(0,self.page1)
        
        self.assertEqual(self.logicMemory.get(self.page1), 0)
        self.assertEqual(self.logicMemory.freeSpace, 4)
        
        expected=0
        actual=self.logicMemory.remove(self.page1)
        self.assertEqual(expected,actual)
        self.assertEqual(self.logicMemory.freeSpace, 5)
        
    def testNextIndex(self):
        self.assertEqual(self.logicMemory.getNextIndex(), 0)
        self.logicMemory.put(0,self.page1)
        self.assertEqual(self.logicMemory.getNextIndex(), 1)
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()