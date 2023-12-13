
def parseData(data):
    patterns = []
    pattern = []
    for line in data:
        if line == "\n":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(list(line)[:-1])
    patterns.append(pattern)

    return patterns

def findLineOfSymmetry(pattern):
    count = 0

    num_cols = len(pattern[0])
    # Check symmetry across a vertical line
    for line in range(1, num_cols):
        is_symmetric = True
        for row in pattern:
            first_half = row[:line]
            first_half.reverse()
            second_half = row[line:]
            s1 = len(first_half)
            s2 = len(second_half)
            size = min(s1, s2)
            if first_half[:size] != second_half[:size]:
                is_symmetric = False
                break

        if is_symmetric:
            count += line
            break


    num_rows = len(pattern)
    for line in range(1, num_rows):
        top_half = pattern[:line]
        top_half.reverse()
        bottom_half = pattern[line:]
        s1 = len(top_half)
        s2 = len(bottom_half)
        size = min(s1, s2)

        is_symmetric = True
        for i in range(size):
            if top_half[i] != bottom_half[i]:
                is_symmetric = False
                break

        if is_symmetric:
            count += 100*line

    return count

def part1():
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    patterns = parseData(data)

    count = 0
    for pattern in patterns:
        count += findLineOfSymmetry(pattern)

    print(count)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
