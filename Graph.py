class Vertex:

    def __init__(self, value: int):
        self._value = value


class Edge:
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight: int):
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._weight = weight


class Graph(object):
    def __init__(self):
        self._vertices: list = list()
        self._edges:list = list()
        self._adjacency_list: dict = dict()
        self._adjacency_matrix: list = list()
        self._counter = 0

    def add_vertex(self):
        self._vertices.append(Vertex(self.counter))
        self._counter += 1
        self._adjacency_list[vertex] = list()
        self.add_vertex_to_adjacency_matrix()

    def add_edge(self, edge: Edge):
        self._edges.append(edge)
        self.add_edge_to_adjacency_matrix(edge)
        self._adjacency_list[edge.vertex1.value].append(edge.vertex2.value)
        self._adjacency_list[edge.vertex2.value].append(edge.vertex1.value)

    def add_edge_to_adjacency_matrix(self, edge: Edge):
        self.adjacency_matrix[edge.vertex1.value][edge.vertex2.value] = edge.weight
        self.adjacency_matrix[edge.vertex2.value][edge.vertex1.value] = edge.weight

    def add_vertex_to_adjacency_matrix(self):
        # Add new row for new Vertex
        self.adjacency_matrix.append(list())

        # Add new column for new Vertex
        for r in self.adjacency_matrix:
            r.append(0)

    @property
    def counter(self) -> int:
        return self._counter

    @property
    def vertices(self) -> list:
        return self._vertices

    @property
    def edges(self):
        return self._edges

    @staticmethod
    def _create_vertex(value: int) -> Vertex:
        return Vertex(value)

