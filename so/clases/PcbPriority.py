from clases.Pcb import Pcb
class PcbPriority(Pcb):
    def __init__(self,name,pid,pc,finalPc,baseDirection,prioridad):
        self.pid = pid
        self.pc = pc
        self.name = name
        self.finalPc = finalPc
        self.baseDirection = baseDirection
        self.prioridad = (prioridad * -1)
        
        
    def getPriority(self):
        return self.prioridad    