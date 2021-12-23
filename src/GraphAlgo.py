
from face.GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
import json


class GraphAlgo:
    
    def __init__(self):
        self.graph = DiGraph()

    def get_graph(self) -> DiGraph:
        return self.graph
        """
        :return: the directed graph on which the algorithm works on.
        """

def load_from_json(self, file_name: str) -> bool:
    try:
        jsonload = open(file_name)
        data = jsonload.load(jsonO)
        nodes = data["Nodes"]
        edges = data["Edges"]
        for i in nodes:
            self.graph.add_node(i["id"],i["pos"])
        for j in edges:
            self.graph.add_edge(j["src"], j["dest"], j["w"])
        return True
    except:
        print("Error")
        return False

        """
                Loads a graph from a json file.
                @param file_name: The path to the json file
                @returns True if the loading was successful, False o.w.
                """
        raise NotImplementedError

        def save_to_json(self, file_name: str) -> bool:
            """
            Saves the graph in JSON format to a file
            @param file_name: The path to the out file
            @return: True if the save was successful, False o.w.
            """
            raise NotImplementedError

        def shortest_path(self, id1: int, id2: int) -> (float, list):
            D = {v: float('inf') for v in range(graph.v)}
            D[id1] = 0

            current_vertex = id1

            pq = PriorityQueue()
            pq.put((0, start_vertex))

            while not pq.empty():
                (dist, current_vertex) = pq.get()
                graph.nodes.get(current_vertex).setag(1)
                for neighbor in range(graph.nodes):
                    if graph.nodes.get(current_vertex).getag() == 0:
                        distance = graph.nodes.get(current_vertex).inEdges.get(neighbor)
                        if neighbor not in graph.nodes:
                            old_cost = D[neighbor]
                            new_cost = D[current_vertex] + distance
                            if new_cost < old_cost:
                                pq.put((new_cost, neighbor))
                                D[neighbor] = new_cost
            return D
            """
            Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
            @param id1: The start node id
            @param id2: The end node id
            @return: The distance of the path, a list of the nodes ids that the path goes through
            Example:
    #      >>> from GraphAlgo import GraphAlgo
    #       >>> g_algo = GraphAlgo()
    #        >>> g_algo.addNode(0)
    #        >>> g_algo.addNode(1)
    #        >>> g_algo.addNode(2)
    #        >>> g_algo.addEdge(0,1,1)
    #        >>> g_algo.addEdge(1,2,4)
    #        >>> g_algo.shortestPath(0,1)
    #        (1, [0, 1])
    #        >>> g_algo.shortestPath(0,2)
    #        (5, [0, 1, 2])
            Notes:
            If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
            More info:
            https://en.wikipedia.org/wiki/Dijkstra's_algorithm
            """
            raise NotImplementedError

        def TSP(self, node_lst: List[int]) -> (List[int], float):
            """
            Finds the shortest path that visits all the nodes in the list
            :param node_lst: A list of nodes id's
            :return: A list of the nodes id's in the path, and the overall distance
            """

        def centerPoint(self) -> (int, float):
            """
            Finds the node that has the shortest distance to it's farthest node.
            :return: The nodes id, min-maximum distance
            """

        def plot_graph(self) -> None:
            """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            @return: None
            """
            raise NotImplementedError
