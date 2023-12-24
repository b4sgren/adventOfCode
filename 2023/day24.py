import numpy as np

def parseData(data):
    positions, velocities = {}, {}
    for i, line in enumerate(data):
        vals = line[:-1].split('@')
        nums = vals[0].split(',')
        pos = np.array([int(n) for n in nums], dtype=np.float32)
        nums = vals[1].split(',')
        vel = np.array([int(n) for n in nums], dtype=np.float32)

        positions[i] = pos
        velocities[i] = vel

    return positions, velocities

def findIntersectionsXY(positions, velocities):
    intersection_pts = []
    for i in range(len(positions)-1):
        p1, v1 = positions[i], velocities[i]
        vel_ratio_1 = v1[1]/v1[0]
        for j in range(i+1, len(positions)):
            p2, v2 = positions[j], velocities[j]
            vel_ratio_2 = v2[1]/v2[0]

            if vel_ratio_1 == vel_ratio_2:
                continue

            A = np.array([[-vel_ratio_1, 1], [-vel_ratio_2, 1]])
            b = np.array([p1[1] - vel_ratio_1*p1[0], p2[1] - vel_ratio_2*p2[0]])

            pt = np.linalg.solve(A, b)

            # Determine if time is in the future or the past
            t1 = (pt - p1[:2])/v1[:2]
            t2 = (pt - p2[:2])/v2[:2]
            if t1[0] > 0 and t2[0] > 0:
                intersection_pts.append(pt)


    return intersection_pts




def part1():
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    positions, velocities = parseData(data)

    intersection_pts = findIntersectionsXY(positions, velocities)

    bnds_x = [7, 27]
    bnds_y = [7, 27]
    counter = 0
    for pt in intersection_pts:
        if bnds_x[0] <= pt[0] <= bnds_x[1] and bnds_y[0] <= pt[1] <= bnds_y[1]:
            counter += 1

    print(counter)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
