from copy import deepcopy

def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    # pad around to not worry about overflow/underflow
    for i in range(len(data)):
        # strip new line off
        data[i] = '.' + data[i][:-1] + '.'

    num_cols = len(data[0])
    data.insert(0, '.'*(num_cols))
    data.append('.' * (num_cols))
    data2 = deepcopy(data)
    num_rows = len(data)


    num_papers_to_move = 0
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            if data[i][j] != '@':
                continue

            num_surrounding_papers = 0
            im1 = i-1
            ip1 = i+1
            jm1 = j-1
            jp1 = j+1

            num_surrounding_papers += 1 if data[im1][jm1] == '@' else 0
            num_surrounding_papers += 1 if data[im1][j] == '@' else 0
            num_surrounding_papers += 1 if data[im1][jp1] == '@' else 0
            num_surrounding_papers += 1 if data[i][jm1] == '@' else 0
            num_surrounding_papers += 1 if data[i][jp1] == '@' else 0
            num_surrounding_papers += 1 if data[ip1][jm1] == '@' else 0
            num_surrounding_papers += 1 if data[ip1][j] == '@' else 0
            num_surrounding_papers += 1 if data[ip1][jp1] == '@' else 0

            if num_surrounding_papers < 4:
                num_papers_to_move += 1
    
    for i in range(len(data2)):
        print(data2[i])
    print(num_papers_to_move)


if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt" 

    part1(file)
    # part2(file)