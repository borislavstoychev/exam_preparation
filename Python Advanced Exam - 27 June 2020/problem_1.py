from collections import deque


def bomb_count(boom, cre_bomb):
    if cre_bomb in boom:
        boom.pop(boom.index(cre_bomb))
        return boom
    elif len(boom) > 0:
        return boom
    return


def check_bombs_effects_casings(b_e, b_c):
    if bomb_effects:
        print("Bomb Effects:", end=" ")
        print(*bomb_effects, sep=", ")
    else:
        print("Bomb Effects: empty")
    if bomb_casings:
        print("Bomb Casings:", end=" ")
        print(*bomb_casings, sep=", ")
    else:
        print("Bomb Casings: empty")


bomb_effects = deque(int(effect) for effect in input().split(", "))
bomb_casings = deque(int(casing) for casing in input().split(", "))

bombs = {
    40: ["Datura Bombs", 0],
    60: ["Cherry Bombs", 0],
    120: ["Smoke Decoy Bombs", 0]
}
booms = [40, 60, 120]
while bomb_effects and bomb_casings:
    if not booms:
        break
    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()
    creating_bomb = bomb_casing + bomb_effect
    if creating_bomb in bombs:
        bombs[creating_bomb][1] += 1
        if bombs[creating_bomb][1] >= 3:
            booms = bomb_count(booms, creating_bomb)
        continue
    bomb_effects.appendleft(bomb_effect)
    bomb_casing -= 5
    bomb_casings.append(bomb_casing)

if len(booms) > 0:
    print("You don't have enough materials to fill the bomb pouch.")
    check_bombs_effects_casings(bomb_effects, bomb_casings)
else:
    print("Bene! You have successfully filled the bomb pouch!")
    check_bombs_effects_casings(bomb_effects, bomb_casings)

for kye, value in dict(sorted(bombs.items(), key=lambda el: el[1][0])).items():
    print(f"{value[0]}: {value[1]}")





