#!/usr/bin/env python3

import pprint, math

contents = None
with open('input.txt', 'r') as f:
    contents = f.read().splitlines()
# print(contents)

x_reg = 0
cycle_count = 0
ss_sum = 0
# sprite_position = 0
crt_rows = [[], [], [], [], [], [], []]

def check_cycle_count(value = 0):
    global ss_sum
    global crt_rows
    global x_reg
    global cycle_count

    row = cycle_count // 40
    col = cycle_count % 40
    # if (row == 0):
    #     print(f"row: {row}\t\tcol: {col}\t\tx_reg: {x_reg}\tmath: {cycle_count % 40}")
    cycle_count += 1

    if col in range(x_reg, x_reg + 3):
        # print(f"cycle: {cycle_count}\tmath: {math.ceil(cycle_count // 40)}")
        crt_rows[row].append('#')
    else:
        crt_rows[row].append('.')

    x_reg += value
    if cycle_count + 1 in [20, 60, 100, 140, 180, 220]:
        ss_sum += (cycle_count + 1) * (x_reg + 1)

for line in contents:
    if line == 'noop':
        # cycle_count += 1
        check_cycle_count()
    else:
        value = int(line.split()[1])
        # cycle_count += 1
        check_cycle_count()
        # cycle_count += 1
        check_cycle_count(value)
        # x_reg += value


# print(x_reg)
# print(cycle_count)
print(ss_sum)
# crt_rows.pop()
for row in crt_rows:
    print(''.join(row))