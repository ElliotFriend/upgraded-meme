#!/usr/bin/env python3

import re, pprint

from math import sqrt

sensors = []
beacons = []
distances = []
blocked = set()
min_x, min_y, max_x, max_y, max_d = 0, 0, 0, 0, 0

contents = None
with open('input.txt', 'r') as f:
    contents = f.read().splitlines()
# print(contents)

def manhattan(sensor, beacon):
    return sum([abs(sensor[0] - beacon[0]), abs(sensor[1] - beacon[1])])

for line in contents:
    # do something here
    match = re.search(r'x=(-?\d+), y=(-?\d+):.*x=(-?\d+), y=(-?\d+)$', line)
    sensor = (int(match.group(1)), int(match.group(2)))
    beacon = (int(match.group(3)), int(match.group(4)))
    distance = manhattan(sensor, beacon)
    # distance = manhattan(sensor, beacon)
    # l_min_x = min(sensor[0], beacon[0])
    # l_max_x = max(sensor[0], beacon[0])
    # l_min_y = min(sensor[1], beacon[1])
    # l_max_y = max(sensor[1], beacon[1])

    if sensor[0] < min_x:
        min_x = sensor[0]
    elif sensor[0] > max_x:
        max_x = sensor[0]

    if sensor[1] < min_y:
        min_y = sensor[1]
    elif sensor[1] > max_y:
        max_y = sensor[1]

    if distance > max_d:
        max_d = distance

    sensors.append(sensor)
    beacons.append(beacon)
    distances.append(distance)
    # print(match.group(4))
# print(sensors, beacons)
print((min_x, min_y), (max_x, max_y), max_d)

# print(manhattan(sensors[6], beacons[6]))

# grid = {}
# # grid = []
# for y in range(min_y, max_y):
#     # grid.append([])
#     # grid[y] = []
#     for x in range(min_x, max_x):
#         print(f"examining position: {(x, y)}")
#         for s in range(len(sensors)):
#             if manhattan((x, y), sensors[s]) <= distances[s]:
#                 blocked.add((x, y))
#         if (x, y) in beacons:
#             grid[y].append('B')
#         elif (x, y) in sensors:
#             grid[y].append('S')
#         elif (x, y) in blocked:
#             grid[y].append('#')
#         else:
#             grid[y].append('.')

# for b in beacons:
#     blocked.discard(b)
# for s in sensors:
#     blocked.discard(s)

# pprint.pprint(grid)

def part_one(y):
    blocked = set()
    print((min_x - max_d, max_x + max_d))
    for x in range(min_x - max_d, max_x + max_d):
        # print((x, y))
        for s in range(len(sensors)):
            if manhattan((x, y), sensors[s]) <= distances[s]:
                blocked.add((x, y))

    for b in beacons:
        blocked.discard(b)
    for s in sensors:
        blocked.discard(s)

    return len(blocked)
    # return grid[row].count('#')
    # count = 0
    # for c in blocked:
    #     if c[1] == row:
    #         count += 1
    # return count
# for pair in zip(sensors, beacons)
# distance = manhattan(sensors[6], beacons[6])
# for i in range(distance + 1):
#     sensor_coord = sensors[6]

# for row in grid:
#     print(''.join(grid[row]))

# N=int(5e7)
# O=int(1e6)
# res = [0 for i in range(min_x, max_x)]
# print(len(res))
# print(f"Example: {part_one(10)}")
print(f"Part 01: {part_one(2000000)}")
print(f"Part 02: {None}")
