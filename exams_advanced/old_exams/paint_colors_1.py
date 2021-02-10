from collections import deque


def searching_color(f_c, l, r):
    if l + r in f_c:
        return l + r
    elif r + l in f_c:
        return r + l
    return


def searching_sub_color(s_c, l, r):
    if l + r in s_c:
        return l + r
    elif r + l in s_c:
        return r + l
    return


def sub_color_validate(c_l, sub_col, s_c):
    color_1, color_2 = s_c[sub_col]
    if color_1 in c_l and color_2 in c_l:
        return sub_col
    return


strings = deque(s for s in input().split())
first_color = ["red", "yellow", "blue"]
second_color = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}
colors = []

while len(strings) > 1:
    right = strings.pop()
    left = strings.popleft()
    middle = len(strings) // 2
    color = searching_color(first_color, left, right)
    if color:
        colors.append(color)
        continue
    sub_colors = searching_sub_color(second_color, left, right)
    if sub_colors:
        colors.append(sub_colors)
        continue
    if not color:
        right = right[:-1]
        left = left[:-1]
        if not right == "":
            strings.insert(middle, right)
        if not left == "":
            strings.insert(middle, left)
if strings:
    final = strings.pop()
    if final in first_color:
        colors.append(final)
final_colors = []
for c in colors:
    if c in second_color:
        c = sub_color_validate(colors, c, second_color)
    if c:
        final_colors.append(c)
print(final_colors)
