import sys
sys.setrecursionlimit(10000)

def parseData(data):
    directions, distances, colors = [], [], []
    for line in data:
        vals = line[:-1].split()
        directions.append(vals[0])
        distances.append(int(vals[1]))
        colors.append(vals[2][1:-1])

    return directions, distances, colors

def floodFill(grid, loc):
    if loc[0] < 0 or loc[0] >= len(grid) or loc[1] < 0 or loc[1] >= len(grid[0]):
        return grid
    # reached a border or an index already filled
    if grid[loc[0]][loc[1]] == '#' or grid[loc[0]][loc[1]] == '0':
        return grid

    grid[loc[0]][loc[1]] = '0'
    grid = floodFill(grid, [loc[0]+1, loc[1]])
    grid = floodFill(grid, [loc[0]-1, loc[1]])
    grid = floodFill(grid, [loc[0], loc[1]+1])
    grid = floodFill(grid, [loc[0], loc[1]-1])

    return grid

# TODO: Need to handle going up initially. Edit to starting location
def part1():
    # with open('temp2.txt', 'r') as f:
    with open('input2.txt', 'r') as f:
        data = f.readlines()

    directions, distances, colors = parseData(data)

    # Get max rows/cols. Assume it won't go negative
    rows = 0
    cols = 0
    max_rows = 1
    min_rows = 0
    max_cols = 1
    min_cols = 0
    for dir, dist in zip(directions, distances):
        if dir == 'D':
            rows += dist
            if rows > max_rows: max_rows = rows
        elif dir == 'U':
            rows -= dist
            if rows < min_rows: min_rows = rows
        elif dir == 'R':
            cols += dist
            if cols > max_cols: max_cols = cols
        elif dir == 'L':
            cols -= dist
            if cols < min_cols: min_cols = cols

    # Outline the loop
    grid = [['.' for i in range(max_cols - min_cols+1)] for _ in range(max_rows-min_rows+1)]
    row, col = abs(min_rows), abs(min_cols)
    grid[row][col] = '#'
    for dir, dist in zip(directions, distances):
        debug = 1
        for i in range(dist):
            if dir == 'R':
                col += 1
            elif dir == 'L':
                col -= 1
            elif dir == 'D':
                row += 1
            elif dir == 'U':
                row -= 1
            else:
                print("INCORRECT DIRECTION")

            grid[row][col] = '#'


    # Flood fill
    x0 = [abs(min_rows)+1, abs(min_cols) + 1]
    grid = floodFill(grid, x0)

    with open('grid.txt', 'w') as f:
        line_str = ''
        for line in grid:
            for val in line:
                line_str += val
            line_str += '\n'
            f.write(line_str)

    # Count size
    count = 0
    for row in grid:
        count += row.count('#')
        count += row.count('0')
    print(count)

'''
10307 is too low
'''

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
