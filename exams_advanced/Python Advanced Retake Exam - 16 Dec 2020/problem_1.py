from collections import deque


def div_25(m_or_f):
    new_m_f = deque()
    while m_or_f:
        num = m_or_f.pop()
        if num % 25 ==0:
            try:
                m_or_f.pop()
            except IndexError:
                break
            continue
        new_m_f.append(num)
    return new_m_f


def print_result(m_f):
    if len(m_f) > 0:
        return ", ".join(list(map(str, m_f)))
    else:
        return "none"


male = deque(int(num) for num in input().split() if int(num) > 0)
female = deque(int(num) for num in input().split() if int(num) > 0)
matches = 0
if [new for new in male if new % 25 == 0]:
    male = div_25(male)
if [new for new in female if new % 25 == 0]:
    female = div_25(female)
    female = deque(reversed(female))

while male and female:
    m = male.pop()
    f = female.popleft()
    if not m == f:
        m -= 2
        if not m <= 0:
            male.append(m)
    else:
        matches += 1
male = list(reversed(male))

print(f"Matches: {matches}")
print(f"Males left: {print_result(male)}")
print(f"Females left: {print_result(female)}")