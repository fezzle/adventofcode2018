#!/usr/bin/env python3.6

import math

def power_level(x, y, grid_input):
    rack_id = (x) + 10
    power_level = rack_id * (y)
    power_level += grid_input
    power_level *= rack_id
    power_level = int(power_level / 100) % 10
    power_level -= 5
    return power_level

# def vs(a, b):
#     print("got:{} expected:{}".format(a, b))
    
# vs(power_level(122,79, 57), -5)
# vs(power_level(217,196, 39), 0)
# vs(power_level(101,153, 71), 4)

def make_grid(grid_input):
    grid = [0] * (300 * 300)

    for row in range(0,300):
        for col in range(0,300):
            grid[col + row*300] = power_level(col+1, row+1, grid_input)
    return grid

def reduce_grid(grid, size):
    grid_size = round(math.sqrt(len(grid)))
    grid2_size = grid_size-size
    grid2 = [0] * grid2_size**2
    for row in range(0, grid2_size):
        for col in range(0, grid2_size):
            total = 0
            for i in range(0, size):
                total += sum(grid[(col + (row+i)*grid_size) : (col + size + (row+i)*grid_size)])
            grid2[col + row*grid2_size] = total
    return grid2

def print_grid(label, grid):
    size = round(math.sqrt(len(grid)))
    toprint = min(30, size)
    print(label)
    for i in range(0, toprint):
        print(" ".join(["% 3d" % (n) for n in grid[i*size:i*size + toprint]]))
    print("")


#GRID_INPUT = 42
#GRID_INPUT = 18
GRID_INPUT = 7511

grid = make_grid(GRID_INPUT)
#print_grid("start", grid)
grid = reduce_grid(grid, 3)
#print_grid("3x3", grid)
highest = -99999
highest_i = -1
for i, v in enumerate(grid):
    if v > highest:
        highest = v
        highest_i = i
size = round(math.sqrt(len(grid)))
max_y = int(highest_i / size)
max_x = highest_i % size
print ("Part 1: {},{}".format(max_x+1, max_y+1))


best_reduce_grid_size = -1
best_reduce_grid_position = (-1,-1)
best_reduce_grid_value = -99999
grid = make_grid(GRID_INPUT)
for reduce_grid_size in range(0, 200):
    if reduce_grid_size > 0:
        grid2 = reduce_grid(grid, reduce_grid_size)
    else: 
        grid2 = grid

    highest = -99999
    highest_i = -1
    #print_grid("step {}".format(reduce_grid_size), grid2)
    for i, v in enumerate(grid2):
        if v > highest:
            highest = v
            highest_i = i

    size = round(math.sqrt(len(grid2)))
    max_y = int(highest_i / size)
    max_x = highest_i % size
    if highest > best_reduce_grid_value:
        best_reduce_grid_value = highest
        best_reduce_grid_position = (max_x+1, max_y+1)
        best_reduce_grid_size = reduce_grid_size
    

print("Part 2: {},{},{} - maxpower:{}".format(
    best_reduce_grid_position[0], 
    best_reduce_grid_position[1], 
    best_reduce_grid_size, 
    best_reduce_grid_value)
    )