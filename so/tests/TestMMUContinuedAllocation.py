import unittest

from AsignacionContinua.BestFit import BestFit
from AsignacionContinua.FirstFit import FirstFit
from AsignacionContinua.MMUContinuedAllocation import MMUContinuedAllocation
from AsignacionContinua.WorstFit import WorstFit
from clases.Instruction import Instruction
from clases.Memory import Memory
from clases.Program import Program

class TestMMUContinuedAllocation(unittest.TestCase):
    


    def setUp(self):
        self.memory = Memory(10)
        self.bestFit = BestFit()
        self.worstFit = WorstFit()
        self.firstFit = FirstFit()
    
        self.mmubestFit = MMUContinuedAllocation(self.memory,self.bestFit)
        self.mmuworstFit = MMUContinuedAllocation(self.memory,self.worstFit)
        self.mmufirstFit = MMUContinuedAllocation(self.memory,self.firstFit)
    
    
    def testLoadProgram(self):
        instruction1=Instruction('hello',self.window)
        instruction2=Instruction('hello',self.window)
        instruction3=Instruction('hello',self.window)
        instruction4=Instruction('hello',self.window)
        instruction5=Instruction('hello',self.window)
        instruction6=Instruction('hello',self.window)
        
        list1 = [instruction2,instruction1,instruction3]
        
        list2 = [instruction4,instruction1,instruction2,instruction5]
        
        list3 = [instruction1,instruction2,instruction3,instruction4,instruction5,instruction6]
        
        program1=Program('program1',list1)
        
        program2 = Program('program2',list2)
        
        program3 = Program('program3',list3)
        
        #load de mmuBestFit
        self.mmubestFit.loadProgram(program1)
        self.mmubestFit.loadProgram(program2)
        self.mmubestFit.loadProgram(program3)
        
        
        self.assertTrue(True)
    
    
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    