from GeoLocation import GeoLocation


class Nodes:

    def __init__(self,pos : {},id : int):
        self.pos = pos
        self.id = id;
        self.tag = 0;
        self.inEdges = {}
        self.outEdges ={}
        
    def setag(self,tag : int):
        self.tag = tag
        
    def getag(self):
        return self.tag

