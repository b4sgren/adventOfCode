import numpy as np

def parseLines(data):
    winning_numbers = []
    my_numbers = []
    for line in data:
        vals = line.split(':')[1]
        vals2 = vals.split('|')

        nums = vals2[0].split()
        temp = [int(num) for num in nums]
        temp.sort()
        winning_numbers.append(temp)

        nums = vals2[1].split()
        temp = [int(num) for num in nums]
        temp.sort()
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
    # with open('temp.txt', 'r') as f:
    with open('day4.txt', 'r') as f:
        data = f.readlines()

    winning_numbers, my_numbers = parseLines(data)
    num_cards = len(my_numbers)

    card_copies = {}
    for i in range(len(my_numbers)):
        card_copies[i] = 1  # each card has itself

    for i, (winning_nums, my_nums) in enumerate(zip(winning_numbers, my_numbers)):
        count = 0
        for my_num in my_nums:
            if my_num in winning_nums:
                count += 1
        debug = 1
        for j in range(count):
            if i+j+1 < num_cards:
                card_copies[i+j+1] += 1 * card_copies[i]  # multiply by how many cards there are currently
                debug = 1
        debug = 1

    vals = list(card_copies.values())
    print(np.sum(vals))

'''
Part 2 Notes:
5604889 is too low
'''


if __name__=="__main__":
    # part1()

    part2()
