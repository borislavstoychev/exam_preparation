def div_25(deq, m_or_f):
    for i in deq:
        index = m_or_f.index(i)
        m_or_f = m_or_f[:index - 1] + m_or_f[index + 1:]
    return m_or_f


def print_result(m_f):
    m_f = m_f[::-1]
    if len(m_f) > 0:
        return ", ".join(list(map(str, m_f)))
    else:
        return "none"


male = [int(num) for num in input().split() if int(num) > 0]
female = [int(num) for num in input().split() if int(num) > 0]
female = female[::-1]
div_25_male = [new for new in male if new % 25 == 0]
div_25_female = [new for new in female if new % 25 == 0]
if div_25_male:
    male = div_25(div_25_male, male)
if div_25_female:
    female = div_25(div_25_female, female)
matches = 0
while male and female:
    m = male.pop()
    f = female.pop()
    if not m == f:
        m -= 2
        if not m <= 0:
            male.append(m)
    else:
        matches += 1
print(f"Matches: {matches}")
print(f"Males left: {print_result(male)}")
print(f"Females left: {print_result(female)}")
