N = 5  # Size of chessboard

# All 8 possible movements for a knight
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def print_solution(board):
    for row in board:
        print(" ".join(str(cell).rjust(2) for cell in row))

def solve_knight_tour():
    # Initialization of the board
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Starting position
    board[0][0] = 0

    # Start recursive solving
    if not knight_tour_util(0, 0, 1, board):
        print("No solution exists.")
    else:
        print("Knight’s Tour Path:")
        print_solution(board)

def knight_tour_util(x, y, movei, board):
    if movei == N * N:
        return True

    for k in range(8):
        next_x = x + move_x[k]
        next_y = y + move_y[k]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = movei
            if knight_tour_util(next_x, next_y, movei + 1, board):
                return True
            board[next_x][next_y] = -1  # Backtrack

    return False

# Run the program
solve_knight_tour()