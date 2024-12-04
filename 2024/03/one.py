import re

inp = open('input.txt', 'r').read()

out = re.findall(r'mul\(\d+,\d+\)', inp)

res = sum([int(i.split('mul(')[1].split(',')[0]) * int(i.split(',')[1].split(')')[0]) for i in out])

print(res)