from IO.IoResource import IoResource
from IO.Resource import Resource


class Scanner(IoResource):
  

    def __init__(self):
        IoResource.__init__(self)
        
    
    def canHandle(self, resource):
        IoResource.canHandle(self, resource)
        return resource==Resource.scanner
    
    def handle(self, resource):
        IoResource.handle(self, resource)