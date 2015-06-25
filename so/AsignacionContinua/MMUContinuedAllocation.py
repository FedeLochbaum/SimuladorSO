from clases.MemoryManager import MemoryManager
from AsignacionContinua.Block import Block
from _overlapped import NULL
class MMUContinuedAllocation(MemoryManager):
        
    def __init__(self,memory,routineBlock):
        self.super.__init__(memory)
        self.bloquesDisponibles = [Block(1,memory.space)]
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
        pcb.setBlock(block)
        self.addinstructionsToMemory(block.getInicio(),block.getFin(),pcb)
            
    def hayBloqueDisponible(self,pcb):
        for block in self.bloquesDisponibles: 
            if(block.size > pcb.getFinalPc()):
                return True
        return False
    
    def traerBloqueSegunRutina(self,cantidad):
        return self.routine.blockFor(cantidad,self.bloquesDisponibles,self)        
       
    def cleanMemory(self,pcb):
        bloque = pcb.getBlock()
        self.agregarABloquesLibres(bloque)
        pcb.setBlock(NULL)
        self.reordenarBloques()
        
    def sacarBloque(self,block):
        self.bloquesDisponibles.remove(block)
    def reordenarBloques(self):
        pass
    def compactMemory(self):
        pass
    def agregarABloquesLibres(self,block):
        self.bloquesDisponibles.append(block)
    def addinstructionsToMemory(self,inicio,final,pcb):
        i = inicio 
        for instruction in pcb.getInstructions():
            if(i <= final):
                self.memory.put(i,instruction)
                i = i+1
            #hay que ver.. creoque esta bien