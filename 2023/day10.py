import numpy as np
'''
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''


def identifyStartingPipe(starting_point, map):
    north_pipe = None
    use_north = False
    if starting_point[0] > 0:
        north_pipe = map[starting_point[0]-1][starting_point[1]]
        north_idx = np.array(starting_point) + np.array([-1, 0])
        use_north = north_pipe == '|' or north_pipe == 'F' or north_pipe == '7'
    south_pipe = None
    use_south = False
    if starting_point[0] < len(map):
        south_pipe = map[starting_point[0]+1][starting_point[1]]
        south_idx = np.array(starting_point) + np.array([1, 0])
        use_south = south_pipe == '|' or south_pipe == 'L' or south_pipe == 'J'
    west_pipe = None
    use_west = False
    if starting_point[1] > 0:
        west_pipe = map[starting_point[0]][starting_point[1]-1]
        west_idx = np.array(starting_point) + np.array([0, -1])
        use_west = west_pipe == '-' or west_pipe == 'F' or west_pipe == 'L'
    east_pipe = None
    use_east = False
    if starting_point[1] < len(map[0]):
        east_pipe = map[starting_point[0]][starting_point[1]+1]
        east_idx = np.array(starting_point) + np.array([0, 1])
        use_east = east_pipe == '-' or east_pipe == 'J' or east_pipe == '7'


    starting_pipes = []
    if use_north and use_south: starting_pipes.append('|')
    if use_north and use_west: starting_pipes.append('J')
    if use_north and use_east: starting_pipes.append('L')
    if use_west and use_south: starting_pipes.append('7')
    if use_west and use_east: starting_pipes.append('-')
    if use_south and use_east: starting_pipes.append('F')

    return starting_pipes

def getNextIdxs(pipe, idx):
    if pipe == '-':
        idx1 = idx + np.array([0, -1])
        idx2 = idx + np.array([0, 1])
        next_idxs = [idx1, idx2]
    elif pipe == '|':
        idx1 = idx + np.array([1, 0])
        idx2 = idx + np.array([-1, 0])
        next_idxs = [idx1, idx2]
    elif pipe == '7':
        idx1 = idx + np.array([0, -1])
        idx2 = idx + np.array([1, 0])
        next_idxs = [idx1, idx2]
    elif pipe == 'L':
        idx1 = idx + np.array([0, 1])
        idx2 = idx + np.array([-1, 0])
        next_idxs = [idx1, idx2]
    elif pipe == 'J':
        idx1 = idx + np.array([0, -1])
        idx2 = idx + np.array([-1, 0])
        next_idxs = [idx1, idx2]
    elif pipe == 'F':
        idx1 = idx + np.array([0, 1])
        idx2 = idx + np.array([1, 0])
        next_idxs = [idx1, idx2]

    return next_idxs

def part1():
    # with open('temp.txt', 'r') as f:
    # with open('temp2.txt', 'r') as f:
    with open('day10.txt', 'r') as f:
        data = f.readlines()
    map = [list(line)[:-1] for line in data]

    for i, line in enumerate(map):
        if 'S' in line:
            idx = line.index('S')
            starting_point = [i, idx]

    # Identify type of starting tile
    starting_pipes = identifyStartingPipe(starting_point, map)
    visited_node = []
    maximum_distance = 0
    # Perform breadth first search
    for starting_pipe in starting_pipes:
        pipe_queue = [(starting_pipe, np.array(starting_point), 0)]
        while(len(pipe_queue)) > 0:
            pipe, idx, dist = pipe_queue.pop(0)
            visited_node.append(list(idx))
            nextIdxs = getNextIdxs(pipe, idx)
            for nextIdx in nextIdxs:
                out_of_range = nextIdx[0] < 0 or nextIdx[0] >= len(map)
                out_of_range = out_of_range or nextIdx[1] < 0 or nextIdx[1] >= len(map[1])
                if list(nextIdx) not in visited_node and not out_of_range:
                    pipe_queue.append((map[nextIdx[0]][nextIdx[1]], nextIdx, dist+1))
                    maximum_distance = dist+1

    print(maximum_distance)


def part2():
    # with open('temp.txt', 'r') as f:
    # with open('temp2.txt', 'r') as f:
    with open('day10.txt', 'r') as f:
        data = f.readlines()
    map = [list(line)[:-1] for line in data]

    for i, line in enumerate(map):
        if 'S' in line:
            idx = line.index('S')
            starting_point = [i, idx]

    # Identify type of starting tile
    starting_pipes = identifyStartingPipe(starting_point, map)
    visited_node = []  # outlines the loop
    min_row = len(map)
    max_row = 0
    # Perform breadth first search
    for starting_pipe in starting_pipes:
        pipe_queue = [(starting_pipe, np.array(starting_point), 0)]
        while(len(pipe_queue)) > 0:
            pipe, idx, dist = pipe_queue.pop(0)
            if min_row > idx[0]: min_row = idx[0]
            if max_row < idx[0]: max_row = idx[0]
            visited_node.append(list(idx))
            nextIdxs = getNextIdxs(pipe, idx)
            for nextIdx in nextIdxs:
                out_of_range = nextIdx[0] < 0 or nextIdx[0] >= len(map)
                out_of_range = out_of_range or nextIdx[1] < 0 or nextIdx[1] >= len(map[1])
                if list(nextIdx) not in visited_node and not out_of_range:
                    pipe_queue.append((map[nextIdx[0]][nextIdx[1]], nextIdx, dist+1))

    for row, line in enumerate(map):
        crossed_curve = 0
        for col in range(0, len(line)):
            idx = [row, col]
            if idx not in visited_node:
                map[row][col] = '.'

    with open('loop.txt', 'w') as f:
        for line in map:
            string = ''
            for c in line:
                string += c
            f.write(string + "\n")

    num_inside = 0
    for row, line in enumerate(map):
        crossed_curve = 0
        for col in range(0, len(line)):
            idx = [row, col]
            # only increment if in loop and one of the following 3 pipes
            # WOuld also work with ['|', 'F', '7']
            # Couth either both corners going up or both corners going down but dont count both of them
            if idx in visited_node and map[idx[0]][idx[1]] in ['|', 'L', 'J']:
                crossed_curve += 1
            if idx in visited_node:
                continue
            else:
                if crossed_curve % 2 == 1:
                    num_inside += 1

    print(num_inside)

if __name__=="__main__":
    part1()

    part2()
