from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandShow(RoutineCommand):
    

    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.show.value 
    
    def handle(self,param=None, command,shell,kernel,file =None):
        RoutineCommand.handle(self, command)
        shell.showData(open(file,"rb").read())
        