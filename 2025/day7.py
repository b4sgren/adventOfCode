
def padData(data):
    for i in range(len(data)):
        # strip new line off
        data[i] = '.' + data[i][:-1] + '.'

    num_cols = len(data[0])
    data.insert(0, '.'*(num_cols))
    data.append('.' * (num_cols))

    for i in range(len(data)):
        data[i] = list(data[i])

    return data

def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    data = padData(data)

    id = data[1].index('S')
    data[1][id] = '|'

    n = len(data[0])-1
    num_splits = 0
    for i in range(2, len(data) - 1):
        for j in range(1, n):
            if data[i][j] == '.' and data[i-1][j] == '|':
                data[i][j] = '|'

            if data[i][j] == '^' and data[i-1][j] == '|':
                if data[i][j-1] == '.' or data[i][j+1] == '.':
                    num_splits += 1
                if data[i][j-1] == '.':
                    data[i][j-1] = '|'
                if data[i][j+1] == '.':
                    data[i][j+1] = '|'
    
    print(num_splits)

num_solutions = {}

def solveSubProblem(data, index):
    global num_solutions
    if index in num_solutions.keys():
        return num_solutions[index]
    if index[0] == len(data)-1:
        num_solutions[index] = 1
        return num_solutions[index]
    
    row, column = index
    if data[row+1][column] == '^':
        data[row+1][column-1] = '|'
        num_solutions[index] = solveSubProblem(data, (row+1, column-1))
        data[row+1][column-1] = '.'
        data[row+1][column+1] = '|'
        num_solutions[index] += solveSubProblem(data, (row+1, column+1))
        debug = 1
    else:
        data[row+1][column] = '|'
        num_solutions[index] = solveSubProblem(data, (row+1, column))


    return num_solutions[index]


# Requires dynamic programming
def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    data = padData(data)

    id = data[1].index('S')
    data[1][id] = '|'

    index = (1, id)
    solveSubProblem(data, index)

    print(num_solutions[index])



if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt"  

    part1(file)
    part2(file)
