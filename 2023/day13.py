
part1_hcounts = []
part1_vcounts = []

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

def findLineOfSymmetry(pattern, part1 = True):
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
    # with open('input.txt', 'r') as f:
        data = f.readlines()

    patterns = parseData(data)

    count = 0
    for pattern in patterns:
        count += findLineOfSymmetry(pattern)

    print(count)

def identifyKeyLocation(pattern):
    count = 0

    num_cols = len(pattern[0])
    # Check symmetry across a vertical line
    for line in range(1, num_cols):
        diffs = 0
        ids = []
        for r, row in enumerate(pattern):
            first_half = row[:line]
            first_half.reverse()
            second_half = row[line:]
            s1 = len(first_half)
            s2 = len(second_half)
            size = min(s1, s2)
            diff = [n1==n2 for n1,n2 in zip(first_half, second_half)]
            if diff.count(False) == 1:
                idx = diff.index(False)
                ids.append([r, line])
            diffs += diff.count(False)
            if diffs > 1:
                break

        if diffs == 1:
            break

    if len(ids) == 1:
        return size


    num_rows = len(pattern)
    for line in range(1, num_rows):
        top_half = pattern[:line]
        top_half.reverse()
        bottom_half = pattern[line:]
        s1 = len(top_half)
        s2 = len(bottom_half)
        size = min(s1, s2)

        diffs = 0
        ids = []
        for i in range(size):
            diff = [n1==n2 for n1,n2 in zip(top_half[i], bottom_half[i])]
            if diff.count(False) == 1:
                idx = diff.index(False)
                ids.append([line+i, idx])  # not right. Either top_half[i] or bottom half[i]
            diffs += diff.count(False)
            if diffs > 1:
                break

        if diffs == 1:
            return 100*size
            break

    return 0


def part2():
    with open('temp.txt', 'r') as f:
    # with open('input.txt', 'r') as f:
        data = f.readlines()

    patterns = parseData(data)

    count = 0
    for pattern in patterns:
        count += identifyKeyLocation(pattern)


    print(count)

if __name__=="__main__":
    part1()

    part2()
