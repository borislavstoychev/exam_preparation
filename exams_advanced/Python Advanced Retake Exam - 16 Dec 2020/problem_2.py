def get_matrix(matrix, n):
    position = []
    for index in range(n):
        row = input()
        for col in range(n):
            if not row[col] == "-":
                matrix[index][col] = row[col]
                if row[col] == "P":
                    position = [index, col]
    return matrix, position


def next_cells_move(position, move):
    x = position[0] + move[0]
    y = position[1] + move[1]
    return x, y


def is_valid(matrix, coordinate):
    x, y = coordinate
    return 0 <= x < len(matrix) and 0 <= y < len(matrix)


initial_string = input()
n = int(input())
matrix = [["-"]*n for row in range(n)]
commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
matrix, current_position = get_matrix(matrix, n)
for _ in range(int(input())):
    command = input()
    move_coordinate = commands[command]
    next_cell = next_cells_move(current_position, move_coordinate)
    if is_valid(matrix, next_cell):
        pos_x, pos_y = current_position
        x, y = next_cell
        if not matrix[x][y] == "-":
            initial_string += matrix[x][y]
        current_position = next_cell
        matrix[pos_x][pos_y] = "-"
        matrix[x][y] = "P"
    else:
        initial_string = initial_string[:-1]
print(initial_string)
print(*["".join(m) for m in matrix], sep="\n")

