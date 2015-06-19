from clases.MemoryManager import MemoryManager
class MMUContinuedAllocation(MemoryManager):
    
    def __init__(self,memory,routineBlock):
        self.super.__init__(memory)
        self.bloquesDisponibles = [Block(1,memory.space)]
        self.routine = routineBlock
        
        
    def agregarAmemoria(self,pcb):
        
    
    def hayBloqueDisponible(self,pcb):
        
    
    def traerBloqueSegunRutina(self,pcb):
        return self.routine.dameBloquePara(pcb.getFinalPc(),sef.bloquesDisponibles)
                
        