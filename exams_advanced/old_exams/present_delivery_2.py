def get_matrix_positions(n):
    m = []
    g_kids = []
    s_coord = []
    count_pres = 0
    for i in range(n):
        s_m = []
        rows = input().split()
        for j in range(n):
            s_m.append(rows[j])
            if rows[j] == "S":
                s_coord = [i, j]
            elif rows[j] == "V":
                g_kids.append("V")
                count_pres += 1
        m.append(s_m)
    return m, g_kids, s_coord, count_pres


def is_valid(n, p_r, p_c):
    return 0 <= p_r < n and 0 <= p_c < n


def get_cookie(mat, c, p_r, p_c, pres, nice_kids):
    for key, value in c.items():
        if pres == 0:
            return mat, p_r, p_c, pres, nice_kids
        r, c = value
        pot_row = r + p_r
        pot_col = c + p_c
        if is_valid(n, pot_row, pot_col) and not mat[pot_row][pot_col] == "-":
            if mat[pot_row][pot_col] == "V":
                nice_kids.pop()
            mat[pot_row][pot_col] = "-"
            pres -= 1
    return mat, p_r, p_c, pres, nice_kids


m = int(input())
n = int(input())
matrix, good_kids, santa_coordinate, count_presents = get_matrix_positions(n)
commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
command = input()

start_row, start_col = santa_coordinate
while not command == "Christmas morning":
    row, col = commands[command]
    potential_row = start_row + row
    potential_col = start_col + col
    if is_valid(n, potential_row, potential_col):
        if matrix[potential_row][potential_col] == "C":
            matrix[start_row][start_col] = "-"
            matrix[potential_row][potential_col] = "S"
            matrix, potential_row, potential_col, m, good_kids = get_cookie(matrix, commands, potential_row, potential_col, m, good_kids)
            if not m:
                break
            start_row, start_col = potential_row, potential_col
        elif matrix[potential_row][potential_col] == "V":
            matrix[start_row][start_col] = "-"
            matrix[potential_row][potential_col] = "S"
            start_row, start_col = potential_row, potential_col
            good_kids.pop()
            m -= 1
            if not m:
                break
        else:
            matrix[start_row][start_col] = "-"
            matrix[potential_row][potential_col] = "S"
            start_row, start_col = potential_row, potential_col
    command = input()

if not good_kids:
    print(*[" ".join(m) for m in matrix], sep="\n")
    print(f"Good job, Santa! {count_presents} happy nice kid/s.")
else:
    print("Santa ran out of presents!")
    print(*[" ".join(m) for m in matrix], sep="\n")
    print(f"No presents for {len(good_kids)} nice kid/s.")