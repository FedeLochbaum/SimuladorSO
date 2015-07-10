import unittest

from IO.Window import Window
from Paginacion.MMUPaginacion import MMUPaginacion
from Paginacion.PhysicalMemory import PhysicalMemory
from Program.InstructionIO import InstructionIO
from Program.Program import Program


class TestMMUPaginacion(unittest.TestCase):
    
    def setUp(self):
        self.memory = PhysicalMemory(10,2)
        
        
        self.mmuPaginacion = MMUPaginacion(self.memory)
        
        self.window = Window()
        
        instruction1=InstructionIO('hello',self.window)
        instruction2=InstructionIO('hello',self.window)
        instruction3=InstructionIO('hello',self.window)
        instruction4=InstructionIO('hello',self.window)
        instruction5=InstructionIO('hello',self.window)
        instruction6=InstructionIO('hello',self.window)
        
        self.program1 = Program('program1',instruction2,instruction1,instruction3)
        
        self.program2 = Program('program2',instruction4,instruction1,instruction2,instruction5)
        
        self.program3 = Program('program3',instruction1,instruction2,instruction3,instruction4,instruction5,instruction6)
        
    def testLoadProgram(self):
        
        
        self.assertEquals(self.memory.getFreeSpace(),10)
        self.mmuPaginacion.loadProgram(self.program1)
        self.assertEquals(self.memory.getFreeSpace(),7)
        self.mmuPaginacion.loadProgram(self.program3)
        self.assertEquals(self.memory.getFreeSpace(),1)
        
        
    
        