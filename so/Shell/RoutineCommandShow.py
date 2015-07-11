from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandShow(RoutineCommand):
    

    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.show.value 
    
    def handle(self,command,param=None ,shell=None,kernel=None,file= None):
        RoutineCommand.handle(self, command,shell,kernel,file)
        shell.showData(open(file,"rb").read())
        