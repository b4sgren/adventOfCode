
def getLargestVoltage1(line):
    first_digit = max(line[:-2])
    idx1 = line.index(first_digit)

    second_digit = max(line[idx1+1:])
    
    return int(first_digit +  second_digit)

def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    totalVoltage = 0
    for line in data:
        largestVoltage = getLargestVoltage1(line)
        totalVoltage += largestVoltage
    
    print(totalVoltage)


if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt" 

    part1(file)
    # part2(file)  