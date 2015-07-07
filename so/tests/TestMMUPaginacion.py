import unittest

from Paginacion.MMUPaginacion import MMUPaginacion
from clases.Instruction import Instruction
from clases.PhysicalMemory import PhysicalMemory
from clases.Program import Program


class TestMMUPaginacion(unittest.TestCase):
    
    def setUp(self):
        self.memory = PhysicalMemory(10)
        
        
        self.mmuPaginacion = MMUPaginacion(self.memory)
        
        instruction1=Instruction('hello',self.window)
        instruction2=Instruction('hello',self.window)
        instruction3=Instruction('hello',self.window)
        instruction4=Instruction('hello',self.window)
        instruction5=Instruction('hello',self.window)
        instruction6=Instruction('hello',self.window)
        
        self.program1 = Program('program1',instruction2,instruction1,instruction3)
        
        self.program2 = Program('program2',instruction4,instruction1,instruction2,instruction5)
        
        self.program3 = Program('program3',instruction1,instruction2,instruction3,instruction4,instruction5,instruction6)
        
    def testLoadProgram(self):
        
        self.assertEquals(self.memory1.getFreeSpace(),10)
        self.mmuPaginacion.loadProgram(self.program1)
        self.assertEquals(self.memory1.getFreeSpace(),7)
        self.mmuPaginacion.loadProgram(self.program3)
        self.assertEquals(self.memory1.getFreeSpace(),1)
        
        
    
        