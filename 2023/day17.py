import numpy as np
np.set_printoptions(linewidth=200)
from copy import deepcopy as copy

def findShortestPath(grid, source, target):
    grid_distances = np.ones_like(grid) * 1e8
    prev_node = {}
    queue = [[i, j] for i in range(len(grid)) for j in range(len(grid[0]))]
    grid_distances[source[0], source[1]] = 0

    north = np.array([-1, 0])
    south = np.array([1, 0])
    east = np.array([0, 1])
    west = np.array([0, -1])
    # while list(source) != list(target) and len(queue) > 0:
    while len(queue) > 0:
        # Not min index but index of nodes left in queue that is the min
        min_dist = 1e8
        for q in queue:
            if grid_distances[q[0], q[1]] < min_dist:
                min_dist = grid_distances[q[0], q[1]]
                source = q

        idx = queue.index(list(source))
        queue.pop(idx)
        if source == [1, 4]:
            debug = 1

        # Probably need to check to make sure I havent gone 3 straight yet
        neighbors = [source + north, source + south, source + east, source + west]
        for neighbor in neighbors:
            # Determine if this is a valid neighbor
            if neighbor[0] < 0 or neighbor[0] >= len(grid) or neighbor[1] < 0 or neighbor[1] >= len(grid[0]):
                continue
            prev = copy(source)
            curr = copy(neighbor)
            diff = np.zeros(2)
            for _ in range(4):
                diff += np.array(curr) - np.array(prev)
                curr = prev
                if tuple(curr) in prev_node:
                    prev = list(prev_node[tuple(curr)])
                else:
                    break
            if np.max(np.abs(diff)) > 3:
                continue
            alt = grid_distances[source[0], source[1]] + grid[neighbor[0], neighbor[1]]
            if alt < grid_distances[neighbor[0], neighbor[1]]:
                grid_distances[neighbor[0], neighbor[1]] = alt
                prev_node[tuple(neighbor)] = tuple(source)
                debug = 1
        debug = 1

    # Get path
    path = [target]
    node = target
    while tuple(node) in prev_node:
        node = list(prev_node[tuple(node)])
        path.append(node)
    path.reverse()

    print(path)
    for val in path:
        grid[val[0], val[1]] = 0
    print(grid)

    return grid_distances[target[0], target[1]]

'''
1  function Dijkstra(Graph, source):
 2
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8
 9      while Q is not empty:
10#           u ← vertex in Q with min dist[u]
11          remove u from Q
12
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
'''

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

    source = np.array([0, 0])  # because of padding
    target = np.array([len(grid)-1, len(grid[0])-1])
    path_length = findShortestPath(grid, source, target)
    # path_length = findShortestPath(grid, target, source)

    print(path_length)


def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
