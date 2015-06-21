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
        
    def agregarAmemoria(self,pcb):
        
            
    
    def hayBloqueDisponible(self,pcb):
        ***iterar self.bloquesDisponibles hay que ver que ed usamos para los bloques :D 
            result = result or (each.size > pcb.getFinalPc())
        return result
    
    def traerBloqueSegunRutina(self,cantidad):
        bloque =  self.routine.dameBloquePara(cantidad,sef.bloquesDisponibles)
        self.reordenarBloque(bloque)
        return bloque        
        