import os
import re

from clases.FIFO import FIFO
from clases.IrqHandler import IrqHandler
from clases.Cpu import Cpu
from clases.Disk import Disk
from clases.Instruction import Instruction
from clases.Kernel import Kernel
from clases.PhysicalMemory import PhysicalMemory
from clases.MemoryManager import MemoryManager
from clases.Program import Program
from clases.QueuesManager import QueuesManager
from clases.ReadyQueuePriority import ReadyQueuePriority
from clases.WaitingQueue import WaitingQueue
from clases.Window import Window
from clases.IoWaitingQueue import IoWaitingQueue
from logging import NullHandler
import logging


class Terminal :
        def __init__(self,kernel):
            os.chdir("C:/")
            self.ubicacion = os.getcwd()
            self.kernel = kernel
            self.usser = NullHandler
            self.usuarios = {}
            self.usuarios["fede"] = "fede"
            self.main()
            
            

        def main(self):
            self.ubicacion = os.getcwd()
            if(self.estaLogeado()):
                self.arrancarSo()
            else:
                self.loggin()
                self.main()

        
        def arrancarSo(self):
            prompt = '>'
            promp = input (self.ubicacion + prompt)
            
            if (promp == "fin"):
                self.finalizarTerminal()
            else:
                self.ejecutarComand(promp)
            
        def estaLogeado(self):
            return self.usser != NullHandler
        
        def loggin(self):
            prompt = 'usuario:'
            prompt = input(prompt)
            nombreUsuario = self.logginDe(prompt)
            prompt = 'password:'
            prompt = input(prompt)
            passDeUsuario = self.logginDe(prompt)
            self.verificarUsuarioYPassword(nombreUsuario,passDeUsuario)

        def finalizarTerminal(self):
            print ("se finalizo la terminal")
            
        def verificarUsuarioYPassword(self,usuario,password):
            if(self.usuarios.get(usuario) == password):
                print ("bienvenido")
                self.usser = usuario
                self.arrancarSo()
            else:
                print("Usuario o Contrasenia incorrecta")
                self.main()

        def ejecutarComand(self,promp):
            if(self.esCD(promp) and os.path.exists(self.contenidoDeCd(promp))):
                os.chdir(self.contenidoDeCd(promp))
            elif(self.esLs(promp)):
                print (os.listdir(self.ubicacion))
            elif(self.esShow(promp)):
                print(open(self.contenidoDeShow(promp),"rb").read())
            elif(self.esLoad(promp)):
                self.kernel.loadProgram(self.contenidoDeLoad(promp))
            elif(self.esRun(promp)):
                self.kernel.runProgram(self.contenidoDeRun(promp))
                self.main()
            else :
                print("error invalid command")

            self.main()

        def  esCD(self,promp):
            esCD = re.compile("cd  ")
            return esCD.match(promp)

        def  esLoad(self,promp):
            esCD = re.compile("load")
            return esCD.match(promp)

        def  esRun(self,promp):
            esCD = re.compile("run ")
            return esCD.match(promp)

        def esLs(self,promp):
            esLs = re.compile("ls")
            return esLs.match(promp)

        def esShow(self,promp):
            esShow = re.compile("show")
            return esShow.match(promp)

        def contenidoDeCd(self,promp):
            return promp[5:100]

        def contenidoDeLoad(self,promp):
            return promp[5:100]

        def contenidoDeRun(self,promp):
            return promp[4:100]

        def contenidoDeShow(self,promp):
            return promp[5:100]
        
        def logginDe(self,promp):
            return promp[0:100]


window=Window()
instruction=Instruction('hola11111',window)
program=Program('program',instruction)
program1=Program('program1',instruction)
program2=Program('program2',instruction)
program3=Program('program3',instruction)
program4=Program('program4',instruction)
disk=Disk()
disk.addProgram(program)
disk.addProgram(program1)
disk.addProgram(program2)
disk.addProgram(program3)
disk.addProgram(program4)
memory = PhysicalMemory(200)
memoryManager = MemoryManager(memory)
ioWaitingQueue = IoWaitingQueue()
readyQueue = ReadyQueuePriority()
waitingQueue = WaitingQueue()
queuesManager = QueuesManager(readyQueue,waitingQueue,ioWaitingQueue)
politicaFIFO = FIFO(queuesManager)
irqHandler = IrqHandler(politicaFIFO)
cpu = Cpu(memoryManager,irqHandler)
kernel=Kernel(cpu,disk,memoryManager,queuesManager)
terminal = Terminal(kernel)