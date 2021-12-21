
from GraphAlgoInterface import GraphAlgoInterface
from Nodes import Nodes
import json


def load_from_json(self, file_name: str) -> bool:
    try:
        jsonO = open(file_name)
        data = json.load(jsonO)
        nodes = data["Nodes"]
        edges = data["Edges"]
        for node in nodes:
            self.graph.add_node(node["id"])

            print(ev)
        for edge in edges:
            self.graph.add_edge(edge["src"], edge["dest"], edge["w"])
        return True
    except:
        print("file name wrong")
        return False