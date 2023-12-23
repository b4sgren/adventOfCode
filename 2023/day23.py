import numpy as np

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
    queue = [(0, idx0, 0)]
    max_dist = 0
    while len(queue) > 0:
        idx = queue.pop()
        r, c, dist = idx
        distances[r, c] = dist
        visited[r, c] = True
        if r == target_idx[0] and c == target_idx[1]:
            break

        next_dist = dist-1
        if grid[r][c] == '.':
            neighbors = [(r+1, c, next_dist), (r, c+1, next_dist), (r-1, c, next_dist), (r, c-1, next_dist-1)]
        elif grid[r][c] == '>':
            neighbors = [(r, c+1, next_dist)]
        elif grid[r][c] == '<':
            neighbors = [(r, c-1, next_dist)]
        elif grid[r][c] == '^':
            neighbors = [(r-1, c, next_dist)]
        elif grid[r][c] == 'v':
            neighbors = [(r+1, c, next_dist)]

        for neighbor in neighbors:
            # Check if visited
            r, c, _ = neighbor
            if (r, c) in visited.keys() and not visited[(r, c)] and grid[r][c] != '#':
                queue.append(neighbor)

    print(distances[target_idx[0], target_idx[1]])



def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
