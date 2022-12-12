#!/usr/bin/env python3
import string, pprint
import numpy as np
from collections import deque

alphabet = string.ascii_lowercase
fewest_steps_options = []
starting_points = []
map_array = []

contents = None
with open('input.txt', 'r') as f:
    contents = [line.rstrip() for line in f.readlines()]
# print(contents)

for line in contents:
    map_array.append([*line])
np_array = np.array(map_array)
a_spots = np.where((np_array == 'a') | (np_array == 'S'))
for i in range(0, len(a_spots[0])):
    starting_points.append((a_spots[0][i], a_spots[1][i]))


class MapSpot():
    def __init__(self, letter, row, col):
        self.letter = letter
        self.row = row
        self.col = col

        self.pre_letter = None
        self.distance = None
        self.neighbors = []

    def __repr__(self):
        return f"MapSpot({self.letter})\tLocation: ({self.row}, {self.col})\tNeighbors({len(self.neighbors)})"

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def reset(self):
        self.pre_letter = None
        self.distance = None

for point in starting_points:
    spots = {}

    for row in range(0, len(contents)):
        line = contents[row]
        # map_array.append([*line])
        for col in range(0, len(line)):
            letter = line[col]
            if letter == 'S' or letter == 'a':
                spots[(row, col)] = MapSpot('a', row, col)
            elif letter == 'E':
                end = MapSpot('z', row, col)
                spots[(row, col)] = end
            else:
                spots[(row, col)] = MapSpot(letter, row, col)
    # print(map_array)
    # pprint.pprint(spots)

    def compare_letters(a, b):
        return alphabet.find(b) <= alphabet.find(a) + 1

    for (row, col) in spots:
        spot = spots[(row, col)]

        directions = [
            (row + 1, col),
            (row - 1, col),
            (row, col - 1),
            (row, col + 1)
        ]

        for d in directions:
            if (
                d in spots
                and compare_letters(spot.letter, spots[d].letter)
            ):
                spot.add_neighbor(spots[d])


    trail = []
    spot = spots[point]
    # print(spot)
    spot.distance = 0
    trail.append(spots[point])

    while len(trail) > 0:
        spot = trail.pop(0)
        for neighbor in spot.neighbors:
            if neighbor.distance == None: # means we haven't visited this neighbor yet
                neighbor.distance = spot.distance + 1
                neighbor.pre_letter = spot
                trail.append(neighbor)

    # pprint.pprint(spots)
    fewest_steps_options.append(end.distance)

print(min([i for i in fewest_steps_options if i is not None]))