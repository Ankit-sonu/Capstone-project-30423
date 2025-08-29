def is_safe(x, y, maze, visited, N):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1 and not visited[x][y]

def solve_maze_util(x, y, maze, visited, path, all_paths, N):
    # If destination is reached
    if x == N - 1 and y == N - 1:
        all_paths.append(path)
        return

    # Direction vectors
    directions = ['D', 'L', 'R', 'U']
    row_change = [1, 0, 0, -1]
    col_change = [0, -1, 1, 0]

    for i in range(4):
        next_x = x + row_change[i]
        next_y = y + col_change[i]
        if is_safe(next_x, next_y, maze, visited, N):
            visited[next_x][next_y] = True
            solve_maze_util(next_x, next_y, maze, visited, path + directions[i], all_paths, N)
            visited[next_x][next_y] = False  # Backtrack

def find_paths(maze):
    N = len(maze)
    visited = [[False for _ in range(N)] for _ in range(N)]
    all_paths = []

    if maze[0][0] == 0:
        return []  # Start is blocked

    visited[0][0] = True
    solve_maze_util(0, 0, maze, visited, "", all_paths, N)
    return all_paths

# 🔁 Example usage
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

paths = find_paths(maze)
print("All possible paths:")
for p in paths:
    print(p)

# D R D D R R