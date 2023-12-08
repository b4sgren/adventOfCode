from collections import Counter

counter_dict = {}

def parseData(data):
    hands = {}

    # POSSIBLE ISSUES FOR DUPLICATE HANDS!!!
    for line in data:
        vals = line.split()
        res = ''.join(sorted(vals[0]))
        hands[str(res)] = int(vals[1])

    return hands

def sorting_func(val):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    # card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    global counter_dict
    id = []
    for pair in counter_dict[val].most_common():
        char = pair[0]
        id.append(card_order.index(char))

    return id

def sorting_func2(val):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    # card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    global counter_dict
    id = []
    for pair in counter_dict[val].most_common():
        char = pair[0]
        id.append(card_order.index(char))

    return id

def sorting_funcHC(val):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    # card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    global counter_dict
    id = []
    for pair in counter_dict[val].most_common():
        char = pair[0]
        id.append(card_order.index(char))

    id.sort()

    return id

def sorting_func3(val):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    global counter_dict
    id = [card_order.index(counter_dict[val].most_common()[0][0])]
    rest = []
    for pair in counter_dict[val].most_common()[1:]:
        char = pair[0]
        rest.append(card_order.index(char))
    rest.sort()
    id.extend(rest)

    return id

def sorting_func2P(val):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    global counter_dict
    id = [card_order.index(counter_dict[val].most_common()[0][0])]
    id = [card_order.index(counter_dict[val].most_common()[1][0])]
    id.sort()
    id.append(card_order.index(counter_dict[val].most_common()[-1][0]))

    return id

def sortHands(hands, counter_dict):

    hands['5'].sort(key = sorting_func )
    hands['4'].sort(key = sorting_func )
    hands['FH'].sort(key = sorting_func )
    hands['3'].sort(key = sorting_func3 )  # Diff func
    hands['2P'].sort(key = sorting_func2P )  # Diff func
    hands['P'].sort(key = sorting_func3 )  # DIff func
    hands['HC'].sort(key = sorting_funcHC )  # Diff func
    debug = 1

    return hands

def part1():
    with open('temp.txt', 'r') as f:
        data = f.readlines()
    hands = parseData(data)

    hands_dict = {'5':[], '4':[], 'FH':[], '3':[], '2P':[], 'P':[], 'HC':[]}
    # counter_dict = {}
    for hand, value in hands.items():
        hand_count = Counter(hand)
        unique_cards = len(hand_count)
        counter_dict[hand] = hand_count

        if unique_cards == 1:
            hands_dict['5'].append(hand)
        elif unique_cards == 2:
            if hand_count.most_common()[0][1] == 4:
                hands_dict['4'].append(hand)
            else:
                hands_dict['FH'].append(hand)
        elif unique_cards == 3:
            if hand_count.most_common()[0][1] == 3:
                hands_dict['3'].append(hand)
            else:
                hands_dict['2P'].append(hand)
        elif unique_cards == 4:
            hands_dict['P'].append(hand)
        else:
            hands_dict['HC'].append(hand)

    hands_dict = sortHands(hands_dict, counter_dict)

    hand_order = []
    hand_order.extend(hands_dict['HC'])
    hand_order.extend(hands_dict['P'])
    hand_order.extend(hands_dict['2P'])
    hand_order.extend(hands_dict['3'])
    hand_order.extend(hands_dict['FH'])
    hand_order.extend(hands_dict['4'])
    hand_order.extend(hands_dict['5'])

    sum = 0
    for i, hand in enumerate(hand_order):
        val = hands[hand]
        sum += (i+1) * val

    print(sum)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
