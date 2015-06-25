from AsignacionContinua.Block import Block
class RoutineBlock:
    
    
    def blockFor(self):
        pass    
    
    def recortarBLoque(self,block,pcb):
        block2 = Block(block.getInicio(),pcb.getSize())
        return block2
        
    def bloquePequenioDe(self,blockG,block):
        return Block(blockG.getFin()+1,block.getFin()+(block.size()-blockG.size()))