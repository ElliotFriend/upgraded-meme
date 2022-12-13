#!/usr/bin/env python3

import ast
from itertools import zip_longest

contents = None
with open('input.txt', 'r') as f:
    contents = f.read()
# print(contents)

packet_pairs = [p.split('\n') for p in contents.split('\n\n')]
# print(packet_pairs)
# probly def helper functions here


def left_lt_right(l, r):
    return l < r

def shorter_list(l, r):
    return l if l < r else r

def longer_list(l, r):
    return l if l > r else r

for line in contents:
    # do something here
    pass

def compare_packet_ints(left, right):
    # print(left, right)
    if left == None:
        return True
    elif right == None:
        return False

    if left == right:
        pass
    elif left < right:
        return True
    else:
        return False

def compare_packet_lists(left, right):
    # shorter = shorter_list(left, right)
    # longer = longer_list(left, right)
    for l, r in zip_longest(left, right, fillvalue=None):
        # print(l, r)
        verdict = compare_packet_ints(l, r)
        if verdict == None:
            pass
        elif verdict == True:
            print(l, r)
            print("we got true!")
            return True
        elif verdict == False:
            print(l, r)
            print('we got false...')
            return False


# def compare_packet_mixed(left, right):
#     pass

def part_one(input):
    packet_index = 1
    correctly_ordered = []
    for [left, right] in input:
        # print(left)
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        verdict = None

        # if isinstance(left, int) and isinstance(right, int):
        #     print(compare_packet_ints(left, right))
        print(left, right)
        while verdict == None:
            for (l, r) in zip_longest(left, right, fillvalue=None):
                print(l, r)
                if l == None:
                    print("none makes it true")
                    correctly_ordered.append(packet_index)
                    verdict = True
                    break
                if r == None:
                    print("none makes it false")
                    verdict = False
                    break

                if isinstance(l, list) and isinstance(r, list):
                    v0 = compare_packet_lists(l, r)
                    if v0 == True:
                        correctly_ordered.append(packet_index)
                        verdict = True
                        # break
                    elif v0 == False:
                        verdict = False
                elif isinstance(l, int) and isinstance(r, int):
                    v1 = compare_packet_ints(l, r)
                    if v1 == True:
                        correctly_ordered.append(packet_index)
                        verdict = True
                        # break
                    elif v1 == False:
                        verdict = False
                else:
                    l = l if isinstance(l, list) else [l]
                    r = r if isinstance(r, list) else [r]
                    v2 = compare_packet_lists(l, r)
                    if v2 == True:
                        correctly_ordered.append(packet_index)
                        verdict = True
                    elif v2 == False:
                        verdict = False
        packet_index += 1

    # print(packet_index)
        # print(compare_packet_ints(left, right))
        # for i in range(len(shorter)):
        #     print(compare_packet_data(shorter[i], longer[i]))

        # if isinstance(left, list) and isinstance(right, list):
        #     print('both lists')
    print(correctly_ordered)
    return sum(correctly_ordered)

def part_two(input):
    pass


if __name__ == '__main__':
    print(f"Part 01: {part_one(packet_pairs)}")
    print(f"Part 02: {part_two(packet_pairs)}")
