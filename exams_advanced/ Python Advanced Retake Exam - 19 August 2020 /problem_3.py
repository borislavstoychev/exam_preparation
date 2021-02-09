def numbers_searching(*args):
    nums = []
    numbers = []
    print_list = []
    for num in args:
        if num not in numbers:
            numbers.append(num)
        else:
            if num not in nums:
                nums.append(num)
    count = 0
    number = 0
    numbers = sorted(numbers)
    for n in range(min(numbers), len(numbers) + min(numbers)):
        if not n == numbers[count]:
            number = n
            break
        count += 1
    print_list.append(number)
    print_list.append(sorted(nums))
    return print_list


# print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))