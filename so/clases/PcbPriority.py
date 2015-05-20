from clases.Pcb import Pcb
class PcbPriority(Pcb):
    def __init__(self,name,pid,pc,finalPc,baseDirection,prioridad):
        super.__init__(name,pid,pc,finalPc,baseDirection)
        self.prioridad = (prioridad * -1)
        
        
    def getPriority(self):
        return self.prioridad    