import sys
import numpy as np
from copy import deepcopy as copy

def part1():
    with open('day1.txt', 'r') as f:
        data = f.readlines()

    vals = []

    for str in data:
        num = ''
        for char in str:
            if char.isdigit():
                num += char
                break
        for char in reversed(str):
            if char.isdigit():
                num += char
                break
        vals.append(int(num))

    print(np.sum(vals))

def part2():
    # with open('day1.txt', 'r') as f:
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    vals = []

    nums_text = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']  #, '1', '2', '3', '4', '5', '6', '7', '8', '9']
    nums_digit_map = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for str in data:
        str_orig = copy(str)
        num = ''
        for i, temp in enumerate(nums_text):
            idx = str.find(temp)
            while(idx > -1):  # For duplicate numbers
                str = str[:idx+1] + nums_digit_map[i] + str[idx+2:]
                idx = str.find(temp)

        for char in str:
            if char.isdigit():
                num += char
                break
        for char in reversed(str):
            if char.isdigit():
                num += char
                break

        # max_id = np.argmax(idxs)
        # max_val = np.max(idxs)
        # min_id = -1
        # min_val = 1000
        # for i, id in enumerate(idxs):
        #     if id > -1 and id < min_val:
        #         min_id = i
        #         min_val = id
        # num += nums_digit_map[min_id]
        # num += nums_digit_map[max_id]
        # if max_val < min_val or max_val == min_val:
        #     debug = 1
        # # if max_id != min_id:
        # #     num += nums_digit_map[max_id]

        vals.append(int(num))

    print(np.sum(vals))


if __name__=="__main__":
    # part1()

    part2()
