
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
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    grid , start_id = parseData(data)

    num_steps = 6
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
    pass

if __name__=="__main__":
    part1()

    part2()
