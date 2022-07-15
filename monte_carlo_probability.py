# An ant is trying to get from point A to point B on a nxn grid. The coordinates of point A is (1, 1)(This is the top left corner),
# and the coordinates of point B is (n, n)(This is the bottom right corner). The ant can only move in four directions: top, bottom, left and right (no diagonal movement is allowed).
# If any of the four options satisfies the following conditions:
#
# - The new point should be within the boundary of the grid
# - The new point should not be already visited
#
# If P is the probablility of the and reaching point B for a 20x20 grid, use the Monte Carlo simulation to compute P.
#

import random


DIRE = ["UP", "DOWN", "RIGHT", "LEFT"]
NUMBER_OF_SIMS = 10000

grid_size = 10
grid = [["O" for x in range(grid_size)] for y in range(grid_size)]

ant_pos = [0, 0]
grid[ant_pos[0]][ant_pos[1]] = "X"
destination = (9, 9)


def remove_direction(direction, directions):
    for dir in directions:
        if dir == direction:
            ## delete dir from directions
            directions.remove(dir)
    
    return directions


def getRandomCoordinates(ant_pos, grid):
    not_found = True
    directions = DIRE.copy()

    while not_found:
        x = 0
        y = 0

        if len(directions) == 0:
            return None

        direction = random.choice(directions)
        # print(direction)
        directions = remove_direction(direction, directions)
        # print(directions)
        if direction == "UP":
            x = ant_pos[0] - 1
            y = ant_pos[1]
        elif direction == "DOWN":
            x = ant_pos[0] + 1
            y = ant_pos[1]
        elif direction == "RIGHT":
            x = ant_pos[0]
            y = ant_pos[1] + 1
        elif direction == "LEFT":
            x = ant_pos[0]
            y = ant_pos[1] - 1


        if x < 0 or y < 0 or x >= grid_size or y >= grid_size:
            # print("Out of bounds: ", x, y)
            continue
        if grid[x][y] == "O":
            return x, y


def move(grid, ant_pos, destination):
    while True:
        coordinates = getRandomCoordinates(ant_pos, grid)
        
        if coordinates:
            ant_pos[0], ant_pos[1] = coordinates
            # print("Ant moved to: ", ant_pos)
            if ant_pos[0] == destination[0] and ant_pos[1] == destination[1]:
                # print_grid(grid)
                return True
            else:
                grid[ant_pos[0]][ant_pos[1]] = "X"
                # print_grid(grid)
        else:
            return False


def print_grid(grid):
    for i in range(grid_size):
        for j in range(grid_size):
            if destination[0] == i and destination[1] == j:
                print("D", end=" ")
            else:
                print(" " if grid[i][j] == "O" else grid[i][j], end=" ")
        
        print()
    
    print()


found = 0
lost = 0
for i in range(0, NUMBER_OF_SIMS):
    grid = [["O" for x in range(grid_size)] for y in range(grid_size)]
    ant_pos = [0, 0]
    if move(grid, ant_pos, destination):
        found += 1
    else:
        lost += 1


print(f"Found: {found}, losses: {lost}")
found_probability = found / (found + lost)
print(f"Probability of reaching point B is : {found_probability}")
