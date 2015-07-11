from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandLoad(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.load.value 
    
    def handle(self,param =None, command,shell,kernel,file =None):
        RoutineCommand.handle(self, command)
        param=str(param)
        return kernel.loadProgram(param)