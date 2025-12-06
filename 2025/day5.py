
def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    # Parse data
    ranges = []
    values = []
    for line in data:
        if len(line) == 0 or line == '\n':
            continue
        if '-' in line:
            vals = line.split('-')
            ranges.append([int(vals[0]), int(vals[1])])
        else:
            values.append(int(line))
    
    num_valid = 0
    for val in values:
        for [r1, r2] in ranges:
            if val >= r1 and val <= r2:
                num_valid += 1
                break
    
    print(num_valid)

def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    # Parse data
    ranges = []
    for line in data:
        if '-' in line:
            vals = line.split('-')
            ranges.append([int(vals[0]), int(vals[1])])
    

    ranges.sort()
    ids_to_remove = []
    for i in range(1, len(ranges)):
        ri = ranges[i]
        rim1 = ranges[i-1]
        if ri[0] <= rim1[1] and ri[1] <= rim1[1]:
            ids_to_remove.append(i)
            continue
        if ri[0] <= rim1[1]:
            ranges[i][0] = rim1[1] + 1
            print(ranges[i])
    
    for id in reversed(ids_to_remove):
        ranges.remove(ranges[id])

    total = 0
    for [r1, r2] in ranges:
        total += r2 - r1 + 1
    
    print(total)

if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt"  

    part1(file)
    part2(file)