def is_valid(n, pot_row, pot_col):
    return 0 <= pot_row < n and 0 <= pot_col < n


def get_matrix_positions(n, matrix):
    position = []
    barrow = []
    for i in range(n):
        row = input()
        for j in range(n):
            if not row[j] == "-":
                matrix[i][j] = row[j]
                if row[j] == "S":
                    position = [i, j]
                elif row[j] == "B":
                    barrow.append([i, j])
    return matrix, position, barrow


n = int(input())
matrix = [n * ["-"] for m in range(n)]
matrix, start_position, barrows = get_matrix_positions(n, matrix)
commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
is_out = False
eaten_food = 0
while eaten_food < 10:
    command = input()
    start_row, start_col = start_position
    new_row, new_col = commands[command]
    potential_row = start_row + new_row
    potential_col = start_col + new_col
    if is_valid(n, potential_row, potential_col):
        if matrix[potential_row][potential_col] == "*":
            eaten_food += 1
        elif matrix[potential_row][potential_col] == "B":
            barrows.pop(barrows.index([potential_row, potential_col]))
            matrix[start_row][start_col] = "."
            matrix[potential_row][potential_col] = "."
            start_position = barrows[0]
            matrix[barrows[0][0]][barrows[0][1]] = "S"
            continue
        matrix[start_row][start_col] = "."
        matrix[potential_row][potential_col] = "S"
        start_position = [potential_row, potential_col]
    else:
        matrix[start_row][start_col] = "."
        is_out = True
        break
if is_out:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {eaten_food}")
print(*["".join(m) for m in matrix], sep="\n")
