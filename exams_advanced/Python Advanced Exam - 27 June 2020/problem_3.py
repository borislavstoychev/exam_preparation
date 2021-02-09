from collections import deque


def list_manipulator(some_list, command, place, *args):
    new_list = deque(some_list.copy())

    if command == "remove":
        assert 0 <= len(args) <= 1
        n = args[0] if len(args) == 1 else 1
        for _ in range(n):
            new_list.popleft() if place == "beginning" else new_list.pop()

    elif command == "add":
        assert len(args) > 0
        if place == "end":
            new_list += deque(args)
        elif place == "beginning":
            new_list = deque(args) + new_list

    return list(new_list)


# print(list_manipulator([1,2,3], "remove", "end"), [1, 2])
# print(list_manipulator([1,2,3], "remove", "beginning"), [2, 3])
# print(list_manipulator([1,2,3], "add", "beginning", 20), [20, 1, 2, 3])
# print(list_manipulator([1,2,3], "add", "end", 30), [1, 2, 3, 30])
print(list_manipulator([1,2,3], "remove", "end", 2), [1])
print(list_manipulator([1,2,3], "remove", "beginning", 2), [3])
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40), [20, 30, 40, 1, 2, 3])
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50), [1, 2, 3, 30, 40, 50])
