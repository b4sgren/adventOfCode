import numpy as np
from itertools import combinations

def getAllCombos(buttons):
    n = len(buttons)
    result = []
    for k in range(1, n+1):
        temp = list(combinations(buttons, k))
        result.extend(temp)
    
    return result

def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    lights = []
    button_groups = []
    for line in data:
        groups = line.split()
        light = [1 if i == '#' else 0 for i in groups[0][1:-1]]
        lights.append(np.array(light))

        num_buttons = len(light)

        buttons = []
        for i in range(1, len(groups)-1):
            nums = groups[i][1:-1].split(',')
            b0 = np.zeros(num_buttons)
            for num in nums:
                b0[int(num)] = 1
            buttons.append(b0)
        button_groups.append(buttons)
    
    total_presses = 0
    for i in range(len(lights)):
        combos = getAllCombos(button_groups[i])
        for combo in combos:
            res = np.zeros(lights[i].size)
            for c in combo:
                res += c
            res = np.mod(res, 2)
            if (res == lights[i]).all():
                total_presses += len(combo)
                break
    
    print(total_presses)
    


if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt"

    part1(file)
    # part2(file)
