def find_sub_list(n_l, n):
    subs_list = []
    for i in range(n):
        subs_list.append(n_l[i:len(n_l):n])
    return subs_list


def find_strongest(r):
    max_num = max(r)
    if not max_num == r[0] and not max_num == r[-1]:
        return max_num
    return


def find_strongest_eggs(*args):
    result = []
    nums_list, n = args
    if n > 1:
        sub_list = find_sub_list(nums_list, n)
        for row in sub_list:
            egg = find_strongest(row)
            if egg:
                result.append(egg)
    else:
        result = [find_strongest(nums_list)]
    return result


test = ([-1, 7, 3, 15, 2, 12, 6, 7, 8], 3)
print(find_strongest_eggs(*test))
test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
