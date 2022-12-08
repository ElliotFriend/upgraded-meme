#!/usr/bin/env python3

import re, pprint

from collections import defaultdict

term_output = None
with open('input.txt', 'r') as f:
    term_output = f.read().splitlines()
# print(term_output)


def recursive_defaultdict():
    return defaultdict(recursive_defaultdict)

def set_path(d, p, k):
    # print(f"d: {d}")
    # print(f"p: {p}")
    # print(f"k: {k}")
    if len(p) == 1:
        d[p[0]] = k
    else:
        set_path(d[p[0]], p[1:], k)

tree = recursive_defaultdict()
set_path(tree, ['/'], {})
curr_path = ['/']

dir_sizes = {'/': 0}
def find_dir_sizes(d):
    total = 0
    for k, v in d.items():
        if isinstance(v, dict):
            dir_total = find_dir_sizes(v)
            # print(f"{k}: {dir_total}")
            total += find_dir_sizes(v)
            # dir_sizes[k] = total
        else:
            total += int(v)
    # print(sizes)
    # if len(sizes) == 1:
    #     return sizes.values()
    # else:
    #     return sizes
    return total
# def find_candidates(d):
#     dirs = {}
#     for k, v in d.items():
#         if isinstance(v, dict):
#             dirs[k] = 0
#             dirs[k] += find_candidates(v)
#         else:
#             return int(v)
#     return dirs

# def get_curr_dir(path):
#     return path.pop()
#
# def cd_up(path):
#     return path[:-1]

# print(cd_up("/a/b/c/d/e/f/"))
for i in range(0, len(term_output)):
    if i != 0:
        line_parts = term_output[i].split(' ')
        if line_parts[0] == '$':
            if line_parts[1] == 'cd':
                if line_parts[2] == '..':
                    curr_path = curr_path[:-1]
                else:
                    # print(line_parts)
                    curr_path.append(line_parts[2])
                    set_path(tree, curr_path, {})
        elif line_parts[0] != 'dir':
            curr_path.append(line_parts[1])
            # print(curr_path)
            set_path(tree, curr_path, line_parts[0])
            curr_path.pop()
    else:
        continue

# pprint.pprint(dict(tree))
# print(dict(tree).iteritems())
find_dir_sizes(tree)
# pprint.pprint(dir_sizes)

total_valid_size = 0
for i in dir_sizes.values():
    if i <= 100000:
        # print(i)
        total_valid_size += i
print(total_valid_size)

# print(curr_path)
# curr_dir = ""
# parent_path = "/"
# new_dir = ""
#
# for line in term_output:
#     if line.split(' ')[1] == "cd":
#         location = line.split(' ')[2]
#         if location != "/":
#             break
#         curr_dir = location
#     elif line.split(' ')[0] == 'dir':
#         new_dir = line.split(' ')[1]
#         tree[curr_dir][new_dir] = {}
#     else:
#         size, name = line.split(' ')
#         tree[curr_dir][new_dir]["size"] = size
#         tree[curr_dir][new_dir]["name"] = name

# def record_stuff(dir_name, parent_path, line):

# def cd_up(path):
#     # print(path)
#     path_parts = path.split('/')
#     path_parts.pop()
#     return '/'.join(path_parts)
#
# current_path = '/'
#
# for i in range(0, len(term_output)):
#     if i == 0:
#         continue
#     line_parts = term_output[i].split(' ')
#     # print(line_parts)
#     if line_parts[1] == 'cd':
#         if line_parts[2] == '..':
#             current_path = cd_up(current_path)
#             # current_path = cd_up(current_path)
#         else:
#             current_path += '/' + line_parts[2]
#             # print(current_path)
#             tree['/'][line_parts[2]] = {}
