import numpy as np
from collections import defaultdict

def parseData(data):
    snapshot_locations = []
    for line in data:
        vals = line[:-1].split('~')
        temp1 = tuple(int(c) for c in vals[0].split(','))
        temp2 = tuple(int(c) for c in vals[1].split(','))
        snapshot_locations.append([temp1, temp2])

    return snapshot_locations

def settleBricks(snapshot_locations):
    max_x, max_y = 0, 0
    max_z = 0
    for brick in snapshot_locations:
        edge1, edge2 = brick
        x = max(edge1[0], edge2[0])+1
        if x > max_x: max_x = x
        y = max(edge1[1], edge2[1])+1
        if y > max_y: max_y = y
        delta_z = abs(edge1[2]- edge2[2])+1
        max_z += delta_z

    # Note: Np prints (page, row, col) or (z, y, x)
    brick_positions = {}
    grid = np.zeros((max_z, max_y, max_x))
    z_counter = 0
    edge1, edge2 = snapshot_locations[0]
    x1, y1, z1 = edge1
    x2, y2, z2 = edge2
    delta_z = z2 - z1 + 1
    grid[z_counter:z_counter+delta_z, y1:y2+1, x1:x2+1] = 1
    brick_positions[1] = [(x1, y1, z_counter), (x2, y2, z_counter+delta_z)]
    z_counter += delta_z

    for i in range(1, len(snapshot_locations)):
        brick = snapshot_locations[i]
        edge1, edge2 = brick
        x1, y1, z1 = edge1
        x2, y2, z2 = edge2
        delta_z = z2 - z1 + 1

        # find first page where all values between x and y are zero
        for j in range(max_z-1, -1, -1):
            if np.any(grid[j, y1:y2+1, x1:x2+1] != 0):
                z_counter = j+1
                break

        grid[z_counter:z_counter+delta_z, y1:y2+1, x1:x2+1] = i+1
        brick_positions[i+1] = [(x1, y1, z_counter), (x2, y2, z_counter+delta_z-1)]

    return grid, brick_positions

def getDependencies(grid, brick_positions):
    dependencies = {1:[]}

    for i in range(2, len(brick_positions)+1):
        edge1, edge2 = brick_positions[i]
        x1, y1, z1 = edge1
        x2, y2, z2 = edge2

        # No dependencies if on bottom level
        if z1 == 0:
            dependencies[i] = []
            continue
        temp = grid[z1-1, y1:y2+1, x1:x2+1]
        if np.any(temp != 0):
            vals = list(np.unique(temp))
            if 0 in vals:
                idx = vals.index(0)
                vals.pop(idx)
            dependencies[i] = list(vals)
        else:
            dependencies[i] = []

    return dependencies

def part1():
    with open('input.txt', 'r') as f:
        data = f.readlines()

    snapshot_locations = parseData(data)
    settled_positions, brick_positions = settleBricks(snapshot_locations)
    dependencies = getDependencies(settled_positions, brick_positions)
    # Can remove supporting bricks with more than one
    # Combine lists for bricks in a given row and see if they overlap
    can_remove = {}
    for i in range(len(dependencies)):
        can_remove[i+1] = True

    for i in dependencies.keys():
        if len(dependencies[i]) == 1:
            can_remove[dependencies[i][0]] = False

    # Need to get bricks with no dependencies

    print(list(can_remove.values()).count(True))


"""
405 is too low
"""

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
