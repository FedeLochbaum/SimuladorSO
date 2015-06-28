import unittest

from AsignacionContinua.BestFit import BestFit
from AsignacionContinua.FirstFit import FirstFit
from AsignacionContinua.MMUContinuedAllocation import MMUContinuedAllocation
from AsignacionContinua.WorstFit import WorstFit
from clases.Instruction import Instruction
from clases.Memory import Memory
from clases.Program import Program
from clases.Window import Window


class TestMMUContinuedAllocation(unittest.TestCase):
    


    def setUp(self):
        self.memory = Memory(10)
        self.bestFit = BestFit()
        self.worstFit = WorstFit()
        self.firstFit = FirstFit()
        self.window = Window()
    
        self.mmubestFit = MMUContinuedAllocation(self.memory,self.bestFit)
        self.mmuworstFit = MMUContinuedAllocation(self.memory,self.worstFit)
        self.mmufirstFit = MMUContinuedAllocation(self.memory,self.firstFit)
        
        instruction1=Instruction('hello',self.window)
        instruction2=Instruction('hello',self.window)
        instruction3=Instruction('hello',self.window)
        instruction4=Instruction('hello',self.window)
        instruction5=Instruction('hello',self.window)
        instruction6=Instruction('hello',self.window)
        
        list1 = [instruction2,instruction1,instruction3]
        
        list2 = [instruction4,instruction1,instruction2,instruction5]
        
        list3 = [instruction1,instruction2,instruction3,instruction4,instruction5,instruction6]
        
        self.program1 = Program('program1',list1)
        
        self.program2 = Program('program2',list2)
        
        self.program3 = Program('program3',list3)
    
    
    def testLoadProgram(self):
        
        
        #load de mmuBestFit
        self.assertEquals(self.memory.getFreeSpace(),10)
        self.mmubestFit.loadProgram(self.program1)
        self.assertEquals(self.memory.getFreeSpace(),7)
        self.mmubestFit.loadProgram(self.program3)
        self.assertEquals(self.memory.getFreeSpace(),1)
        
        
    def testcleanMemory(self):
        self.mmubestFit.loadProgram(self.program1)
        self.mmubestFit.loadProgram(self.program3)
        self.mmubestFit.cleanMemory(self.program1)
        self.self.assertEquals(self.memory.getFreeSpace(),4)
    
        #ESTE TEST ES UNA MIERDA HAY QUE TERMINARLO
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    