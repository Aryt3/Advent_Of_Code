import string

known_positions = []

# List of valid frequencies
frequencies = list(string.ascii_letters + string.digits)

# Read the antenna map from the file
antenna_map = [list(i.strip()) for i in open('input.txt', 'r')]

# Extract positions of frequencies in the map
a_positions = {
    (i, j): cell for i, row in enumerate(antenna_map)
    for j, cell in enumerate(row) if cell in frequencies
}

# Group positions by frequency
antenna_positions = {}
for pos, freq in a_positions.items():
    antenna_positions.setdefault(freq, []).append(pos)
    known_positions.append(pos)

# Modify map based on pairwise distances
for freq, positions in antenna_positions.items():
    for i in positions:
        for x in positions:
            if i != x:
                # Calculate directional differences
                diff_x = abs(i[1] - x[1])
                diff_y = abs(i[0] - x[0])

                # Adjust positions symmetrically based on comparison
                if i[1] < x[1]:  # i's x-coordinate is lower
                    pos_x_0, pos_x_1 = i[1] - diff_x, i[1] + diff_x
                else:  # i's x-coordinate is higher
                    pos_x_0, pos_x_1 = i[1] + diff_x, i[1] - diff_x

                if i[0] < x[0]:  # i's y-coordinate is lower
                    pos_y_0, pos_y_1 = i[0] - diff_y, i[0] + diff_y
                else:  # i's y-coordinate is higher
                    pos_y_0, pos_y_1 = i[0] + diff_y, i[0] - diff_y


                if 0 <= pos_x_0 < len(antenna_map[0]) and 0 <= pos_y_0 < len(antenna_map):
                    while True:
                        # Append position if valid
                        if antenna_map[pos_y_0][pos_x_0] != freq:
                            known_positions.append((pos_y_0, pos_x_0))
                        
                        # Increment positions progressively outward
                        next_x_0 = pos_x_0 + (-diff_x if i[1] < x[1] else diff_x)
                        next_y_0 = pos_y_0 + (-diff_y if i[0] < x[0] else diff_y)

                        # Break if out of bounds (based on next values)
                        if not (0 <= next_x_0 < len(antenna_map[0]) and 0 <= next_y_0 < len(antenna_map)):
                            break

                        # Update to the next position
                        pos_x_0, pos_y_0 = next_x_0, next_y_0

print(len(list(set(known_positions))))