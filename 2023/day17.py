import numpy as np
np.set_printoptions(linewidth=200)
from copy import deepcopy as copy
from functools import cache
import sys
sys.setrecursionlimit(10000)

# Things to try
'''
Graph has 3 states (x, y, direction)
The grid is not the graph. Use the grid to build up the graph and find the shortest path dynamically
Still Use djikstras algorithm with my 3 path limit
Prev_node will be a function of 3 states
'''
grid = []
min_distance = 1e9

# facing north: 1, facing west: 2, facing south:3, facing east:4
def getNeighbors(source, path):
    neighbors = []

    if source[-1] == 1:
        r, c = source[0]-1, source[1]
        neighbors.append((r, c, 1))
        neighbors.append((r, c, 2))
        neighbors.append((r, c, 4))
    elif source[-1] == 2:
        r, c = source[0], source[1]-1
        neighbors.append((r, c, 1))
        neighbors.append((r, c, 2))
        neighbors.append((r, c, 3))
    elif source[-1] == 3:
        r, c = source[0]+1, source[1]
        neighbors.append((r, c, 2))
        neighbors.append((r, c, 3))
        neighbors.append((r, c, 4))
    elif source[-1] == 4:
        r, c = source[0], source[1]+1
        neighbors.append((r, c, 1))
        neighbors.append((r, c, 3))
        neighbors.append((r, c, 4))

    return neighbors

# Need to check somewhere if the distance is less than min distance
@cache
def getShortestPath(source, target, path, distance):
    if source[0] == target[0] and source[1] == target[1]:
        if distance < min_distance:
            min_distance = distance

    neighbors = getNeighbors(source, path)
    for neighbor in neighbors:
        new_path = (*path, neighbor)
        new_dist = distance + grid[neighbor[0], neighbor[1]]
        getShortestPath(neighbor, target, new_path, new_dist)

# Try recursively
def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    # Convert to a grid
    global grid
    for line in data:
        temp = list(line)[:-1]
        row = [int(v) for v in temp]
        grid.append(row)
    grid  = np.array(grid)

    source = (0, 0, 3)  # may need to test facing south first
    target = (len(grid)-1, len(grid[0])-1, 1)
    distance = 0
    path = (source)

    getShortestPath(source, target, path, distance)

    print(min_distance)


def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
