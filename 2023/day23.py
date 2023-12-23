import numpy as np
np.set_printoptions(linewidth=200)
from heapq import heappop, heappush

def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    grid = [list(line[:-1]) for line in data]
    distances = np.zeros((len(grid), len(grid[0])))

    # get possible trail indices
    visited = {(r, c):False for r, row in enumerate(grid) for c, col in enumerate(row) if grid[r][c] != '#'}

    idx0 = grid[0].index('.')
    distances[0, idx0] = 0
    visited[(0, idx0)] = True

    idx = grid[-1].index('.')
    target_idx = (len(grid)-1, idx)

    # Do a version of DFS. Looking for longest path
    # Do BFS with negative weights
    queue = []
    heappush(queue, (0, 0, idx0))
    while len(queue) > 0:
        idx = heappop(queue)
        _, r, c = idx
        dist = distances[r, c]
        visited[r, c] = True
        if r == target_idx[0] and c == target_idx[1]:
            break

        next_dist = dist-1
        neighbors = []
        if grid[r][c] == '.':
            neighbors = [(next_dist, r+1, c), (next_dist, r, c+1), (next_dist, r-1, c), (next_dist, r, c-1)]
        elif grid[r][c] == '>':
            neighbors = [(next_dist, r, c+1)]
        elif grid[r][c] == '<':
            neighbors = [(next_dist, r, c-1)]
        elif grid[r][c] == '^':
            neighbors = [(next_dist, r-1, c)]
        elif grid[r][c] == 'v':
            neighbors = [(next_dist, r+1, c)]

        for neighbor in neighbors:
            # Check if visited
            _, r, c = neighbor
            if (r, c) in visited.keys() and not visited[(r, c)] and grid[r][c] != '#':
                heappush(queue, neighbor)
                if distances[r, c] > next_dist:
                    distances[r, c] = next_dist
                    queue.append(neighbor)

    print(distances[target_idx[0], target_idx[1]])



def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
