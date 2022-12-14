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
hole_plugged = False

# maybe a class?
class Line:
    lowest_x = 500
    highest_x = 500
    highest_y = 0
    floor = 0
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
            Line.floor = Line.highest_y + 2
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

# floor_points = [(0, Line.highest_y + 2), (1000, Line.highest_y + 2)]
# paths['floor'] = Path(floor_points)

# print(Line.all_points)
# pprint.pprint(paths)
# print(Line.lowest_x, Line.highest_x, Line.highest_y, Line.floor)
# print(Line.rock_points)

def get_next_sand_pos(x, y, part):
    global abyss_reached
    # global hole_plugged
    # sand_pos (x, y) = sand_pos
    down_pos = (x, y + 1)
    if y + 1 > Line.highest_y and part == 1:
        abyss_reached = True
        return False
    down_left_pos = (x - 1, y + 1)
    down_right_pos = (x + 1, y + 1)
    all_blocks = [*all_sand, *Line.rock_points]
    if y + 1 < Line.floor:
        if down_pos not in all_blocks:
            return down_pos
        elif down_left_pos not in all_blocks:
            return down_left_pos
        elif down_right_pos not in all_blocks:
            return down_right_pos
        else:
            return (x, y)
    else:
        return (x, y)
    # else:
    #     hole_plugged = True
    #     return (x, y)


def drop_sand(x, y, part):
    global all_sand
    global hole_plugged
    # sand_origin = (500, 0)
    # (x, y) = sand_pos
    # abyss_threshold = Line.highest_y + 2
    # for i in range(y, Line.highest_y):
    next_pos = get_next_sand_pos(x, y, part)
    # print(sand_pos, next_pos)
    if next_pos == False:
        return False
    # elif next_pos :
    #     hole_plugged = True
    elif next_pos == (x, y):
        if y == 1:
            hole_plugged = True
        all_sand.add((x, y))
        # break
    else:
        drop_sand(next_pos[0], next_pos[1], part)
        # if next_pos in all_sand or next_pos in Line.rock_points:
        #     all_sand.add(sand_pos)
        #     break
        # else:
        #     pass

# sand_landed = True
def part_one():
    while not abyss_reached:
        drop_sand(500, 0, 1)
    # if sand_landed == False:
    #     abyss_reached = True
    #     break

    # grid = []
    # for y in range(0, Line.highest_y + 2):
    #     grid.append([])
    #     for x in range(Line.lowest_x - 1, Line.highest_x + 2):
    #         if (x, y) in Line.rock_points:
    #             grid[y].append('#')
    #         elif x == 500 and y == 0:
    #             grid[y].append('+')
    #         elif (x, y) in all_sand:
    #             grid[y].append('o')
    #         else:
    #             grid[y].append('.')
    # # grid[y].append('.')
    # for g in grid:
    #     print(''.join(g))


def part_two():
    # while not hole_plugged:
    for i in range(28000):
        drop_sand(500, 0, 2)
    # if sand_landed == False:
    #     abyss_reached = True
    #     break

    # grid = []
    # for y in range(0, Line.floor + 1):
    #     grid.append([])
    #     for x in range(Line.lowest_x - 100, Line.highest_x + 100):
    #         if (x, y) in Line.rock_points or y == Line.floor:
    #             grid[y].append('#')
    #         elif x == 500 and y == 0:
    #             grid[y].append('+')
    #         elif (x, y) in all_sand:
    #             grid[y].append('o')
    #         else:
    #             grid[y].append('.')
    # # grid[y].append('.')
    # for g in grid:
    #     print(''.join(g))

if __name__ == '__main__':
    # part_one()
    # print(f"Part 01: {len(all_sand)}")

    part_two()
    print(f"Part 02: {len(all_sand)}")
