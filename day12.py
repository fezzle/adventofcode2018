#!/usr/bin/env python3.6
import math

INDENT = 60

input = """initial state: ####....#...######.###.#...##....#.###.#.###.......###.##..##........##..#.#.#..##.##...####.#..##.#

..... => .
....# => .
...#. => .
...## => #
..#.. => .
..#.# => .
..##. => .
..### => .
.#... => #
.#..# => #
.#.#. => #
.#.## => #
.##.. => .
.##.# => .
.###. => #
.#### => #
#.... => .
#...# => .
#..#. => .
#..## => #
#.#.. => #
#.#.# => #
#.##. => #
#.### => #
##... => #
##..# => .
##.#. => .
##.## => #
###.. => .
###.# => .
####. => .
##### => #""".split("\n")

input = """initial state: #..#.#..##......###...###

..... => .
....# => .
...#. => .
...## => #
..#.. => #
..#.# => .
..##. => .
..### => .
.#... => #
.#..# => .
.#.#. => #
.#.## => #
.##.. => #
.##.# => .
.###. => .
.#### => #
#.... => .
#...# => .
#..#. => .
#..## => .
#.#.. => .
#.#.# => #
#.##. => .
#.### => #
##... => .
##..# => .
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
##### => .""".split("\n")


def str_to_binary(s):
    res = 0
    for c in s:
        res = res << 1
        if c == '#':
            res = res | 1
    return res

initial_state_str = input[0][len("initial state: "):]

rules = []
for rule_str in input[2:]:
    rule, result = rule_str.split(" => ", 1)
    assert len(rule) == 5
    rules.append((str_to_binary(rule), 1 if result == '#' else 0))

def print_binary(v):
    for i in range(int(math.log(current_state, 2)), -1, -1):
        if (v >> i) & 1:
            print("#", end="")
        else:
            print(".", end="")


def sum_pots(val, first_bit):
    length = int(math.log(val, 2))
    pot = length - first_bit
    acc = 0
    for i in range(length, -1, -1):
        #print("pot: {}".format(pot))
        pot += 1
        if (val >> i) & 1:
           acc += pot 
    return acc

def print_state():
    msg = "Generation {}, firstpot:{}, zeropos:{}, total:{} ".format(
        gen_count, 
        int(math.log(current_state, 2)) - first_bit, 
        first_bit,
        sum_pots(current_state, first_bit),
        )
    print("{:<60}".format(msg), end="")
    print(" " * (INDENT - first_bit), end="")
    print_binary(current_state)
    print("")


gen_count = 0
current_state = str_to_binary(initial_state_str)
first_bit = int(math.log(current_state, 2))
print_state()

for gen_count in range(1, 21):
    new_state = 0
    bit_count = int(math.log(current_state, 2)) + 1
    #import pdb; pdb.set_trace()
    for selected_bit in range(bit_count + 2, -5, -1):
        to_shift = selected_bit - 3
        if to_shift >= 0:
            t = (current_state >> to_shift) & (0b011111)
        else:
            t = (current_state << -to_shift) & (0b011111)

        for rule, result in rules:
            if t == rule:
                #import pdb; pdb.set_trace()
                if not new_state and result:
                    first_bit += (selected_bit - bit_count)
                new_state <<= 1
                new_state |= result
                break
        else:
            import pdb; pdb.set_trace()
            new_state <<= 1
    
    # right trim
    right_bits = 0
    while not new_state & (1<<right_bits):
        right_bits += 1
    first_bit += 5 - right_bits
    new_state = new_state >> right_bits
    
    current_state = new_state
    print_state()
    #print("Zero Position:{}  Total:{}".format(zero_position, sum_pots()))
