import unittest
from Paginacion.LogicMemory import LogicMemory
from Paginacion.Page import Page


class Test(unittest.TestCase):


    def setUp(self):
        self.logicMemory=LogicMemory(5)
        self.page1=Page(2)


    def tearDown(self):
        pass


    def testPut(self):
        self.logicMemory.put(1001,self.page1)
        self.assertEqual(self.logicMemory.get(self.page1), 1001)
        self.assertEqual(self.logicMemory.freeSpace, 4)
        
    def testRemove(self):
        self.logicMemory.put(1001,self.page1)
        
        self.assertEqual(self.logicMemory.get(self.page1), 1001)
        self.assertEqual(self.logicMemory.freeSpace, 4)
        
        expected=1001
        actual=self.logicMemory.remove(self.page1)
        self.assertEqual(expected,actual)
        self.assertEqual(self.logicMemory.freeSpace, 5)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()