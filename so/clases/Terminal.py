import os
import re
from clases.Window import Window
from clases.Program import Program
from clases.Disk import Disk
from clases.Memory import Memory
from clases.Cpu import Cpu
from clases.MemoryManager import MemoryManager
from clases.Instruction import Instruction
from clases.WaitingQueue import WaitingQueue
from clases.QueuesManager import QueuesManager
from clases.Kernel import Kernel
from clases.ReadyQueuePriority import ReadyQueuePriority


class Terminal :
        def __init__(self,kernel):
            os.chdir("C:/")
            self.ubicacion = os.getcwd()
            self.kernel = kernel
            self.main()
            

        def main(self):
            self.ubicacion = os.getcwd()
            prompt = '> '
            promp = input (self.ubicacion + prompt)
            if (promp == "fin"):
                    self.finalizarTerminal()
            else:
                    self.ejecutarComand(promp)


        def finalizarTerminal(self):
            print ("se finalizo la terminal")

        def ejecutarComand(self,promp):
            if(self.esCD(promp) and os.path.exists(self.contenidoDeCd(promp))):
                os.chdir(self.contenidoDeCd(promp))
            elif(self.esLs(promp)):
                print (os.listdir(self.ubicacion))
            elif(self.esShow(promp)):
                print(open(self.contenidoDeShow(promp),"rb").read())
            elif(self.esLoad(promp)):
                self.kernel.loadProgram(self.contenido(promp))
            elif(self.esRun(promp)):
                self.kernel.runProgram(self.contenido(promp))
                self.main()
            else :
                print("error invalid command")

            self.main()

        def  esCD(self,promp):
            esCD = re.compile("cd")
            return esCD.match(promp)

        def  esLoad(self,promp):
            esCD = re.compile("load")
            return esCD.match(promp)

        def  esRun(self,promp):
            esCD = re.compile("run")
            return esCD.match(promp)

        def esLs(self,promp):
            esLs = re.compile("ls")
            return esLs.match(promp)

        def esShow(self,promp):
            esShow = re.compile("show")
            return esShow.match(promp)

        def contenidoDeCd(self,promp):
            return promp[3:100]

        def contenidoDeLoad(self,promp):
            return promp[5:100]

        def contenidoDeRun(self,promp):
            return promp[4:100]

        def contenidoDeShow(self,promp):
            return promp[5:100]


window=Window()
instruction=Instruction('hola',window)
program=Program('program',instruction)
disk=Disk()
disk.addProgram(program)
memory = Memory(20)
memoryManager = MemoryManager(memory)
cpu = Cpu(memory)
readyQueue = ReadyQueuePriority()
waitingQueue = WaitingQueue()
queuesManager = QueuesManager(readyQueue,waitingQueue)
kernel=Kernel(cpu,disk,memoryManager,queuesManager)
terminal = Terminal(kernel)