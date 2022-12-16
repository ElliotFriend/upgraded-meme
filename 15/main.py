#!/usr/bin/env python3

import re
from collections import defaultdict

sensors = []
beacons = []
distances = []
blocked = set()
min_x, min_y, max_x, max_y, max_d = 0, 0, 0, 0, 0

contents = None
with open('input.txt', 'r') as f:
    contents = f.read().splitlines()

def manhattan(sensor, beacon):
    return sum([abs(sensor[0] - beacon[0]), abs(sensor[1] - beacon[1])])

def tuning_freq(x, y):
    return x * 4000000 + y

for line in contents:
    match = re.search(r'x=(-?\d+), y=(-?\d+):.*x=(-?\d+), y=(-?\d+)$', line)
    sensor = (int(match.group(1)), int(match.group(2)))
    beacon = (int(match.group(3)), int(match.group(4)))
    distance = manhattan(sensor, beacon)

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

def part_one(y):
    blocked = set()
    for x in range(min_x - max_d, max_x + max_d):
        for s in range(len(sensors)):
            if manhattan((x, y), sensors[s]) <= distances[s]:
                blocked.add((x, y))

    for b in beacons:
        blocked.discard(b)
    for s in sensors:
        blocked.discard(s)

    return len(blocked)

def part_two(low, high):
    x = y = low
    while y < high:
        possibles = defaultdict(int)
        for s in range(len(sensors)):
            distance = distances[s]
            up = distance - manhattan(sensors[s], (sensors[s][0], y))
            if up < low:
                continue
            left = max(low, sensors[s][0] - up)
            right = min(high, sensors[s][0] + up)
            possibles[left] += 1
            possibles[right+1] -= 1
            curr = 0
        for x_pos in sorted(possibles.keys()):
            curr += possibles[x_pos]
            if curr == 0 and x_pos != high + 1:
                return tuning_freq(x_pos, y)
        y += 1

# print(f"Example 01: {part_one(10)}")
print(f"Part 01: {part_one(2000000)}")
# print(f"Example 02: {part_two(0, 20)}")
print(f"Part 02: {part_two(0, 4000000)}")
