class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Cycle detected

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)

    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# Example usage
vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('B', 'D', 3),
    ('C', 'D', 4),
    ('A', 'D', 5),
]

mst_edges, total = kruskal(vertices, edges)

print("Edges in MST:")
for u, v, w in mst_edges:
    print(f"{u} -- {v} == {w}")

print("Total weight of MST:", total)