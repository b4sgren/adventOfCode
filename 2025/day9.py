import numpy as np

def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    corners = []
    for line in data:
        vals = line.split(',')
        corners.append([float(vals[0]), float(vals[1])])
    
    corners = np.array(corners)
    x = corners[:, 0]
    y = corners[:, 1]

    dx = np.abs(x - x[:, np.newaxis]) + 1
    dy = np.abs(y - y[:, np.newaxis]) + 1

    area = dx * dy

    print(np.max(np.abs(area)))

    max_area = 0
    for i in range(len(corners)-1):
        for j in range(i+1, len(corners)):
            x1 = x[i]
            x2 = x[j]
            y1 = y[i]
            y2 = y[j]
            area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
            if area > max_area:
                max_area = area
    
    print(max_area)


if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt" 

    part1(file)
    # part2(file)
