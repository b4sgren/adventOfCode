
def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    num_problems = len(data[0].split())
    problems = [[] for i in range(num_problems)]
    for line in data:
        vals = line.split()
        if '*' in vals:
            operators = vals
        else:
            for i in range(num_problems):
                problems[i].append(int(vals[i]))
    
    total = 0
    for i in range(num_problems):
        if operators[i] == '*':
            problem_val = 1
            for num in problems[i]:
                problem_val *= num 
        else:
            problem_val = 0
            for num in problems[i]:
                problem_val += num
        total += problem_val
    
    print(total)
    

if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt"  

    part1(file)
    # part2(file)
