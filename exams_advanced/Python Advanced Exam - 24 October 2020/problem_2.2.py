def is_valid(matrix, n_r, n_c):
    return 0 <= n_r < len(matrix) and 0 <= n_c < len(matrix[0]) and matrix[n_r][n_c] == "Q"


def move_left_right(matrix, r, c, list_q):
    rows = r
    # cols = [1, 2, 3, 4, 5, 6, 7][-1, -2, -3, -4, -5, -6, -7]
    for i in range(1, len(matrix) + 1):
        potential_row = rows
        potential_col = c + i
        if is_valid(matrix, potential_row, potential_col):
            list_q.append([potential_row, potential_col])
            break
    for i in range(1, len(matrix)):
        potential_row = rows
        potential_col = c - i
        if is_valid(matrix, potential_row, potential_col):
            list_q.append([potential_row, potential_col])
            break
    return list_q


def move_up_down(matrix, r, c, list_q):
    # rows = [-1, -2, -3, -4, -5, -6, -7][1, 2, 3, 4, 5, 6, 7]
    cols = c
    for i in range(1, len(matrix) + 1):
        potential_row = r + i
        potential_cow = cols
        if is_valid(matrix, potential_row, potential_cow):
            list_q.append([potential_row, potential_cow])
            break
    for i in range(1, len(matrix) + 1):
        potential_row = r - i
        potential_cow = cols
        if is_valid(matrix, potential_row, potential_cow):
            list_q.append([potential_row, potential_cow])
            break
    return list_q


def first_diagonal(matrix, r, c, list_q):
    # rows = [1, 2, 3, 4, 5, 6, 7][-1, -2, -3, -4, -5, -6, -7]
    # cols = [1, 2, 3, 4, 5, 6, 7][-1, -2, -3, -4, -5, -6, -7]
    for i in range(len(matrix)):
        potential_row = r + i
        potential_col = c + i
        if is_valid(matrix, potential_row, potential_col):
            list_q.append([potential_row, potential_col])
            break
    for i in range(len(matrix)):
        potential_row = r - i
        potential_col = c - i
        if is_valid(matrix, potential_row, potential_col):
            list_q.append([potential_row, potential_col])
            break
    return list_q


def second_diagonal(matrix, r, c, list_q):
    # rows = [-1, -2, -3, -4, -5, -6, -7][1, 2, 3, 4, 5, 6, 7]
    # cols = [1, 2, 3, 4, 5, 6, 7][-1, -2, -3, -4, -5, -6, -7]
    for i in range(len(matrix)):
        potential_row = r - i
        potential_col = c + i
        if is_valid(matrix, potential_row, potential_col):
            list_q.append([potential_row, potential_col])
            break
    for i in range(len(matrix)):
        potential_row = r + i
        potential_col = c - i
        if is_valid(matrix, potential_row, potential_col):
            list_q.append([potential_row, potential_col])
            break
    return list_q


def searching_the_king(matrix):
    list_q = []
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "K":
                move_up_down(matrix, r, c, list_q)
                move_left_right(matrix, r, c, list_q)
                second_diagonal(matrix, r, c, list_q)
                first_diagonal(matrix, r, c, list_q)
    return list_q


matrix = [[m for m in input().split()] for _ in range(8)]
result = searching_the_king(matrix)
if result:
    print(*result, sep="\n")
else:
    print("The king is safe!")