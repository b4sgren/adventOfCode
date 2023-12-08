from collections import Counter

counter_dict = {}

def parseData(data):
    hands = {}

    for line in data:
        vals = line.split()
        res = vals[0]
        hands[str(res)] = int(vals[1])

    return hands

def sorting_func(val):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    global counter_dict
    id = []
    for char in val:
        id.append(card_order.index(char))

    return id

def sortHands(hands, counter_dict):
    hands['5'].sort(key = sorting_func )
    hands['4'].sort(key = sorting_func )
    hands['FH'].sort(key = sorting_func )
    hands['3'].sort(key = sorting_func )  # ok
    hands['2P'].sort(key = sorting_func )  # ok
    hands['P'].sort(key = sorting_func )  # ok
    hands['HC'].sort(key = sorting_func )  # Ok, i think

    return hands

def part1():
    # with open('temp.txt', 'r') as f:
    with open('day7.txt', 'r') as f:
        data = f.readlines()
    hands = parseData(data)

    hands_dict = {'5':[], '4':[], 'FH':[], '3':[], '2P':[], 'P':[], 'HC':[]}
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
