#!/usr/bin/env python3

import re

input = None
drawing = []
procedure = None
n = 4

with open('input.txt', 'r') as f:
    with open('drawing.txt', 'w') as df:
        with open('procedure.txt', 'w') as pf:
            input = f.read().splitlines()
            for line in input:
                if line != '':
                    if line.startswith('move'):
                        pf.write(f"{line}\n")
                    else:
                        df.writelines(f"{line}\n")

with open('drawing.txt', 'r') as f:
    lines = f.read().splitlines()
    for row in lines:
        chunks = [row[i:i+n] for i in range(0, len(row), n)]
        drawing.append(chunks)

with open('procedure.txt', 'r') as f:
    procedure = f.read().splitlines()

stacks = {}
for i in range(1, len(drawing[-1])+1):
    stacks[i] = []

for row in drawing[:-1]:
    for i in range(1, len(row)+1):
        crate = re.sub(r'[\W]', '', row[i-1])
        if crate != '':
            stacks[i].insert(0, crate)

print("STARTING STACKS")
for col in stacks:
    print(f"{col}: {stacks[col]}")

steps = []

def calc_move(step):
    _, amount, _, col_from, _, col_to = step.split(' ')
    return [amount, col_from, col_to]

for move in procedure:
    steps.append(calc_move(move))
# print(steps)

for step in steps:
    # print(step)
    amount, col_from, col_to = int(step[0]), int(step[1]), int(step[2])
    move_crates = stacks[col_from][len(stacks[col_from])-amount:]
    stacks[col_from] = stacks[col_from][:len(stacks[col_from])-amount]
    stacks[col_to].extend(move_crates)
    # for i in range(0, amount):
    #     crate = stacks[col_from].pop()
    #     stacks[col_to].append(crate)

print("ENDING STACKS")
message = []
for col in stacks:
    print(f"{col}: {stacks[col]}")
    message.append(stacks[col][-1])

print(''.join(message))


#
# n = 4
# # str = drawing[-1]
# # chunks = [str[i:i+n] for i in range(0, len(str), n)]
# # print(chunks)
# # print(drawing[-1][:len(drawing[-1]) // 4])
# for row in drawing:
#     chunks = [row[i:i+n] for i in range(0, len(row), n)]
#     print(chunks)

# for i in

# print("PROCEDURE BELOW:")
# print(procedure)
# print("DRAWING BELOW:")
# print(drawing)