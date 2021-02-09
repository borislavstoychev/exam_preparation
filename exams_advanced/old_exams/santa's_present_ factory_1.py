from collections import deque


def materials_or_magics(m):
    if m:
        print("Materials left:", end=" ")
        print(*materials, sep=", ")


materials = deque(int(n) for n in input().split() if int(n) != 0)
magics = deque(int(n) for n in input().split() if int(n) != 0)
gifts = {
    150: ["Doll", 0],
    250: ["Wooden train", 0],
    300: ["Teddy bear", 0],
    400: ["Bicycle", 0]
}
while magics and materials:
    material = materials.pop()
    magic = magics.popleft()
    total = magic * material
    if total not in gifts:
        if total < 0:
            material += magic
        else:
            material += 15
        if not material == 0:
            materials.append(material)
        continue
    gifts[total][1] += 1
    
materials = deque(reversed(materials))
if gifts[150][1] > 0 and gifts[250][1] > 0 or gifts[400][1] > 0 and gifts[300][1] > 0:
    print("The presents are crafted! Merry Christmas!")
    materials_or_magics(materials)
    materials_or_magics(magics)
    for key, value in dict(sorted(gifts.items(), key=lambda el: el[1][0])).items():
        if value[1] > 0:
            print(f"{value[0]}: {value[1]}")
else:
    print("No presents this Christmas!")
    materials_or_magics(materials)
    materials_or_magics(magics)

