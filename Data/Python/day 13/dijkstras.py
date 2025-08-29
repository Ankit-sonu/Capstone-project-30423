import heapq


class Dijkstras:
    def dijkstraalgorithm(self, graph, start):
        distances = {vertex : float('inf') for vertex in graph}
        distances[start] = 0

        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances


if __name__ == "__main__":
    dijkstras = Dijkstras()
    graph = {
        'A': [('B',2), ('C',1)],
        'B' :[('A',2), ('D',3)],
        'C':[('A',1), ('D',4)],
        'D':[('B',3), ('C',4)]
    }

    source = 'B'
    shortest_paths = dijkstras.dijkstraalgorithm(graph, source)

    print("The Shortest Paths from the given source")
    for node in shortest_paths:
        print(f"{source} --> {node} = {shortest_paths[node]}")