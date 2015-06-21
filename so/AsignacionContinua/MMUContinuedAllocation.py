from clases.MemoryManager import MemoryManager
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
                self.compactarMemory()
                self.loadProgram(pcb)
        
    def agregarAmemoria(self,pcb,bloque):
        for instruction in pcb.getInstructions():
            bloque.addInstruction(instruction)
            
    
    def hayBloqueDisponible(self,pcb):
        for each in self.bloquesDisponibles: 
            if(each.size > pcb.getFinalPc()):
                return True
        return False
    
    def traerBloqueSegunRutina(self,cantidad):
        bloque =  self.routine.dameBloquePara(cantidad,self.bloquesDisponibles)
        self.reordenarBloque(bloque)
        return bloque        
        