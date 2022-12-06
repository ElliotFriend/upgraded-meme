#!/usr/bin/env python3

elf_pairs = None
with open('input.txt', 'r') as f:
    elf_pairs = f.read().splitlines()

fully_contained = 0

def expand(s):
    l = []
    j = s.split('-')
    for k in range(int(j[0]), int(j[1])+1):
        l.append(k)
    return l

nested_elves = 0

for pair in elf_pairs:
    elf1, elf2 = pair.split(',')
    elf1 = expand(elf1)
    elf2 = expand(elf2)
    if set(elf1).issubset(elf2) or set(elf2).issubset(elf1):
        nested_elves += 1

print(nested_elves)