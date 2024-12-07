from collections import deque

lab_map = [list(i.strip()) for i in open('input.txt', 'r')]

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

# Find the initial position and direction of the guard
start_position = [(i, j) for i, row in enumerate(lab_map) for j, cell in enumerate(row) if cell in directions][0]
start_direction = lab_map[start_position[0]][start_position[1]]

# Find all reachable positions using BFS
def get_reachable_positions(lab_map, start_position):
    rows, cols = len(lab_map), len(lab_map[0])
    reachable = set()
    queue = deque([start_position])
    visited = set([start_position])

    while queue:
        x, y = queue.popleft()
        reachable.add((x, y))

        # Check all four possible moves
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and lab_map[nx][ny] == '.':
                visited.add((nx, ny))
                queue.append((nx, ny))

    return reachable

reachable_positions = get_reachable_positions(lab_map, start_position)

# Simulate the guard's movement
def simulate_guard(lab_map, start_position, start_direction):
    current_position = start_position
    current_direction = start_direction
    visited = set()

    while True:
        # If we've been in this position and direction before, it's a loop
        if (current_position, current_direction) in visited:
            return True
        visited.add((current_position, current_direction))

        x, y = current_position
        dx, dy = directions[current_direction]
        next_x, next_y = x + dx, y + dy

        # Check if the guard can move forward
        if 0 <= next_x < len(lab_map) and 0 <= next_y < len(lab_map[0]) and lab_map[next_x][next_y] not in ['#', 'O']:
            current_position = (next_x, next_y)
        else:
            # Turn right if obstructed
            current_direction = turn_right[current_direction]

        # Stop if the guard leaves the map
        if not (0 <= next_x < len(lab_map) and 0 <= next_y < len(lab_map[0])):
            return False

# Check all reachable positions for valid obstruction placement
possible_positions = []
for x, y in reachable_positions:
    if (x, y) == start_position:
        continue

    # Temporarily place the obstruction
    lab_map[x][y] = 'O'

    # Simulate the guard's movement
    if simulate_guard(lab_map, start_position, start_direction):
        possible_positions.append((x, y))

    # Remove the obstruction
    lab_map[x][y] = '.'

# Output the results
print("Number of possible obstruction positions:", len(possible_positions))
print("Positions:", possible_positions)
