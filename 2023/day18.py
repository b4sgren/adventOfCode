
def parseData(data):
    directions, distances, colors = [], [], []
    for line in data:
        vals = line[:-1].split()
        directions.append(vals[0])
        distances.append(int(vals[1]))
        colors.append(vals[2][1:-1])

    return directions, distances, colors

def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    directions, distances, colors = parseData(data)

    # Get max rows/cols. Assume it won't go negative
    max_rows = 1
    net_rows = 0
    max_cols = 1
    net_cols = 0
    for dir, dist in zip(directions, distances):
        if dir == 'D':
            max_rows += dist
            net_rows += dist
        elif dir == 'U':
            net_rows -= dist
        elif dir == 'R':
            max_cols += dist
            net_cols += dist
        elif dir == 'L':
            net_cols -= dist

    # Outline the loop
    grid = [['.' for i in range(max_cols)] for _ in range(max_rows)]
    grid[0][0] = '#'
    row, col = 0, 0
    for dir, dist in zip(directions, distances):
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

    for line in grid:
        print(line)

    # Flood fill
    # grid = floodFill(grid)

    # Count size
    count = 0
    for row in grid:
        count += row.count('#')
    print(count)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
