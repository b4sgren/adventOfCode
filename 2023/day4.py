import numpy as np

def parseLines(data):
    winning_numbers = []
    my_numbers = []
    for line in data:
        vals = line.split(':')[1]
        vals2 = vals.split('|')

        nums = vals2[0].split()
        temp = [int(num) for num in nums]
        winning_numbers.append(temp)

        nums = vals2[1].split()
        temp = [int(num) for num in nums]
        my_numbers.append(temp)

    return winning_numbers, my_numbers

def part1():
    # with open('temp.txt', 'r') as f:
    with open('day4.txt', 'r') as f:
        data = f.readlines()

    winning_numbers, my_numbers = parseLines(data)

    sum = 0
    for winning_nums, my_nums in zip(winning_numbers, my_numbers):
        count = 0
        for my_num in my_nums:
            if my_num in winning_nums:
                count += 1
        if count > 0:
            sum += 2**(count-1)

    print(sum)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
