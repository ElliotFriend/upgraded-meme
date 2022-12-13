#!/usr/bin/env python3

import ast, pprint
from itertools import zip_longest

contents = None
with open('input.txt', 'r') as f:
    contents = f.read()
packet_pairs = [[ast.literal_eval(l), ast.literal_eval(r)] for [l, r] in [p.split('\n') for p in contents.split('\n\n')]]
# print(packet_pairs)

all_packets = None
with open('input.txt', 'r') as f:
    all_packets = f.read().splitlines()
while '' in all_packets:
    all_packets.remove('')
all_packets = [ast.literal_eval(p) for p in all_packets]
# print(all_packets)
# probly def helper functions here

def compare_items(left, right):

    if isinstance(left, list) and isinstance(right, list):
        # both are lists, compare each item
        for l, r in zip_longest(left, right):
            # print(l, r)
            if l == None:
                return True
            elif r == None:
                return False


            if compare_items(l, r) == True:
                return True
            elif compare_items(l, r) == False:
                return False

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False

    if (
        (isinstance(left, list) and isinstance(right, int))
        or
        (isinstance(left, int) and isinstance(right, list))
    ):
        left = left if isinstance(left, list) else [left]
        right = right if isinstance(right, list) else [right]
        if compare_items(left, right) == True:
            return True
        elif compare_items(left, right) == False:
            return False

def part_one(input):
    correctly_ordered = []
    for i in range(1, len(input) + 1):
        if compare_items(input[i - 1][0], input[i - 1][1]):
            correctly_ordered.append(i)
    return sum(correctly_ordered)

def part_two(input):
    ordered_packets = [[[2]], [[6]]]
    # input.append([[2]]).append([[6]])
    for packet in input:
        # if i == 0:
        #     ordered_packets.append(input[i])
        # else:
        for i in range(len(ordered_packets)):
            op = ordered_packets[i]
            v = compare_items(packet, op)
            if v == True:
                ordered_packets.insert(i, packet)
                break
            else:
                pass
        if packet not in ordered_packets:
            ordered_packets.append(packet)
    # pprint.pprint(ordered_packets)
    index2 = ordered_packets.index([[2]]) + 1
    index6 = ordered_packets.index([[6]]) + 1
    return index2 * index6

if __name__ == '__main__':
    print(f"Part 01: {part_one(packet_pairs)}")
    print(f"Part 02: {part_two(all_packets)}")
