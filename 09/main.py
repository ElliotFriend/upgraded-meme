#!/usr/bin/env python3

import math

motions = None
with open('input.txt', 'r') as f:
    motions = f.read().splitlines()

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

def t_touches_h(h, t):
    if h == t:
        # yes, they touch (overlap)
        return True
    elif math.dist(h, t) < 1.5:
        # yes, they touch (mathemagic!)
        return True
    else:
        return False

def t_follows_h(h, t):
    x_dist = h[0] - t[0]
    y_dist = h[1] - t[1]
    new_t_coords = [t[0], t[1]]
    new_t_coords[0] += min(max(x_dist, -1), 1)
    new_t_coords[1] += min(max(y_dist, -1), 1)
    return tuple(new_t_coords)


for line in motions:
    line_parts = line.split()
    direction = line_parts[0]
    spaces = int(line_parts[1])
    for i in range(0, spaces):
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
        unique_coords[0].add(h_coords)

        # now i need to calculate the space between tail and head
        for knot in range(1, 10):
            head = knot - 1
            touching = t_touches_h(curr_coords[head], curr_coords[knot])
            if not touching:
                curr_coords[knot][0], curr_coords[knot][1] = t_follows_h(
                    curr_coords[head], curr_coords[knot]
                )
            knot_coords = (curr_coords[knot][0], curr_coords[knot][1])
            unique_coords[knot].add(knot_coords)

print(len(unique_coords[9]))