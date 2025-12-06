
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

def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    # My parsing doesn't work. This will be the hard part
    # Replace all white space with 0's. Problem ends when a column has all zeros...
    data2 = []
    num_problems = len(data[0].split())
    problems = [[] for i in range(num_problems)]
    for i, line in enumerate(data):
        line = line.rstrip('\n')
        if '*' in line:
            vals = line.split()
            operators = vals
        else:
            line = line.replace(' ', 'x')
            data2.append(line)
    
    # Look for where columns are all 0
    problem_ids = []
    for i in range(len(data2[0])):
        is_zero = True
        for j in range(len(data2)):
            is_zero = is_zero and data2[j][i] == 'x'
        
        if is_zero:
            problem_ids.append(i)
    
    problems = []
    prev_id = 0
    for id in problem_ids:
        problem = []
        for j in range(len(data2)):
            problem.append(data2[j][prev_id:id])
        
        problems.append(problem)
        prev_id = id+1
    problem = []
    for j in range(len(data2)):
        problem.append(data2[j][prev_id:])
    problems.append(problem)

    total = 0
    for i in range(num_problems):
        problem = problems[i]
        K = len(problem[0])
        if operators[i] == '*':
            problem_val = 1
            for k in range(K): # iterate over digis
                num = ''
                for val in problem:
                    if val[k] != 'x':
                        num = num + val[k]
                    # create the number
                problem_val *= int(num)
        else:
            problem_val = 0
            for k in range(K): # iterate over digis
                num = ''
                for val in problem:
                    if val[k] != 'x':
                        num = num + val[k]
                    # create the number
                problem_val += int(num)


        total += problem_val
    
    print(total)


if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt"  

    part1(file)
    part2(file)
