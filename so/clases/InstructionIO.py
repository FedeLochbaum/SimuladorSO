from clases.Instruction import Instruction
from _overlapped import NULL
class InstructionIO(Instruction):
    def __init__(self,message,window,io):
        Instruction.__init__(message,window)
        self.io = io
        self.answer = NULL
        
    def hacerIO(self):
        self.window.show(self.getMessage())  
        
    def setAnsert(self,answer):
        self.answer = answer    
        
    