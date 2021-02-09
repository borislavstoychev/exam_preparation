def is_valid(matrix, r, c):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)


def explosion(matrix, r, c):
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if is_valid(matrix, i, j) and not matrix[i][j] == "*":
                matrix[i][j] += 1
    return matrix


def get_bombs_matrix():
    n = int(input())
    matrix = [n * [0] for i in range(n)]
    for _ in range(int(input())):
        coordinate = input().strip("()")
        row, col = coordinate.split(", ")
        row = int(row)
        col = int(col)
        matrix[row][col] = "*"
        explosion(matrix, row, col)
    return matrix


def get_print():
    matrix = get_bombs_matrix()
    for m in matrix:
        print(*m, sep=" ")


get_print()


