from clases.IoResource import IoResource
from clases.Resource import Resource


class Window(IoResource):
    
    def __init__(self):
        IoResource.__init__(self)
        
    def show(self,item):
        print (item)
    
    def put(self,item):
        self.content.append(item)
        
    def getCantContents(self):
        return self.ioWaitingQueue._qsize()
    
    def get(self,index):
        return self.content[index]
    
    def canHandle(self, resource):
        IoResource.canHandle(self, resource)
        return resource==Resource.window
    def handle(self, resource):
        IoResource.handle(self, resource)
        