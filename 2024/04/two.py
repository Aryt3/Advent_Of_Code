# Load Text Lines into File
char_arr = [list(line.strip()) for line in open('input.txt', 'r')]

# Generate every possible 3x3 Chunk
chunks = [[row[x:x+3] for row in char_arr[i:i+3]] for i in range(len(char_arr) - 2) for x in range(len(char_arr[0]) - 2)]

# Count amount of MAS occurrances in 3x3 Chunks when there are more then 2 occurrances
occurrances = sum([1 for i in chunks if sum('MAS' == ''.join([i[x][y] for x, y in coords]) for coords in [((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((2, 0), (1, 1), (0, 2)), ((2, 2), (1, 1), (0, 0))]) == 2])

print(occurrances)