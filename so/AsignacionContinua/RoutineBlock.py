from AsignacionContinua.Block import Block
class RoutineBlock:
    
    
    def blockFor(self):
        pass    
    
    def recortarBLoque(self,block,cantidad):
        block1 = Block(block.getInicio(),block.getInicio()+cantidad-1)
        return block1
        
    def bloquePequenioDe(self,blockG,block):
        return Block(blockG.getFin()+1,block.getFin()+(block.size()-blockG.size()))
    
    def bloquesMasGrandes(self,cantidad,mapDeBloques):
        list = []
        for (k,block) in mapDeBloques.items():
            if(block.size() >= cantidad):
                list.append(block)
        return list