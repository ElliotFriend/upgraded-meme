#!/usr/bin/env python3
import pprint

tree_map = None
with open('input.txt', 'r') as f:
    tree_map = f.read().splitlines()
# print(tree_map)

tree_lists = []
visible_perimiter_trees = 0
visible_interior_trees = 0

for row in tree_map:
    # print(row.split())
    tree_lists.append([int(x) for x in str(row)])
# pprint.pprint(tree_lists)

visible_perimiter_trees += len(tree_lists) * 2
visible_perimiter_trees += (len(tree_lists) - 2) * 2
# print(visible_perimiter_trees)

def visible_left(tree, x, y):
    for i in range(0, x):
        if tree_lists[y][i] >= tree:
            return False
    return True
# print(visible_left(5, 2, 1))

def visible_right(tree, x, y):
    for i in range(x+1, len(tree_lists[y])):
        if tree_lists[y][i] >= tree:
            return False
    return True
# print(visible_right(5, 2, 1))

def visible_top(tree, x, y):
    for i in range(0, y):
        if tree_lists[i][x] >= tree:
            return False
    return True
# print(visible_top(5, 2, 1))

def visible_bottom(tree, x, y):
    for i in range(y+1, len(tree_lists)):
        if tree_lists[i][x] >= tree:
            return False
    return True
# print(visible_bottom(3, 2, 2))

for y in range(1, len(tree_lists) - 1):
    for x in range(1, len(tree_lists[y]) - 1):
        tree = tree_lists[y][x]
        if (visible_left(tree, x, y)
            or visible_top(tree, x, y)
            or visible_right(tree, x, y)
            or visible_bottom(tree, x, y)
        ):
            visible_interior_trees += 1

print(f"Visible Perimeter Trees: {visible_perimiter_trees}\n")
print(f"Visible Interior Trees: {visible_interior_trees}\n")
print(f"Total Visible Trees: {visible_perimiter_trees + visible_interior_trees}")
# def find_left_right_visible(tree_row):
#     for i in range(1, len(tree_row) - 1):
#         shorter_trees = 0
#         for left_tree in tree_row[0:i-1]:
#             if left_tree <= tree_row[i]:
#                 shorter_trees += 1
#         # for right_tree in tree_row[i+1:-1]:
#             # if right_tree
#         # print(tree_row[i])

# find_left_right_visible(tree_lists[1])