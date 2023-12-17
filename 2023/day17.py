import numpy as np
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
    steps_map = {'N':0, 'S':0, 'E':0, 'W':0}
    while list(source) != list(target) and len(queue) > 0:
        # Not min index but index of nodes left in queue that is the min
        min_dist = 1e8
        for q in queue:
            if grid_distances[q[0], q[1]] < min_dist:
                source = q

        idx = queue.index(list(source))
        queue.pop(idx)

        # Probably need to check to make sure I havent gone 3 straight yet
        temp = [source + north, source + south, source + east, source + west]
        neighbors = [loc for loc in temp if list(loc) in queue]
        for neighbor in neighbors:
            # Determine if this is a valid neighbor
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

    print(path_length)


def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
