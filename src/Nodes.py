from GeoLocation import GeoLocation


class Nodes:

    def __init__(self,pos : {},id : int):
        self.pos = pos
        self.id = id;
        self.inEdges = {}
        self.outEdges ={}


