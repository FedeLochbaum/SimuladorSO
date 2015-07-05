import unittest
from Paginacion.LogicMemory import LogicMemory
from Paginacion.Page import Page


class Test(unittest.TestCase):


    def setUp(self):
        self.logicMemory=LogicMemory(5)
        self.page1=Page(4)


    def tearDown(self):
        pass


    def testPut(self):
        self.logicMemory.put(1001,self.page1)
        self.assertEqual(self.logicMemory.get(1001), self.page1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()