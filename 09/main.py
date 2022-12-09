#!/usr/bin/env python3

import numpy as np
import pprint, math

motions = None
with open('input.txt', 'r') as f:
    motions = f.read().splitlines()
# print(motions)

unique_coords = {
    0: set(),
    1: set(),
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set(),
    7: set(),
    8: set(),
    9: set()
}

curr_coords = {
    0: [0, 0],
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0],
    7: [0, 0],
    8: [0, 0],
    9: [0, 0],
}

x_coord_h = 0
y_coord_h = 0
unique_h_coords = [(0, 0)]

x_coord_t = 0
y_coord_t = 0
# all_t_coords = [(0, 0)]
unique_t_coords = [(0, 0)]

def print_coords():
    print(f"head: ({x_coord_h}, {y_coord_h})")
    print(f"tail: ({x_coord_t}, {y_coord_t})\n")

def t_touches_h(h, t):
    x_dist = math.dist([h[0]], [t[0]])
    y_dist = math.dist([h[1]], [t[1]])
    if h == t:
        # yes, they touch (overlap)
        return True
    elif math.dist(h, t) < 1.5:
    # elif x_dist <= 1 and y_dist <= 1:
        # print(math.dist(h, t))
        # yes, they touch (mathemagic!)
        return True
    else:
        return False

def t_follows_h(h, t):
    x_dist = h[0] - t[0]
    y_dist = h[1] - t[1]
    # print((x_dist, y_dist))
    new_t_coords = [t[0], t[1]]
    new_t_coords[0] += min(max(x_dist, -1), 1)
    new_t_coords[1] += min(max(y_dist, -1), 1)
    # if x_dist > y_dist:
    #     new_t_coords[1] = h[1]
    #     new_t_coords[0] = int((h[0] + t[0]) / 2)
    # else:
    #     new_t_coords[0] = h[0]
    #     new_t_coords[1] = int((h[1] + t[1]) / 2)
    # print(new_t_coords)
    return tuple(new_t_coords)


for line in motions:
    line_parts = line.split()
    direction = line_parts[0]
    spaces = int(line_parts[1])
    # print(line_parts)
    for i in range(0, spaces):
        # print(i)
        match direction:
            case 'R':
                curr_coords[0][0] += 1
            case 'L':
                curr_coords[0][0] -= 1
            case 'U':
                curr_coords[0][1] += 1
            case 'D':
                curr_coords[0][1] -= 1
        h_coords = (curr_coords[0][0], curr_coords[0][1])
        # print(h_coords)
        unique_coords[0].add(h_coords)
        # if h_coords not in unique_h_coords:
        #     unique_h_coords.append(h_coords)

        # now i need to calculate the space between tail and head
        for knot in range(1, 10):
            head = knot - 1
            # curr_knot_coords = curr_coords[knot]
            touching = t_touches_h(curr_coords[head], curr_coords[knot])
            if not touching:
                curr_coords[knot][0], curr_coords[knot][1] = t_follows_h(
                    curr_coords[head], curr_coords[knot]
                )
                # if knot == 9:
                #     print((curr_coords[knot][0], curr_coords[knot][1]))
            knot_coords = (curr_coords[knot][0], curr_coords[knot][1])
            # print(f"Space: {i}: Knot {knot}: ({knot_coords})")
            unique_coords[knot].add(knot_coords)
            # if knot == 9:
            #     print(knot_coords)
        # curr_t_coords = (x_coord_t, y_coord_t)
        # touching = t_touches_h(h_coords, curr_t_coords)
        # # print(touching)
        # # print_coords()
        # if not touching:
        #     x_coord_t, y_coord_t = t_follows_h(h_coords, curr_t_coords, direction)
        # t_coords = (x_coord_t, y_coord_t)
        # if t_coords not in unique_t_coords:
        #     unique_t_coords.append(t_coords)
        # if t_coords not in unique_t_coords:
        #     unique_t_coords.append(t_coords)
        # print_coords()
# pprint.pprint(unique_coords[9])
# print(unique_coords[9])
print(len(unique_coords[9]))