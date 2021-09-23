# Instance of Graph, Vertex, open
# Methods: add_node, add_edge, get_nodes, get_neighbors, size
# from typing_extensions import ParamSpecKwargs


class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """
        add node
        Arguments: value
        Returns: The added node
        Add a node to the graph
        """
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """
        add edges
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        """
        if start_vertex not in self._adjacency_list:
            raise KeyError("Starting Vertex not in Graph")
        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not in Graph")

        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_nodes(self):
        """
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        """
        if self._adjacency_list == {}:
            return None
        else:
            nodes = [*self._adjacency_list]
            print(nodes)

            for i in range(len(nodes)):
                nodes[i] = nodes[i].value

            return nodes

    def get_neighbors(self, node):
        """
        Arguments: node
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        """
        nodes = [*self._adjacency_list]
        print(nodes)

        for i in range(len(nodes)):
            if nodes[i].value == node:
                adjacencies = self._adjacency_list[nodes[i]]
                print(adjacencies)

                adjacencies_with_weight = [
                    adjacencies[i].vertex.value,
                    adjacencies[i].weight,
                ]

                return adjacencies_with_weight
            else:
                raise KeyError("Null")

    def size(self):
        """
        size
        Arguments: none
        Returns the total number of nodes in the graph
        """
        return len(self._adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
