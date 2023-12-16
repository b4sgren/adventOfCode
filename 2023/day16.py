
def getNextLocation(loc, grid_val):
    row, col, dir = loc
    next_loc = None
    if grid_val == '.':
        if dir == 0: col += 1
        elif dir == 1: row += 1
        elif dir == 2: col -= 1
        else: row -= 1
        next_loc = [(row, col, dir)]
    elif grid_val == '\\':
        if dir == 0: next_loc = [(row+1, col, 1)]
        elif dir == 1: next_loc = [(row, col+1, 0)]
        elif dir == 2: next_loc = [(row-1, col, 3)]
        else: next_loc = [(row, col-1, 2)]
    elif grid_val == '/':
        if dir == 0: next_loc = [(row-1, col, 3)]
        elif dir == 1: next_loc = [(row, col-1, 2)]
        elif dir == 2: next_loc = [(row+1, col, 1)]
        else: next_loc = [(row, col+1, 0)]
    elif grid_val == '|':
        if dir == 1 or dir == 3:
            if dir == 0: col += 1
            elif dir == 1: row += 1
            elif dir == 2: col -= 1
            else: row -= 1
            next_loc = [(row, col, dir)]
        else:
            # Turning to go north means coming from the south
            next_loc = [(row+1, col, 1), (row-1, col, 3)]
    elif grid_val == '-':
        if dir == 0 or dir == 2:
            if dir == 0: col += 1
            elif dir == 1: row += 1
            elif dir == 2: col -= 1
            else: row -= 1
            next_loc = [(row, col, dir)]
        else:
            next_loc = [(row, col+1, 0), (row, col-1, 2)]
    else:
        print("INVALID GRID_VAL", loc, grid_val)

    return next_loc

def traverseGrid(grid, locations, loc):
    # Cycle reached
    if loc in locations:
        return grid, locations

    locations.add(loc)
    if grid[loc[0]][loc[1]] == '.':
        loc = getNextLocation(loc)

def part1():
    grid = []
    with open('temp.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            grid.append(list(line)[:-1])

    # Directions: 0 = from left, 1 = from north, 2 = from right, 3 = from south
    locations= set()  # Filled with tuple of (row, col, direction in)
    loc = (0, 0, 0)

    locations = traverseGrid(grid, locations, loc)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
