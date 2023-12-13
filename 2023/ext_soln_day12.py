from functools import cache  # see decorator comment

@cache  # caches the inputs to function so its not called multiple times
def nbconf( record, groups ):

    # base case
    if len(groups) == 0: # more than # to place
        return 1 if '#' not in record else 0
    if sum(groups) + len(groups) - 1 > len(record): # not enough space for the #
        return 0

    # recursion
    if record[0] == '.': # if we start with a period. Call function on shorter string until it begins with ? or #
        return nbconf( record[1:], groups)

    nb = 0
    if record[0] == '?': # if ? is first
        nb += nbconf( record[1:], groups) # replace with a .

    # possibilities with first group of numbers at beginning
    # Verify no . in first group. At the end of first group we want a .
    # Place the entire first block at the beginning (required to start with a #)
    if '.' not in record[:groups[0]] and (len(record) <= groups[0] or (len(record) > groups[0] and record[groups[0]] != '#')):
            nb += nbconf( record[groups[0]+1:], groups[1:]   )

    return nb


somme = 0
with open('input.txt', 'r') as f:
    for line in f.read().splitlines():
        record, groups = line.split(' ')
        groups = [int(x) for x in groups.split(',')]
        somme += nbconf( tuple(record) , tuple(groups) ) # tuples pour pouvoir hasher...

print('Part 1 :', somme)

## Part 2
somme = 0
# with open('input.txt', 'r') as f:
with open('temp.txt', 'r') as f:
    for line in f.read().splitlines():
        record, groups = line.split(' ')
        record = (5*(record + '?'))[:-1] # attention, pas de ? à la fin
        groups = 5*[int(x) for x in groups.split(',')]
        somme += nbconf( tuple(record) , tuple(groups) )

print('Part 2 :', somme) #300ms on a crappy i5 :)
