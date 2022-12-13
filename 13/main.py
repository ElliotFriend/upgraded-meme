#!/usr/bin/env python3

import ast
from itertools import zip_longest

contents = None
with open('input.txt', 'r') as f:
    contents = f.read()
# print(contents)

packet_pairs = [[ast.literal_eval(l), ast.literal_eval(r)] for [l, r] in [p.split('\n') for p in contents.split('\n\n')]]
# print(packet_pairs)
# probly def helper functions here

def compare_items(left, right):

    if isinstance(left, list) and isinstance(right, list):
        # both are lists, compare each item
        for l, r in zip_longest(left, right):
            print(l, r)
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
        if compare_items(input[i-1][0], input[i-1][1]):
            correctly_ordered.append(i)
    return sum(correctly_ordered)

def part_two(input):
    # return input
    pass

if __name__ == '__main__':
    print(f"Part 01: {part_one(packet_pairs)}")
    print(f"Part 02: {part_two(packet_pairs)}")
