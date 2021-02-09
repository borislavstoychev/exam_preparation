def list_manipulator(*args):
    try:
        some_list, command, place, nums = args
    except ValueError:
        some_list, command, place = args
    if command == "remove":
        if place == "end":
            some_list.pop()
        elif place == "beginning":
            some_list.pop(0)
    elif command == "add":
        if place == "end":
            pass
    return some_list
print(list_manipulator([1,2,3], "remove", "end"))