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

def sorting_func2(val):
    card_order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    id = []
    for char in val:
        id.append(card_order.index(char))

    return id

def sortHands2(hands):
    hands['5'].sort(key = sorting_func2 )
    hands['4'].sort(key = sorting_func2 )
    hands['FH'].sort(key = sorting_func2 )
    hands['3'].sort(key = sorting_func2 )  # ok
    hands['2P'].sort(key = sorting_func2 )  # ok
    hands['P'].sort(key = sorting_func2 )  # ok
    hands['HC'].sort(key = sorting_func2 )  # Ok, i think

    return hands


def part2():
    # with open('temp.txt', 'r') as f:
    with open('day7.txt', 'r') as f:
        data = f.readlines()
    hands = parseData(data)

    hands_dict = {'5':[], '4':[], 'FH':[], '3':[], '2P':[], 'P':[], 'HC':[]}
    for hand, value in hands.items():
        hand_count = Counter(hand)
        unique_cards = len(hand_count)
        counter_dict[hand] = hand_count
        num_jokers = hand.count('J')



        # Issue with this I think
        common_card = hand_count.most_common()[0][0]
        if common_card == 'J' and unique_cards == 1:
            common_card_count = 0
        elif common_card == 'J':
            common_card = hand_count.most_common()[1][0]
            common_card_count = hand_count[common_card]
        else:
            common_card_count = hand_count[common_card]

        if common_card_count + num_jokers == 5:
            hands_dict['5'].append(hand)
        elif common_card_count + num_jokers == 4:
            hands_dict['4'].append(hand)
        elif common_card_count + num_jokers == 3:
            # 3 or FH
            if unique_cards == 4: # HC with 2 jokers or pair
                hands_dict['3'].append(hand)
            elif unique_cards == 3 and num_jokers == 0:
                hands_dict['3'].append(hand)
            elif unique_cards >= 2: # 2P with 1 joker, or FH
                hands_dict['FH'].append(hand)
        elif common_card_count + num_jokers == 2:
            # P or 2P
            if unique_cards >= 4:  # HC with 1 joker
                hands_dict['P'].append(hand)
            elif unique_cards >= 3: # 2P w/ no jokers
                hands_dict['2P'].append(hand)
        else:  # No jokers
            hands_dict['HC'].append(hand)

    hands_dict = sortHands2(hands_dict)

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
        print(hand, val)
        sum += (i+1) * val

    print(sum)


if __name__=="__main__":
    # part1()

    part2()
