
import unittest


class Test(unittest.TestCase):
    logicMemory=None

    def setUp(self):
        self.logicMemory=LogicMemory(20)


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()