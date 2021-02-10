def get_bunny_position(matrix):
    start = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "B":
                start = [i, j]
            elif matrix[i][j].isdigit():
                matrix[i][j] = int(matrix[i][j])
    return matrix, start


def is_valid(matrix, pot_row, pot_col):
    return 0 <= pot_row < len(matrix) and 0 <= pot_col < len(matrix) and matrix[pot_row][pot_col] != "X"


def all_valid_moves(matrix, m, move,  cord, move_coord):
    start_row, start_col = cord
    if move == "up":
        for i in range(1, len(matrix) + 1):
            potential_row = start_row - i
            potential_col = start_col
            if is_valid(matrix, potential_row, potential_col):
                m[move] += matrix[potential_row][potential_col]
                move_coord[move].append([potential_row, potential_col])
            else:
                return m, move_coord
    elif move == "down":
        for i in range(1, len(matrix) + 1):
            potential_row = start_row + i
            potential_col = start_col
            if is_valid(matrix, potential_row, potential_col):
                m[move] += matrix[potential_row][potential_col]
                move_coord[move].append([potential_row, potential_col])
            else:
                return m, move_coord
    elif move == "left":
        for i in range(1, len(matrix) + 1):
            potential_row = start_row
            potential_col = start_col - i
            if is_valid(matrix, potential_row, potential_col):
                m[move] += matrix[potential_row][potential_col]
                move_coord[move].append([potential_row, potential_col])
            else:
                return m, move_coord
    elif move == "right":
        for i in range(1, len(matrix) + 1):
            potential_row = start_row
            potential_col = start_col + i
            if is_valid(matrix, potential_row, potential_col):
                m[move] += matrix[potential_row][potential_col]
                move_coord[move].append([potential_row, potential_col])
            else:
                return m, move_coord


def best_move(m, f,):
    for move in m:
        all_valid_moves(f, m, move, coordinate, moves_coordinates)
    for key, value in dict(sorted(m.items(), key=lambda el: -el[1])).items():
        return key, value


field = [[col for col in input().split()]for _ in range(int(input()))]
moves = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0
}
moves_coordinates = {
    "up": [],
    "down": [],
    "left": [],
    "right": []
}
field, coordinate = get_bunny_position(field)
best_of_moves, total = best_move(moves, field)
print(best_of_moves)
print(*moves_coordinates[best_of_moves], sep="\n")
print(total)