'''
Created on 13/05/2015

@author: apiorno
'''
class Window:
    
    def __init__(self):
        self.content=[]
        
    def show(self,item):
        self.put(item)
        print (item)
    
    def put(self,item):
        self.content.append(item)
        
    def getCantContents(self):
        return self.content.__len__()
    
    def get(self,index):
        return self.content[index]