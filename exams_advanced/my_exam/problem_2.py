def get_positions(field):
    play_pos = []
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == "P":
                play_pos = [i, j]
            elif field[i][j].isdigit():
                field[i][j] = int(field[i][j])
    return field, play_pos


def is_valid(matrix, pot_r, pot_c):
    return 0 <= pot_r < len(matrix) and 0 <= pot_c < len(matrix) and not matrix[pot_r][pot_c] == "X"


def player_result(matrix, all_moves, player_pos):
    score = 0
    position_take = []
    while True:
        row, col = player_pos
        move = input()
        if move in all_moves:
            new_row, new_col = all_moves[move]
            pot_row, pot_col = row + new_row, col + new_col
            if is_valid(matrix, pot_row, pot_col):
                score += matrix[pot_row][pot_col]
                matrix[pot_row][pot_col] = 0
                position_take.append([pot_row, pot_col])
                player_pos = [pot_row, pot_col]
                if score >= 100:
                    is_loss = False
                    break
            else:
                is_loss = True
                break
    print_result(is_loss, score, position_take)


def print_result(is_loss, score, position_take):
    if not is_loss:
        print(f"You won! You've collected {score} coins.")
    else:
        score //= 2
        print(f"Game over! You've collected {score} coins.")
    print("Your path:")
    for p in position_take:
        print(p)


matrix = [[x for x in input().split(' ')] for _ in range(int(input()))]
matrix, player_position = get_positions(matrix)
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
player_result(matrix, moves, player_position)

