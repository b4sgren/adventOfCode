import numpy as np
import scipy.linalg as spl
from itertools import combinations, product
import math

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
    
# Not just Vh
def getFloatSolution(buttons, joltage):
    A = np.hstack([c[:, None] for c in buttons])
    U, s, Vh = spl.svd(A, full_matrices=False)
    t1 = U.T @ joltage
    t2 = np.diag(1/s) @ t1
    # res = Vh[:len(s), :].T @ t2
    res = Vh.T @ t2

    return res

def getRoundedCombos(res):
    lists = [[math.floor(res[i]), math.ceil(res[i])] for i in range(len(res))]
    result = list(product(*lists))

    return result

# requires multiple button presses
def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    lights = []
    button_groups = []
    joltage_groups = []
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

        nums = groups[-1][1:-1].split(',')
        joltage = [int(v) for v in nums]
        joltage_groups.append(np.array(joltage))

    
    total_presses = 0
    for i in range(len(lights)):
        res = getFloatSolution(button_groups[i], joltage_groups[i])
        combos = getRoundedCombos(res)
        combos.sort(key=np.sum)

        for combo in combos:
            joltage_res = np.zeros(len(joltage_groups[i]))
            for j, num in enumerate(combo):
                joltage_res += button_groups[i][j] * num
            on_res = np.mod(joltage_res, 2)

            if (joltage_res == joltage_groups[i]).all() and (on_res == lights[i]).all():
                total_presses += np.sum(combo)
                break
    
    print(total_presses)



if __name__=="__main__":
    file = "test_input.txt"
    # file = "input.txt"

    part1(file)
    part2(file)
