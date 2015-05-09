class DirectedGraph:

    def __init__(self):
        self.graph = {}
        self.neighbours = []
        self.visited = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph.keys():
            self.neighbours = []
            self.neighbours.append(node_b)
            self.graph[node_a] = self.neighbours
        else:
            self.neighbours = self.graph[node_a]
            if node_b in self.neighbours:
                pass
            else:
                self.neighbours = self.graph[node_a]
                self.neighbours.append(node_b)
                self.graph[node_a] = self.neighbours

    def get_neighbours_for(self, node):
        neighbours_count = 0
        if node in self.graph:
            for neighbour in self.graph[node]:
                neighbours_count += 1
            for nodes in self.graph:
                if node in self.graph[nodes] and nodes not in self.graph[node]:
                    neighbours_count += 1
        return neighbours_count

    def path_between(self, node_a, node_b):
        if node_a not in self.graph:
            self.visited = []
            return False
        if node_b in self.graph[node_a]:
            self.visited = []
            return True
        else:
            self.visited.append(node_a)
            for node in self.graph[node_a]:
                if node in self.graph and node not in self.visited:
                    return self.path_between(node, node_b)
            else:
                self.visited = []
                return False

    def get_graph_dict(self):
        return self.graph


def main():
    g = DirectedGraph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "D")
    g.add_edge("A", "G")
    g.add_edge('A', 'B')
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge('B', 'C')
    g.add_edge('B', 'G')
    g.add_edge('B', 'N')
    g.add_edge('Z', 'A')
    g.add_edge('B', 'A')
    g.add_edge('B', 'M')
    g.add_edge('B', 'F')
    g.add_edge('B', 'Q')
    g.add_edge('B', 'Z')
    print(g.path_between('A', 'F'))
    print(g.get_neighbours_for("B"))
    print(g.get_graph_dict())
    print(g.path_between("A", "Z"))
    print(g.path_between("G", "Q"))

if __name__ == '__main__':
    main()
