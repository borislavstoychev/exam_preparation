jobs_nums = [int(num) for num in input().split(", ")]
index = int(input())
clock = 0
while True:
    min_num = min(jobs_nums)
    i = jobs_nums.index(min_num)
    jobs_nums[i] = 99999
    clock += min_num
    if i == index:
        break

print(clock)
