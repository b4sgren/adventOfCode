import sys
import numpy as np

def part1():
    with open('day2.txt', 'r') as f:
    # with open('temp.txt', 'r') as f:
        data = f.readlines()

    colors = ['red', 'blue', 'green']
    max_cubes_dict = {'red':12, 'green':13, 'blue':14}

    game_ids = []

    for z, line in enumerate(data):
        # look for number of cubes of each color
        # find number and see if correct
        tokens = line.split()
        game_id = tokens[1].split(':')[0]
        tokens = tokens[2:]

        is_possible = True

        for i in range(0, len(tokens), 2):
            num_cubes = int(tokens[i])
            for temp in colors:
                if tokens[i+1].find(temp) > -1:
                    color = temp
                    break

            if num_cubes > max_cubes_dict[color]:
                is_possible = False
                break
                debug = 1

        if is_possible:
            game_ids.append(int(game_id))


    print(np.sum(game_ids))

def part2():
    with open('day2.txt', 'r') as f:
    # with open('temp.txt', 'r') as f:
        data = f.readlines()

    colors = ['red', 'blue', 'green']

    powers = []

    for z, line in enumerate(data):
        max_cubes_dict = {'red':0, 'green':0, 'blue':0}
        tokens = line.split()
        tokens = tokens[2:]


        for i in range(0, len(tokens), 2):
            num_cubes = int(tokens[i])
            for temp in colors:
                if tokens[i+1].find(temp) > -1:
                    color = temp
                    break
            if num_cubes > max_cubes_dict[color]:
                max_cubes_dict[color] = num_cubes

        powers.append(np.product(list(max_cubes_dict.values())))


    print(np.sum(powers))

if __name__=="__main__":
    # part1()
    part2()
