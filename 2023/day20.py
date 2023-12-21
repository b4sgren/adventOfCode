import numpy as np

class FlipFlopModule:
    def __init__(self, targets):
        self.state = 0  # Initially off
        self.targets = targets

    def inputPulse(self, sender, pulse_type):
        if pulse_type == 1:
            return None
        self.state = 1 - self.state  # flip state
        return self.state  # if on send high pulse, if off send lo    # NEED TO INITIALIZE ALL INPUTS IN CONJUCTION MODULES BEFORE I DO THIS LOOPw

    def addInput(self, sender):
        pass

class ConjuctionModule:
    def __init__(self, targets):
        # default remember a low pulse
        self.inputs = {}  # sender is key, pulse type is value
        self.targets = targets

    def addInput(self, sender):
        self.inputs[sender] = 0

    def inputPulse(self, sender, pulse_type):
        if sender not in  self.inputs.keys():
            self.inputs[sender] = 0
        self.inputs[sender] = pulse_type

        values = np.array(list(self.inputs.values()))
        if np.all(values == 1):
            return 0  # send low pulse
        else:
            return 1  # send high pulse

class BroadcasterModule:
    def __init__(self, targets):
        self.targets = targets

    # Outputs the pulse type passed on
    def inputPulse(self, sender, pulse_type):
        return pulse_type

    def addInput(self, sender):
        pass

def parseData(data):
    src_target_map = {}
    module_map = {}

    for line in data:
        line = ''.join(line.split())  # remove white space
        vals = line.split('->')
        targets = vals[1].split(',')
        if vals[0][0] == 'b':
            # broadcaster
            module_id = vals[0]
            module_map[module_id] = BroadcasterModule(targets)
        elif vals[0][0] == '%':
            # flip flop
            module_id = vals[0][1:]
            module_map[module_id] = FlipFlopModule(targets)
        elif vals[0][0] == '&':
            # conjuction module
            module_id = vals[0][1:]
            module_map[module_id] = ConjuctionModule(targets)

        src_target_map[module_id] = targets

    return module_map


def part1():
    # with open('temp2.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        data = f.readlines()

    module_map = parseData(data)


    # NEED TO INITIALIZE ALL INPUTS IN CONJUCTION MODULES BEFORE I DO THIS LOOP
    for key, module in module_map.items():
        for target in module.targets:
            if target in module_map.keys():
                module_map[target].addInput(key)

    # Test input 2 is off on first pass
    num_pulses = {0:0, 1:0}
    for i in range(1000):
        pulse_queue = []  # tuples of (sender, receiver, pulse)
        pulse = module_map['broadcaster'].inputPulse('button', 0)
        num_pulses[0] += 1
        for target in module_map['broadcaster'].targets:
            pulse_queue.append(('broadcaster', target, pulse))

        while len(pulse_queue) > 0:
            sender, target, pulse = pulse_queue.pop(0)
            # print(sender, pulse, target)
            num_pulses[pulse] += 1  # increment pulses sent

            # Verify the target actually does something
            if target not in module_map.keys():
                continue

            output_pulse = module_map[target].inputPulse(sender, pulse)
            if output_pulse is None:
                continue
            for next_target in module_map[target].targets:
                pulse_queue.append((target, next_target, output_pulse))

    print(num_pulses[0] * num_pulses[1])  # Each is off by one

def part2():
    # with open('temp2.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        data = f.readlines()

    module_map = parseData(data)


    # NEED TO INITIALIZE ALL INPUTS IN CONJUCTION MODULES BEFORE I DO THIS LOOP
    for key, module in module_map.items():
        for target in module.targets:
            if target in module_map.keys():
                module_map[target].addInput(key)

    # Test input 2 is off on first pass
    bh, jf, sh, mz = -1, -1, -1, -1
    num_pulses = {0:0, 1:0}
    counter = 0
    flag = True
    while flag:
        pulse_queue = []  # tuples of (sender, receiver, pulse)
        pulse = module_map['broadcaster'].inputPulse('button', 0)
        num_pulses[0] += 1
        counter += 1
        for target in module_map['broadcaster'].targets:
            pulse_queue.append(('broadcaster', target, pulse))

        while len(pulse_queue) > 0:
            sender, target, pulse = pulse_queue.pop(0)
            # if target == 'bh' or target == 'jf' or target == 'sh' or target == 'mz':
                # debug = 1
            if sender == 'bh' and bh < 0 and pulse == 1:
                bh = counter
            if sender == 'jf' and jf < 0 and pulse == 1:
                jf = counter
            if sender == 'sh' and sh < 0 and pulse == 1:
                sh = counter
            if sender == 'mz' and mz < 0 and pulse == 1:
                mz = counter

            if bh > 0 and jf > 0 and sh > 0 and mz > 0:
                flag = False
                break

            # print(sender, pulse, target)
            num_pulses[pulse] += 1  # increment pulses sent

            # Verify the target actually does something
            if target not in module_map.keys():
                continue

            output_pulse = module_map[target].inputPulse(sender, pulse)
            if output_pulse is None:
                continue
            for next_target in module_map[target].targets:
                pulse_queue.append((target, next_target, output_pulse))

    # print(counter)  # Each is off by one
    print(bh, jf, sh, mz)
    print(bh * jf * sh * mz)


if __name__=="__main__":
    part1()

    part2()
