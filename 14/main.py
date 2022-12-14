#!/usr/bin/env python3

import pprint
import numpy as np

contents = None
with open('input.txt', 'r') as f:
    contents = f.read().splitlines()
# print(contents)

sand_origin = (500, 0)
all_sand = set()
abyss_reached = False

# maybe a class?
class Line:
    lowest_x = 500
    highest_x = 500
    highest_y = 0
    rock_points = set()

    def __init__(self, start, end):
        self.start = start
        # Line.all_points.add(start)
        self.end = end
        # Line.all_points.add(end)
        self.orientation = "vert" if start[0] == end[0] else "hori"

        self.points = set()
        if self.orientation == "vert":
            top = min(start, end)
            bottom = max(start, end)
            for y in range(top[1], bottom[1] + 1):
                self.points.add((top[0], y))
        elif self.orientation == "hori":
            left = min(start, end)
            right = max(start, end)
            for x in range(left[0], right[0] + 1):
                self.points.add((x, left[1]))
        Line.rock_points.update(self.points)

        if max(start[1], end[1]) > Line.highest_y:
            Line.highest_y = max(start[1], end[1])
        if min(start[0], end[0]) < Line.lowest_x:
            Line.lowest_x = min(start[0], end[0])
        if max(start[0], end[0]) > Line.highest_x:
            Line.highest_x = max(start[0], end[0])

    def __repr__(self):
        return f"{self.orientation}. line from ({self.start}) to ({self.end})"

class Path:
    def __init__(self, points):
        self.lines = {}
        for i in range(len(points) - 1):
            line = Line(points[i], points[i + 1])
            self.lines[i] = line

    def __repr__(self):
        return f"Path:\t{self.lines}"

    def method(self, other_thing):
        return other_thing * 2

# probly def functions here

paths = {}

for i in range(len(contents)):
    # do something here
    # pass
    points = [(int(x), int(y)) for [x, y] in [p.split(',') for p in contents[i].split(' -> ')]]
    paths[i] = Path(points)

# print(Line.all_points)
# pprint.pprint(paths)
print(Line.lowest_x, Line.highest_x, Line.highest_y)

def get_next_sand_pos(sand_pos):
    global abyss_reached
    (x, y) = sand_pos
    down_pos = (x, y + 1)
    if down_pos[1] > Line.highest_y:
        abyss_reached = True
        return False
    down_left_pos = (x - 1, y + 1)
    down_right_pos = (x + 1, y + 1)
    if down_pos not in all_sand and down_pos not in Line.rock_points:
        return down_pos
    elif down_left_pos not in all_sand and down_left_pos not in Line.rock_points:
        return down_left_pos
    elif down_right_pos not in all_sand and down_right_pos not in Line.rock_points:
        return down_right_pos
    else:
        return (x, y)


def drop_sand(sand_pos):
    global all_sand
    # sand_origin = (500, 0)
    (x, y) = sand_pos
    abyss_threshold = Line.highest_y + 2
    # for i in range(y, Line.highest_y):
    next_pos = get_next_sand_pos(sand_pos)
    # print(sand_pos, next_pos)
    if next_pos == False:
        return False
    elif next_pos == sand_pos:
        all_sand.add(sand_pos)
        # break
    else:
        drop_sand(next_pos)
        # if next_pos in all_sand or next_pos in Line.rock_points:
        #     all_sand.add(sand_pos)
        #     break
        # else:
        #     pass

# sand_landed = True
while not abyss_reached:
    sand_landed = drop_sand(sand_origin)
    # if sand_landed == False:
    #     abyss_reached = True
    #     break

grid = []
for y in range(0, Line.highest_y + 2):
    grid.append([])
    for x in range(Line.lowest_x - 1, Line.highest_x + 2):
        if (x, y) in Line.rock_points:
            grid[y].append('#')
        elif x == 500 and y == 0:
            grid[y].append('+')
        elif (x, y) in all_sand:
            grid[y].append('o')
        else:
            grid[y].append('.')
    # grid[y].append('.')



for g in grid:
    print(''.join(g))

if __name__ == '__main__':
    print(f"Part 01: {len(all_sand)}")
    print(f"Part 02: {None}")
