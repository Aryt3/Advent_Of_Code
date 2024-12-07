import time

lab_map = [list(i.strip()) for i in open('example.txt', 'r')]

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
ends = {'^': 0, 'v': len(lab_map), '<': 0, '>': len(lab_map[0])}

# Initial position and direction of guard
current_position = [(i, j) for i, row in enumerate(lab_map) for j, cell in enumerate(row) if cell in directions][0]
current_direction = lab_map[current_position[0]][current_position[1]]

# List to save all moves
moves = [current_position]

# Simulate guard's movements
while True:
    x, y = current_position
    dx, dy = directions[current_direction]
    next_x, next_y = x + dx, y + dy

    # Move forward if no obstacle os found
    if (0 <= next_x < len(lab_map) and 0 <= next_y < len(lab_map[0]) and lab_map[next_x][next_y] != '#'):
        lab_map[x][y] = '.' 
        current_position = (next_x, next_y)
        lab_map[next_x][next_y] = current_direction 

    else:
         # If border is hit break
        if not (0 <= next_x < len(lab_map) and 0 <= next_y < len(lab_map[0])):
            break

        current_direction = turn_right[current_direction]
        lab_map[x][y] = current_direction  # Update guard's direction in place

    moves.append(current_position)

    # For Visualisation

    for row in lab_map:
        print(''.join(row))
    print("\n---\n")
    
    time.sleep(0.5)


unique_moves = set(moves)

print(len(list(unique_moves)))