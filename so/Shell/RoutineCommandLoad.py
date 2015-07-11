from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandLoad(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.load.value 
    
    def handle(self,command,param= None ,shell=None,kernel=None,file= None):
        RoutineCommand.handle(self, command,shell,kernel,file)
        param=str(param)
        return kernel.loadProgram(param)