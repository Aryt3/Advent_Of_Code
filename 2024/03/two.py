import re

inp = open('input.txt', 'r').read()

cor_snippets = [inp.split("don't()")[0]] + [i.split(re.match(r'^.*?(?=do\(\))', i)[0])[1] for i in inp.split("don't()")[1:] if 'do()' in i]

res = sum([int(i.split('mul(')[1].split(',')[0]) * int(i.split(',')[1].split(')')[0]) for i in [y for x in cor_snippets for y in re.findall(r'mul\(\d+,\d+\)', x)]])

print(res)

