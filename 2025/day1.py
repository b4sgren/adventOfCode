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
    for line in data:
        dir = line[0]
        clicks = float(line[1:])
        increase = math.floor(clicks/100)
        # print(clicks, increase)
        num_zeros += math.floor(clicks / 100)
        clicks %= 100
        if dir == 'R':
            xp = (x + clicks) % 100
            if xp < x:
                num_zeros += 1
            if xp == 0:
                num_zeros -= 1
            x = xp
        if dir == 'L':
            xp = (x - clicks) % 100
            if xp > x:
                num_zeros += 1
            if xp == 0:
                num_zeros -= 1
            x = xp
    
    # Count the times it passes zero but does not equal zero
    # Add result from the prior function
    print(num_zeros + 1182)



if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt" # 6913 is to high and 5723 is to low... 

    part1(file)
    part2(file)
