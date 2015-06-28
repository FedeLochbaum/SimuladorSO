from AsignacionContinua.RoutineBlock import RoutineBlock
class FirstFit(RoutineBlock):
    

    
    def blockFor(self,cantidad,listaDeBloques,mmu):
        list = filter(item.size > cantidad,listaDeBloques)#hay que ver que onda
        bloque = list[1]
        mmu.sacarBloque(bloque)
        bloqueG  = super.recortarBLoque(bloque,pcb)
        bloqueP = super.bloquePequenioDe(bloqueG,bloque)
        mmu.agregarABloquesLibres(bloqueP)
        return bloqueG
        
    