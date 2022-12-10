#!/usr/bin/env python3

contents = None
with open('input.txt', 'r') as f:
    contents = f.read().splitlines()
# print(contents)

x_reg = 1
cycle_count = 0
ss_sum = 0
crt_rows = [[], [], [], [], [], []]

def clock_cycle(value = 0):
    global ss_sum
    global crt_rows
    global x_reg
    global cycle_count

    row = cycle_count // 40
    col = cycle_count % 40

    if col in range(x_reg - 1, x_reg + 2):
        crt_rows[row].append('#')
    else:
        crt_rows[row].append('.')

    cycle_count += 1
    x_reg += value
    # because i'm 0-indexing (not 1) `cycle_count`, i have to add 1 here
    if cycle_count + 1 in [20, 60, 100, 140, 180, 220]:
        ss_sum += (cycle_count + 1) * x_reg

for line in contents:
    if line == 'noop':
        clock_cycle()
    else:
        clock_cycle()
        clock_cycle(int(line.split()[1]))

print(f"Part 01: {ss_sum}\n")

print("Part 02:")
for row in crt_rows:
    print(''.join(row))