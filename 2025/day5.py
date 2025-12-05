
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



if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt" 

    part1(file)
    # part2(file)