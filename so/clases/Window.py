from clases.IoResource import IoResource
from clases.Resource import Resource


class Window(IoResource):
    
    def __init__(self):
        IoResource.__init__(self)
        
    def show(self,item):
        self.put(item)
        print (item)
    
    def put(self,item):
        self.content.append(item)
        
    def getCantContents(self):
        return self.content.__len__()
    
    def get(self,index):
        return self.content[index]
    
    def canHandle(self, resource):
        IoResource.canHandle(self, resource)
        return resource==Resource.window
    def handle(self, resource):
        IoResource.handle(self, resource)
        