def get_magic_triangle(n):
    matrix = [[1], [1, 1]]
    for row in range(2, int(n)):
        sub_matrix = []
        for col in range(row + 1):
            upper_row = matrix[row - 1]
            left_number = get_upper_left(upper_row, col)
            right_number = get_upper_right(upper_row, col)
            sub_matrix.append(left_number + right_number)
        matrix.append(sub_matrix)
    return matrix


def get_upper_left(arr, index):
    if index == 0:
        return 0
    return arr[index - 1]


def get_upper_right(arr, index):
    if index >= len(arr):
        return 0
    return arr[index]


print(get_magic_triangle(5))

