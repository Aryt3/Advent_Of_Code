left, right = [], []

for i in open('input.txt', 'r'):
    left.append(int(i.strip().split()[0]))
    right.append(int(i.strip().split()[1]))

res = 0

for l in sorted(left):
    res += abs(l * right.count(l))

print(res)