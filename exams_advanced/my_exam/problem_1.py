from collections import deque

firework_effects = deque(int(n) for n in input().split(", ") if int(n) > 0)
powers = deque(int(num) for num in input().split(", ") if int(num) > 0)

bombs = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
is_show = False
while firework_effects and powers:
    if bombs["Palm Fireworks"] >= 3 and bombs["Willow Fireworks"] >= 3 and bombs["Crossette Fireworks"] >= 3:
        is_show = True
        break
    firework = firework_effects.popleft()
    power = powers.pop()
    result = firework + power
    if result % 3 == 0 and result % 5 == 0:
        bombs["Crossette Fireworks"] += 1
    elif result % 3 == 0 and not result % 5 == 0:
        bombs["Palm Fireworks"] += 1
    elif result % 5 == 0 and not result % 3 == 0:
        bombs["Willow Fireworks"] += 1
    else:
        firework -= 1
        if not firework <= 0:
            firework_effects.append(firework)
        powers.append(power)

if is_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if firework_effects:
    print("Firework Effects left: ", end="")
    print(*firework_effects, sep=", ")
if powers:
    print("Explosive Power left: ", end="")
    print(*powers, sep=", ")
for key, value in bombs.items():
    print(f"{key}: {value}")