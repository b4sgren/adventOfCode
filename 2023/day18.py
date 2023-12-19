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
    queue = [loc]

    while len(queue) > 0:
        loc = queue.pop()
        r, c = loc
        if grid[r][c] == '#' or grid[r][c] == '0':
            continue

        grid[loc[0]][loc[1]] = '0'
        queue.append([r+1, c])
        queue.append([r-1, c])
        queue.append([r, c+1])
        queue.append([r, c-1])

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
    x0 = [abs(min_rows) + 1, abs(min_cols) + 1]
    grid = floodFill(grid, x0)

    with open('grid.txt', 'w') as f:
        for line in grid:
            line_str = ''
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

def colors2Instructions(colors):
    directions, distances = [], []
    for color in colors:
        char = color[-1]
        if char == '0': directions.append('R')
        if char == '1': directions.append('D')
        if char == '2': directions.append('L')
        if char == '3': directions.append('U')

        distances.append(int(color[1:-1], 16))

    return directions, distances

def part2():
    # with open('temp2.txt', 'r') as f:
    with open('input2.txt', 'r') as f:
        data = f.readlines()

    directions, distances, colors = parseData(data)
    directions, distances = colors2Instructions(colors)

    # need to detect areas
    r, c = 0, 0
    corners = [[r, c]]
    perimeter = 0
    for dir, dist in zip(directions, distances):
        if dir == 'R':
            c += dist
        elif dir == 'L':
            c -= dist
        elif dir == 'U':
            r -= dist
        elif dir == 'D':
            r += dist
        else:
            print("BAD DIRECTION")
        perimeter += dist
        corners.append([r, c])


    # Calculate area using the shoelace algorithm
    # Follow this with picks theorem: A = I + B/2 - 1. Then solve for I
    sum1 = 0
    sum2 = 0
    for i in range(len(corners)):
        idx = (i+1) % len(corners)  # cover the last case when it wraps
        sum1 += int(corners[i][0] * corners[idx][1])
        sum2 += int(corners[idx][0] * corners[i][1])
    area = abs(int(0.5 * (sum1-sum2)))

    area = area + perimeter/2 + 1

    print(area)

'''
96556165374331  not right
'''


if __name__=="__main__":
    part1()

    part2()
