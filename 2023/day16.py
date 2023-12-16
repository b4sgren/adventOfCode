import sys
sys.setrecursionlimit(10000)

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

def traverseGrid(grid, locations, current_location):
    # Cycle reached
    if current_location is None or current_location in locations:
        return locations
    # Outside of grid
    if current_location[0] >= len(grid) or current_location[1] >= len(grid[0]) or current_location[0] < 0 or current_location[1] < 0:
        return locations

    # Add location to places visited
    locations.add(current_location)
    tile = grid[current_location[0]][current_location[1]]
    next_locations = getNextLocation(current_location, tile)
    # For whatever reason
    if next_locations is None:
        return locations

    # Recursion
    locations = traverseGrid(grid, locations, next_locations[0])
    if len(next_locations) == 2:
        locations = traverseGrid(grid, locations, next_locations[1])

    return locations


def part1():
    grid = []
    with open('input.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            grid.append(list(line)[:-1])

    # Directions: 0 = from left, 1 = from north, 2 = from right, 3 = from south
    directed_locations= set()  # Filled with tuple of (row, col, direction in)
    loc = (0, 0, 0)

    directed_locations = traverseGrid(grid, directed_locations, loc)

    locations = set()
    for dloc in directed_locations:
        loc = (dloc[0], dloc[1])
        if loc not in locations:
            locations.add(loc)

    print(len(locations))

    # for loc in locations:
    #     grid[loc[0]][loc[1]] = '#'

    # for line in grid: print(line)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
