from clases.IoResource import IoResource
from clases.Resource import Resource


class Printer(IoResource):
  

    def __init__(self):
        IoResource.__init__(self)
        
    
    def canHandle(self, resource):
        IoResource.canHandle(self, resource)
        return resource==Resource.printer
    
    def handle(self, resource):
        IoResource.handle(self, resource)
      
        