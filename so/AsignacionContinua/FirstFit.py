from AsignacionContinua.RoutineBlock import RoutineBlock
class FirstFit(RoutineBlock):
    

    
    def getBlockFor(self,cantidad,mapDeBloques,mmu):
        list = RoutineBlock.bloquesMasGrandes(self,cantidad,mapDeBloques)
        block = list[1]
        mmu.sacarBloque(block)
        blockG  = RoutineBlock.recortarBLoque(self,block,cantidad)
        blockP = RoutineBlock.bloquePequenioDe(self,blockG,block)
        mmu.agregarABloquesLibres(blockP)
        return blockG
        
    