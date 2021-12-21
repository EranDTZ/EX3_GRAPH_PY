from GeoLocation import GeoLocation


class Nodes:

    def __init__(self,pos,id : int):
        self.pos = pos
        "??"
        "need to read json for GeoLocation pos"
        self.id = id;
        self.inEdges = {}
        self.outEdges ={}

