class ResourceManager:
    
    
    def __init__(self):
        self.ioResources=[] 
        
    def addResource(self,resourceIo):
        self.resources.append(resourceIo)
        
    def receiveResource(self,resource):
        self.anyHandle(resource)
        
    def anyHandle(self,resource):
        for res in self.ioResources:
            if(res.canHandle(resource)):
                res.handle(resource)
                