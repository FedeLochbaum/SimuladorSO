from clases.MemoryManager import MemoryManager
from AsignacionContinua.Block import Block
class MMUContinuedAllocation(MemoryManager):
        
    def __init__(self,memory,routineBlock):
        self.super.__init__(memory)
        self.bloquesDisponibles = [Block(1,memory.space)]
        self.bloquesNoDisponibles = []
        self.routine = routineBlock
        
    def loadProgram(self,pcb):
        if(self.memoryFree()>pcb.getFinalPc):
            if(self.hayBloqueDisponible()):
                bloque = self.traerBloquePara(pcb.getFinalPc())
                self.agregarAmemoria(pcb,bloque)
            else:
                self.compactMemory()
                self.loadProgram(pcb)
        
    def agregarAmemoria(self,pcb,block):
        for instruction in pcb.getInstructions():
            block.addInstruction(instruction)
            
    def hayBloqueDisponible(self,pcb):
        for block in self.bloquesDisponibles: 
            if(block.size > pcb.getFinalPc()):
                return True
        return False
    
    def traerBloqueSegunRutina(self,cantidad):
        block =  self.routine.blockFor(cantidad,self.bloquesDisponibles)
        self.reordenarBloque(block)
        return block        
       
    def reordenarBloque(self,block): 
        
    def compactMemory(self):
            
        ***falta la posibilidad de borrar y liberar un  bloque