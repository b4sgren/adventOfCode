from collections import defaultdict
from heapq import heappop, heappush
import itertools

# help from here: https://github.com/tmo1/adventofcode/blob/main/2023/17.py

# part 1
heap = []
entries_map = {}
cost = defaultdict(lambda: 1e8)
counter = itertools.count()

def addTask(task, priority):
    count = next(counter)
    entry = [priority, count, task]
    heappush(heap, entry)

def removeTask():
    entry = heappop(heap)
    return entry

def part1():
    # with open('temp2.txt', 'r') as f:
    with open('input2.txt', 'r') as f:
        data = f.readlines()

    # Convert to a grid
    grid = []
    for line in data:
        temp = list(line)[:-1]
        row = [int(v) for v in temp]
        grid.append(row)


    movement = {0:(0, -1), 1:(1, 0), 2:(0, 1), 3:(-1, 0)}
    # Add first step to priority queue
    addTask((0, 0, 1, 0), 0)
    cost[(0, 0, 1, 0)] = 0

    while True:
        entry = removeTask()
        _, _, task = entry
        x, y, dir, consecutive = task
        distance = cost[task]
        # Check if we reached our target
        if x == len(grid[0])-1 and y == len(grid)-1:
            print(distance)
            break
        # tuples of the direction and consecutive in that direction. First two are to the right and left
        directions = [((dir+1)%4, 1), ((dir-1)%4, 1)]
        if consecutive < 3:
            directions.append((dir, consecutive+1))
        for d in directions:
            next_dir, next_consecutive = d
            next_x = x + movement[next_dir][0]  # x is row
            next_y = y + movement[next_dir][1]  # y is col
            new_task = (next_x, next_y, next_dir, next_consecutive)
            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
                next_distance = distance + grid[next_y][next_x]
                if cost[new_task] > next_distance:
                    cost[new_task] = next_distance
                    addTask((next_x, next_y, next_dir, next_consecutive), next_distance)

# Move a minimum of 4 straight and max of 10
def part2():
    # with open('temp2.txt', 'r') as f:
    with open('input2.txt', 'r') as f:
        data = f.readlines()

    # Convert to a grid
    grid = []
    for line in data:
        temp = list(line)[:-1]
        row = [int(v) for v in temp]
        grid.append(row)


    movement = {0:(0, -1), 1:(1, 0), 2:(0, 1), 3:(-1, 0)}
    # Add first step to priority queue
    addTask((0, 0, 1, 0), 0)
    cost[(0, 0, 1, 0)] = 0

    while True:
        entry = removeTask()
        _, _, task = entry
        x, y, dir, consecutive = task
        distance = cost[task]
        # Check if we reached our target
        if x == len(grid[0])-1 and y == len(grid)-1:
            print(distance)
            break
        # tuples of the direction and consecutive in that direction. First two are to the right and left
        if consecutive < 4:
            directions = [(dir, consecutive+1)]
        else:
            directions = [((dir+1)%4, 1), ((dir-1)%4, 1)]
            if consecutive < 10:
                directions.append((dir, consecutive+1))
        for d in directions:
            next_dir, next_consecutive = d
            next_x = x + movement[next_dir][0]  # x is row
            next_y = y + movement[next_dir][1]  # y is col
            new_task = (next_x, next_y, next_dir, next_consecutive)
            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
                next_distance = distance + grid[next_y][next_x]
                if cost[new_task] > next_distance:
                    cost[new_task] = next_distance
                    addTask((next_x, next_y, next_dir, next_consecutive), next_distance)


if __name__=="__main__":
    # part1()

    part2()
