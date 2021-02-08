from collections import deque


def best_list_pureness(*args):
    lists, num = args
    lists = deque(lists)
    rotate = 0
    max_result = 0
    max_index = 0
    while not rotate == num + 1:
        results = sum(lists[index]*index for index in range(len(lists)))
        lists.appendleft(lists.pop())
        if max_result < results:
            max_result = results
            max_index = rotate
        rotate += 1

    return f"Best pureness {max_result} after {max_index} rotations"


test = ([4, 3, 2, 6], 0)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


