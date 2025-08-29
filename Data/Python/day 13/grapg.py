class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            print(f"Vertex -> {vertex} added successfully")
        else:
            print(f"Vertex -> {vertex} already exists")

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            print(f"Vertex -> {vertex1} does not exist")
            return
        if vertex2 not in self.graph:
            print(f"Vertex -> {vertex2} does not exist")
            return

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
        print(f"Edge added between {vertex1} -> {vertex2}")



    def display(self):
        print(" Graph display - Adjacency Matrix " )
        for vertex in self.graph:
            print(f"{vertex} -->  {self.graph[vertex]}")


    def dfs_iterations(self,start):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end = " ")
                visited.add(vertex)
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

    def bfs_iterations(self, start):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end = " ")
                visited.add(vertex)
                queue.extend(n for n in self.graph.get(vertex, []) if n not in visited )

if __name__ == '__main__':
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')

    g.add_edge('A', 'B')
    g.add_edge('A', 'D')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
   # g.add_edge('B', 'A')
   # g.add_edge('D', 'A')
   #g.add_edge('C', 'B')
    g.display()
    print("The Depth first search traversal are:")
    g.dfs_iterations('A')
    print("\n")

    print("The Breadth first search traversal are:")
    g.bfs_iterations('A')