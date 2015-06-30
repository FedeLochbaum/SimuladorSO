from AsignacionContinua.Block import Block
from AsignacionContinua.RoutineBlock import RoutineBlock


class BestFit(RoutineBlock):
    
    
    
    def getBlockFor(self,cantidad,mapDeBloques,mmu):
        list = RoutineBlock.bloquesMasGrandes(self,cantidad,mapDeBloques)
        blockR = Block(1,100000000000000000000)
        for block in list:
            if(block.size() < blockR.size()):
                blockR = block
                
                
        mmu.sacarBloque(blockR)
        blockG  = RoutineBlock.recortarBLoque(self,blockR,cantidad)
        blockP = RoutineBlock.bloquePequenioDe(self,blockG,blockR)
        mmu.agregarABloquesLibres(blockP)
        return blockG       
    