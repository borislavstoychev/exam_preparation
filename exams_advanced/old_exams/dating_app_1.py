from collections import deque


def div_25(p, m_or_f):
    return p % 25 == 0 and len(m_or_f) > 0


def print_result(m_f):
    if len(m_f) > 0:
        return ", ".join(list(map(str, m_f)))
    else:
        return "none"


male = deque(int(num) for num in input().split() if int(num) > 0)
female = deque(int(num) for num in input().split() if int(num) > 0)
matches = 0
while male and female:
    m = male.pop()
    f = female.popleft()
    if not div_25(m, male):
        if div_25(f, female):
            female.popleft()
            male.append(m)
            continue
        if not m == f:
            m -= 2
            if m > 0:
                male.append(m)
        else:
            matches += 1
        continue
    male.pop()
    female.appendleft(f)
male = list(reversed(male))
print(f"Matches: {matches}")
print(f"Males left: {print_result(male)}")
print(f"Females left: {print_result(female)}")
