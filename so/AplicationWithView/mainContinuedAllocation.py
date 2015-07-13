from test.test_idle import tk

from AsignacionContinua.BestFit import BestFit
from AsignacionContinua.MMUContinuedAllocation import MMUContinuedAllocation
from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from IO.Printer import Printer
from IO.Scanner import Scanner
from IO.Window import Window
from Irq.IrqHandler import IrqHandler
from Program.InstructionCpu import InstructionCpu
from Program.InstructionIO import InstructionIO
from Program.Program import Program
from SchedullingAndQueuesManager.FIFO import FIFO
from SchedullingAndQueuesManager.FIFOReadyQueue import FIFOReadyQueue
from SchedullingAndQueuesManager.IoWaitingQueue import IoWaitingQueue
from SchedullingAndQueuesManager.QueuesManager import QueuesManager
from SchedullingAndQueuesManager.WaitingQueue import WaitingQueue
from Shell.CommandHandler import CommandHandler
from Shell.Shell import Shell
from clases.Clock import Clock
from clases.Cpu import Cpu
from clases.Disk import Disk
from clases.Kernel import Kernel
from clases.ViewSo import ViewSo


memory=PhysicalMemoryContinuedAllocation(20)
routineBestFit = BestFit()
mmuContinuedAllocation=MMUContinuedAllocation(memory,routineBestFit)
        
colaReadyFifo = FIFOReadyQueue()
         
colaWaiting = WaitingQueue()
ioWaitingQueue =IoWaitingQueue() 
         
adminDeColasConcolaReadyFifo = QueuesManager(colaReadyFifo,colaWaiting,ioWaitingQueue)
        
politicaFifo = FIFO(adminDeColasConcolaReadyFifo)
       
        
irqHandler=IrqHandler(politicaFifo)
        
cpu=Cpu(mmuContinuedAllocation,irqHandler)

disk=Disk()
clock=Clock(cpu)
kernel=Kernel(cpu,disk,irqHandler,cpu)
commandHandler=CommandHandler()
shell=Shell(kernel,commandHandler)
        
window = Window()
scanner = Scanner()
printer = Printer()
        
instruction1=InstructionIO('hello',window)
instruction2=InstructionIO('hello',scanner)
instruction3=InstructionCpu('hello',window)
instruction4=InstructionIO('hello',printer)
instruction5=InstructionCpu('hello',window)
instruction6=InstructionCpu('hello',window)
        
program1 = Program('WordPad',instruction2,instruction1,instruction3)
disk.addProgram(program1)
        
program2 = Program('VirtualBox',instruction4,instruction1,instruction2,instruction5)
disk.addProgram(program2)
        
program3 = Program('Eclipse',instruction1,instruction2,instruction3,instruction4,instruction5,instruction6)
disk.addProgram(program3)

program4 = Program('Internet Explored',instruction1,instruction4,instruction6,instruction2,instruction3,instruction4,instruction5,instruction6)
disk.addProgram(program4)

program5 = Program('NotePad',instruction2,instruction1,instruction3)
disk.addProgram(program5)

def main():
    root = tk.Tk()
    view = ViewSo(master=root)
    view.setShell(shell)
    view.mainloop()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    main()
