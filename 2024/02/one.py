reports = []

for i in open('input.txt', 'r'):
    reports.append([int(x) for x in i.strip().split()])

res = 0

for i in reports:
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

    res += 1 if final == True else 0        

print(res)