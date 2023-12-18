import numpy as np
np.set_printoptions(linewidth=200)
from copy import deepcopy as copy

# Things to try
'''
Graph has 3 states (x, y, direction)
The grid is not the graph. Use the grid to build up the graph and find the shortest path dynamically
Still Use djikstras algorithm with my 3 path limit
Prev_node will be a function of 3 states
'''

# facing north: 1, facing west: 2, facing south:3, facing east:4
def getNeighbors(source):
    neighbors = []
    if source[-1] != 3:
        neighbors.append((source[0]-1, source[1], 1))
    if source[-1] != 4:
        neighbors.append((source[0], source[1]-1, 2))
    if source[-1] != 1:
        neighbors.append((source[0]+1, source[1], 3))
    if source[-1] != 2:
        neighbors.append((source[0], source[1]+1, 4))

    return neighbors

def findShortestPath(grid, source, target):
    prev_node = {tuple(source):None}
    queue = set([(i, j, k) for i in range(len(grid)) for j in range(len(grid[0])) for k in range(1, 5)])  # x, y, direction
    grid_distances = {}
    for q in queue:
        grid_distances[q] = 1e8
    grid_distances[(0, 0, 1)] = 0

    while source not in target and len(queue) > 0:
        min_dist = 1e8
        for q in queue:
            if grid_distances[q] < min_dist:
                min_dist = grid_distances[q]
                source = q

        queue.remove(source)
        # Edit to work with tuples. Do in a function
        neighbors = getNeighbors(source)
        for neighbor in neighbors:
            # Determine if this is a valid neighbor
            if neighbor[0] < 0 or neighbor[0] >= len(grid) or neighbor[1] < 0 or neighbor[1] >= len(grid[0]):
                continue

            prev = copy(source)
            curr = copy(neighbor)
            diff = np.zeros(3)
            for _ in range(4):
                if prev is None:
                    break
                diff += np.array(curr) - np.array(prev)
                curr = prev
                if tuple(curr) in prev_node:
                    prev = prev_node[curr]
                else:
                    break
            if np.max(np.abs(diff[:2])) > 3:
                continue
            alt = grid_distances[source] + grid[neighbor[0], neighbor[1]]
            if alt < grid_distances[neighbor]:
                grid_distances[neighbor] = alt
                prev_node[neighbor] = source
                debug = 1

    # Get path
    path = []
    node = copy(source)
    while prev_node[node] is not None:
        path.append(node)
        node = prev_node[node]
    path.append(node)
    path.reverse()
    print(path)

    return grid_distances[source]

def part1():
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    # Convert to a grid
    grid = []
    for line in data:
        temp = list(line)[:-1]
        row = [int(v) for v in temp]
        grid.append(row)
    grid  = np.array(grid)

    source = (0, 0, 1)  # because of padding
    target = [(len(grid)-1, len(grid[0])-1, 1), (len(grid)-1, len(grid[0])-1, 2), (len(grid)-1, len(grid[0])-1, 3), (len(grid)-1, len(grid[0])-1, 4)]

    path_length = findShortestPath(grid, source, target)
    # path_length = findShortestPath(grid, target, source)

    print(path_length)


def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
