
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

# Requires Dynamic programming
def getLargestVoltage2(line):
    idx = -1
    num = ''
    # print("====================================")
    for i in range(12, 0, -1):
        # print(line[idx+1:-i])
        if i > 1:
            digit = max(line[idx+1:-i])
        else:
            digit = max(line[idx+1:])
        idx = idx + 1 + line[idx+1:].index(digit)
        num = num + digit
    
    return int(num)


def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    totalVoltage = 0
    for line in data:
        largestVoltage = getLargestVoltage2(line)
        print(largestVoltage)
        totalVoltage += largestVoltage
    
    print(totalVoltage)


if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt" 

    part1(file)
    part2(file)  