#!/usr/bin/env python3

contents = None
with open('input.txt', 'r') as f:
    contents = f.read().split('\n\n')

class Elf:
    max_cal = 0
    top_three = []
    def __init__(self, id, items):
        self.id = id
        self.items = items

        self.total_cal = sum(items)
        if self.total_cal > Elf.max_cal:
            Elf.max_cal = self.total_cal

        Elf.top_three.append(self.total_cal)
        Elf.top_three.sort(reverse=True)
        Elf.top_three = Elf.top_three[:3]

    def __repr__(self):
        return f"Elf{self.id}:\tTotal Calories: {self.total_cal}\tItems: {self.items}"

    def empty_snacks(self):
        self.snacks = []
        self.total_cal = sum(self.snacks)

elves = {}

for n in range(len(contents)):
    list = [int(i) for i in contents[n].rstrip().split('\n')]
    elf = Elf(n, list)
    elves[n] = elf

if __name__ == '__main__':
    print(f"Part 01: {Elf.max_cal}")
    print(f"Part 02: {sum(Elf.top_three)}")
