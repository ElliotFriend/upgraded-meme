#!/usr/bin/env python3

import numpy as np
import pprint, math

motions = None
with open('input.txt', 'r') as f:
    motions = f.read().splitlines()
# print(motions)

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
    if h == t:
        # yes, they touch (overlap)
        return True
    elif math.dist(h, t) < 1.5:
        # yes, they touch (mathemagic!)
        return True
    else:
        return False

def t_follows_h(h, t, d):
    x_dist = math.dist([h[0]], [t[0]])
    y_dist = math.dist([h[1]], [t[1]])
    # print((x_dist, y_dist))
    new_t_coords = [0, 0]
    if x_dist > y_dist:
        new_t_coords[1] = h[1]
        match d:
            case 'R':
                new_t_coords[0] = h[0] - 1
            case 'L':
                new_t_coords[0] = h[0] + 1
    else:
        new_t_coords[0] = h[0]
        match d:
            case 'U':
                new_t_coords[1] = h[1] - 1
            case 'D':
                new_t_coords[1] = h[1] + 1
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
                x_coord_h += 1
            case 'L':
                x_coord_h -= 1
            case 'U':
                y_coord_h += 1
            case 'D':
                y_coord_h -= 1
        h_coords = (x_coord_h, y_coord_h)
        if h_coords not in unique_h_coords:
            unique_h_coords.append(h_coords)

        # now i need to calculate the space between tail and head
        curr_t_coords = (x_coord_t, y_coord_t)
        touching = t_touches_h(h_coords, curr_t_coords)
        # print(touching)
        # print_coords()
        if not touching:
            x_coord_t, y_coord_t = t_follows_h(h_coords, curr_t_coords, direction)
        t_coords = (x_coord_t, y_coord_t)
        if t_coords not in unique_t_coords:
            unique_t_coords.append(t_coords)
        # if t_coords not in unique_t_coords:
        #     unique_t_coords.append(t_coords)
        # print_coords()
pprint.pprint(unique_t_coords)
print(len(unique_t_coords))