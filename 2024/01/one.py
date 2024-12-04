left, right = [], []

for i in open('input.txt', 'r'):
    left.append(int(i.strip().split()[0]))
    right.append(int(i.strip().split()[1]))

res = 0

for l, r in zip(sorted(left), sorted(right)):
    res += abs(r - l)

print(res)