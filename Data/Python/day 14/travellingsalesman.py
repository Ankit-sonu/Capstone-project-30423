from itertools import permutations


def tsp_brute_force(dist_matrix):
    cities = list(range(len(dist_matrix)))
    min_path = None
    min_cost = float('inf')

    for perm in permutations(cities[1:]):
        path = [0] + list(perm) + [0]
        cost = sum(dist_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

        if cost < min_cost:
            min_cost = cost
            min_path = path

    city_names = ['A', 'B', 'C', 'D']
    path_names = [city_names[i] for i in min_path]

    print("Minimum Cost Path:", ' → '.join(path_names))
    print("Total Cost:", min_cost)


distances = [
    [10, 0, 15, 0],
    [10, 20, 35, 25],
    [5, 35, 0, 30],
    [20, 25, 40, 0]
]

tsp_brute_force(distances)