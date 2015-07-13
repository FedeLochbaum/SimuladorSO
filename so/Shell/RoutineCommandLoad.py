from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandLoad(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.load.value 
    
    def handle(self,command,param= None ,shell=None,file= None):
        RoutineCommand.handle(self, command,shell,file)
        param=str(param)
        print("llegue")
        return shell.getKernel().loadProgram(param)
        