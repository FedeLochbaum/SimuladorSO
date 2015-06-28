import unittest

from AsignacionContinua.BestFit import BestFit
from AsignacionContinua.FirstFit import FirstFit
from AsignacionContinua.MMUContinuedAllocation import MMUContinuedAllocation
from AsignacionContinua.WorstFit import WorstFit
from clases.Memory import Memory


def setUp(self):
    self.memory = Memory(10)
    self.bestFit = BestFit()
    self.worstFit = WorstFit()
    self.firstFit = FirstFit()
    
    self.mmubestFit = MMUContinuedAllocation(self.memory,self.bestFit)
    self.mmuworstFit = MMUContinuedAllocation(self.memory,self.worstFit)
    self.mmufirstFit = MMUContinuedAllocation(self.memory,self.firstFit)
    
    
    def testLoadProgram(self):
        self.pcb=Pcb('proceso',1,0,1,0)
        self.pcb2=Pcb('proceso2',1,0,1,0)
        self.pcb3=Pcb('proceso3',1,0,1,0)
        self.assertEquals()
    
    
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    