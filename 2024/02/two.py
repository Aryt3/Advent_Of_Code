reports = []

for i in open('input.txt', 'r'):
    reports.append([int(x) for x in i.strip().split()])

res = 0

def checker(i: list):
    asc, final = None, False

    for x in range(len(i)):
        if x != 0:
            if i[x-1] < i[x]:
                if asc == False:
                    break

                dif = i[x] - i[x-1]
                asc = True

            elif i[x-1] > i[x]:
                if asc == True:
                    break

                dif = i[x-1] - i[x]
                asc = False

            else:
                break

            if 3 < dif:
                final = False
                break

        if x == len(i) - 1:
            final = True

    return final

for i in reports:
    final = checker(i)

    if final != True:
        for x in range(len(i)):
            tmp_i = i.copy()
            tmp_i.pop(x)

            if checker(tmp_i) == True:
                res += 1
                break

    else:
        res += 1

print(res)