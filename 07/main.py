#!/usr/bin/env python3

import collections, pprint

term_output = None
with open('input.txt', 'r') as f:
    term_output = f.read().splitlines()
# print(term_output)

all_dirs = collections.defaultdict(int)
curr_dirs = []

for line in term_output:
    line_parts = line.split(' ')
    # print(line_parts)
    if line_parts[0] == '$':
        # it's a command, what will we do
        if line_parts[1] == 'ls':
            # we can ignore the 'ls' lines
            pass

        elif line_parts[1] == 'cd':
            # where will we change to?

            if line_parts[2] == '/':
                curr_dirs = []

            elif line_parts[2] == '..':
                # move up a directory "somehow"
                curr_dirs.pop()

            else:
                # we're cd-ing forward into a directory, let's add it to the path
                curr_dirs.append(line_parts[2])

    elif line_parts[0] == 'dir':
        # we can also ignore any 'dir' output, since there's no size to count
        pass

    else:
        # print(line_parts)
        # print(curr_dirs)
        # we have reached files and sizes... let's add /shrug
        file_size = int(line_parts[0])

        # add that to root
        all_dirs['/'] += file_size

        # add that to every all_dirs entry in the current filepath
        for i in range(0, len(curr_dirs)):
            curr_dirs_str = '/'.join(curr_dirs[:i+1])
            # print(curr_dirs_str)
            all_dirs[curr_dirs_str] += file_size

# pprint.pprint(all_dirs)

total_sums = 0
max_space = 70000000
curr_free = max_space - all_dirs['/']
needed_free = 30000000
need_to_del = needed_free - curr_free
candidates = []

for dir, size in all_dirs.items():
    if size <= 100000:
        total_sums += size
    if size > need_to_del:
        candidates.append(size)

print(total_sums)
print(min(candidates))