import re

char_arr = []

for line in open('input.txt', 'r'):
    char_arr.append(list(line.strip()))

variations = []
row_len = len(char_arr[0])

# Add Rows
for i in char_arr:
    variations.append(''.join(i))
    variations.append(''.join(i)[::-1])

# Add Columns
for x in range(row_len):
    variations.append(''.join([i[x] for i in char_arr]))
    variations.append(''.join([i[x] for i in char_arr])[::-1])

# Add Diagonal Lines Top-Left to Bottom-Right
for i in range(len(char_arr)):
    cur_arr = []

    for x in range(row_len):
        if i+x < len(char_arr):
            cur_arr.append(char_arr[i+x][x])

    variations.append(''.join(cur_arr))
    variations.append(''.join(cur_arr)[::-1])

# Add Diagonal Lines Top-Right to Bottom-Left
for i in range(len(char_arr)):
    cur_arr = []

    for x, y in zip(range(row_len-1, -1, -1), range(row_len)):
        if i+y < len(char_arr):
            cur_arr.append(char_arr[i+y][x])

    variations.append(''.join(cur_arr))
    variations.append(''.join(cur_arr)[::-1])

# Add Diagonal Lines on Top, Left to Right
for i in range(len(char_arr[0])):
    cur_arr = []

    for x in range(row_len):
        if 1+i+x < row_len:
            cur_arr.append(char_arr[x][1+x+i])
    
    variations.append(''.join(cur_arr))
    variations.append(''.join(cur_arr)[::-1])

# Add Diagonal Lines on Top, Right to Left
for i in range(len(char_arr[0])):
    cur_arr = []

    for x in range(row_len):
        if row_len-2-x-i >= 0:
            cur_arr.append(char_arr[x][row_len-2-x-i])
    
    variations.append(''.join(cur_arr))
    variations.append(''.join(cur_arr)[::-1])


occurrences = 0
search_param = 'XMAS'

for i in variations:
    occurrences += len(re.findall(search_param, i))

print(occurrences)