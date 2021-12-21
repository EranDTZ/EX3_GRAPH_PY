from Nodes import Nodes
from Edges import Edges
from GraphInterface import GraphInterface



class DirectedWeightedGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.edgeID = 0


        def v_size(self) -> int:
            return self.nodes.__sizeof__()


        def e_size(self) -> int:
            return len(self.edges)


        def get_all_v(self) -> dict:
            """return a dictionary of all the nodes in the Graph, each node is represented using a pair
             (node_id, node_data)
            """


        def all_in_edges_of_node(self, id1: int) -> dict:
            """return a dictionary of all the nodes connected to (into) node_id ,
            each node is represented using a pair (other_node_id, weight)
             """


        def all_out_edges_of_node(self, id1: int) -> dict:
            """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
            (other_node_id, weight)
            """


        def get_mc(self) -> int:
            """
            Returns the current version of this graph,
            on every change in the graph state - the MC should be increased
            @return: The current version of this graph.
            """
            raise NotImplementedError


        def add_edge(self, id1: int, id2: int, weight: float) -> bool:
            self.edges[self.edgeID] = Edges(id1,id2,weight)
            self.edgeID = self.edgeID+1
            self.nodes[id2].inEdges.add(Edges(id1,id2,weight))
            self.nodes[id2].outEdges.add(Edges(id1,id2,weight))
            """
            Adds an edge to the graph.
            @param id1: The start node of the edge
            @param id2: The end node of the edge
            @param weight: The weight of the edge
            @return: True if the edge was added successfully, False o.w.
            Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
            """
            raise NotImplementedError


        def add_node(self, node_id: int, pos: tuple = None) -> bool:
            try:
                self.nodes[node_id] = Nodes(node_id,pos)
                return true
            except:
                print("Error")
                return false


        def remove_node(self, node_id: int) -> bool:
            """
            Removes a node from the graph.
            @param node_id: The node ID
            @return: True if the node was removed successfully, False o.w.
            Note: if the node id does not exists the function will do nothing
            """
            raise NotImplementedError


        def remove_edge(self, node_id1: int, node_id2: int) -> bool:
            """
            Removes an edge from the graph.
            @param node_id1: The start node of the edge
            @param node_id2: The end node of the edge
            @return: True if the edge was removed successfully, False o.w.
            Note: If such an edge does not exists the function will do nothing
            """
            raise NotImplementedError

