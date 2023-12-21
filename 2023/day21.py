
def parseData(data):
    grid = []
    for r, line in enumerate(data):
        temp = ['#']
        temp.extend(list(line[:-1]))
        temp.append('#')
        grid.append(temp)
        if 'S' in line:
            c = line.find('S')
            start_id = [r+1, c+1]

    grid.append(['#'] * len(grid[0]))
    grid.insert(0, ['#'] * len(grid[0]))

    return grid, start_id

def part1():
    # with open('temp.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        data = f.readlines()

    grid , start_id = parseData(data)

    num_steps = 64
    queue = [start_id]  # of of possible current locations
    for i in range(num_steps):
        next_queue = []  # queue of possible next locations
        while len(queue) > 0:
            location = queue.pop(0)
            row, col = location

            if grid[row+1][col] != '#':
                if [row+1, col] not in next_queue:
                    next_queue.append([row+1, col])
            if grid[row-1][col] != '#':
                if [row-1, col] not in next_queue:
                    next_queue.append([row-1, col])
            if grid[row][col+1] != '#':
                if [row, col+1] not in next_queue:
                    next_queue.append([row, col+1])
            if grid[row][col-1] != '#':
                if [row, col-1] not in next_queue:
                    next_queue.append([row, col-1])

        queue = next_queue
        next_queue = []

    print(len(queue))



def part2():
    with open('temp.txt', 'r') as f:
    # with open('input.txt', 'r') as f:
        data = f.readlines()

    grid , start_id = parseData(data)
    # Remove the padding for easier wrapping
    grid = grid[1:-1]
    grid = [line[1:-1] for line in grid]
    start_id = [start_id[0]-1, start_id[1]-1]

    num_rows = len(grid)
    num_cols = len(grid[0])
    num_steps = 26501365
    queue = [tuple(start_id)]  # of of possible current locations
    for i in range(num_steps):
        next_queue = []  # queue of possible next locations
        while len(queue) > 0:
            location = queue.pop(0)
            row, col = location

            if grid[(row+1)%num_rows][col] != '#':
                if ((row+1)%num_rows, col) not in next_queue:
                    next_queue.append(((row+1)%num_rows, col))
            if grid[(row-1)%num_rows][col] != '#':
                if ((row-1)%num_rows, col) not in next_queue:
                    next_queue.append(((row-1)%num_rows, col))
            if grid[row][(col+1)%num_cols] != '#':
                if (row, (col+1)%num_cols) not in next_queue:
                    next_queue.append((row, (col+1)%num_cols))
            if grid[row][(col-1)%num_cols] != '#':
                if (row, (col-1)%num_cols) not in next_queue:
                    next_queue.append((row, (col-1)%num_cols))

        queue = next_queue
        next_queue = []

    print(len(queue))


if __name__=="__main__":
    # part1()

    part2()
