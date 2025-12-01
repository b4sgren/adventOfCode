import math

def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    x = 50
    num_zeros = 0
    for line in data:
        dir = line[0]
        clicks = float(line[1:])
        if dir == 'R':
            x = (x + clicks) % 100
        if dir == 'L':
            x = (x - clicks) % 100
            if x < 0:
                x = 100 + x
        
        if x == 0:
            num_zeros += 1
    
    print(num_zeros)
    
def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    x = 50
    num_zeros = 0
    num_zeros2 = 0
    for line in data:
        dir = line[0]
        clicks = int(line[1:])
        num_zeros += math.floor(clicks / 100)
        num_zeros2 += math.floor(clicks / 100)
        clicks %= 100
        if dir == 'R':
            xp = (x + clicks) % 100
            if xp < x:
                num_zeros += 1
            x = xp
        if dir == 'L':
            x0 = x
            xp = (x - clicks) % 100
            if (xp > x and x0 != 0) or xp == 0:
                num_zeros += 1
            x = xp

    print(num_zeros)



if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt"

    part1(file)  # 1182
    part2(file)  # 6907
