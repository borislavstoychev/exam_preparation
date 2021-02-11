def get_matrix_positions(n):
    m = []
    t_list = []
    p_coord = []
    cou_targets = 0
    for i in range(n):
        s_m = []
        rows = input().split()
        for j in range(n):
            s_m.append(rows[j])
            if rows[j] == "p":
                p_coord = [i, j]
            elif rows[j] == "t":
                t_list.append("t")
                cou_targets += 1
        m.append(s_m)
    return m, t_list, p_coord, cou_targets


def is_valid(n, p_r, p_c):
    return 0 <= p_r < n and 0 <= p_c < n


def up(p, p_c):
    s_r, s_c = p_c
    pot_row = s_r - p
    pot_col = s_c
    if is_valid(n, pot_row, pot_col):
        return pot_row, pot_col


def down(p, p_c):
    s_r, s_c = p_c
    pot_row = s_r + p
    pot_col = s_c
    if is_valid(n, pot_row, pot_col):
        return pot_row, pot_col


def left(p, p_c):
    s_r, s_c = p_c
    pot_row = s_r
    pot_col = s_c - p
    if is_valid(n, pot_row, pot_col):
        return pot_row, pot_col


def right(p, p_c):
    s_r, s_c = p_c
    pot_row = s_r
    pot_col = s_c + p
    if is_valid(n, pot_row, pot_col):
        return pot_row, pot_col


n = int(input())
matrix, targets, planet_coordinate, count_targets = get_matrix_positions(n)
moves_shoots = {
        'up': up,
        'down': down,
        'left': left,
        'right': right
    }
for _ in range(int(input())):
    command, side, power = input().split()
    power = int(power)
    if command == "move":
        try:
            potential_row, potential_col = moves_shoots[side](power, planet_coordinate)
            if matrix[potential_row][potential_col] == ".":
                matrix[potential_row][potential_col] = "p"
                start_row, start_col = planet_coordinate
                matrix[start_row][start_col] = "."
                planet_coordinate = [potential_row, potential_col]
        except TypeError:
            continue
    elif command == "shoot":
        try:
            potential_row, potential_col = moves_shoots[side](power, planet_coordinate)
            if matrix[potential_row][potential_col] == "t":
                count_targets -= 1
            matrix[potential_row][potential_col] = "x"
        except TypeError:
            continue


if not count_targets:
    print(f"Mission accomplished! All {len(targets)} targets destroyed.")
else:
    print(f"Mission failed! {count_targets} targets left.")
print(*[" ".join(m) for m in matrix], sep="\n")