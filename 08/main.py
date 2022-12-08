#!/usr/bin/env python3

tree_map = None
with open('input.txt', 'r') as f:
    tree_map = f.read().splitlines()

tree_lists = []
visible_perimiter_trees = 0
visible_interior_trees = 0
max_scenic_score = 0

for row in tree_map:
    tree_lists.append([int(x) for x in str(row)])

visible_perimiter_trees += len(tree_lists) * 2
visible_perimiter_trees += (len(tree_lists) - 2) * 2

def visible_left(tree, x, y):
    for i in range(0, x):
        if tree_lists[y][i] >= tree:
            return False
    return True

def find_left_trees(tree, x, y):
    trees = []
    for i in reversed(range(0, x)):
        trees.append(tree_lists[y][i])
        if tree_lists[y][i] >= tree:
            return trees
    return trees

def visible_right(tree, x, y):
    for i in range(x+1, len(tree_lists[y])):
        if tree_lists[y][i] >= tree:
            return False
    return True

def find_right_trees(tree, x, y):
    trees = []
    for i in range(x+1, len(tree_lists[y])):
        trees.append(tree_lists[y][i])
        if tree_lists[y][i] >= tree:
            return trees
    return trees

def visible_top(tree, x, y):
    for i in range(0, y):
        if tree_lists[i][x] >= tree:
            return False
    return True

def find_top_trees(tree, x, y):
    trees = []
    for i in reversed(range(0, y)):
        trees.append(tree_lists[i][x])
        if tree_lists[i][x] >= tree:
            return trees
    return trees

def visible_bottom(tree, x, y):
    for i in range(y+1, len(tree_lists)):
        if tree_lists[i][x] >= tree:
            return False
    return True

def find_bottom_trees(tree, x, y):
    trees = []
    for i in range(y+1, len(tree_lists)):
        trees.append(tree_lists[i][x])
        if tree_lists[i][x] >= tree:
            return trees
    return trees

for y in range(1, len(tree_lists) - 1):
    for x in range(1, len(tree_lists[y]) - 1):
        tree = tree_lists[y][x]
        if (visible_left(tree, x, y)
            or visible_top(tree, x, y)
            or visible_right(tree, x, y)
            or visible_bottom(tree, x, y)
        ):
            visible_interior_trees += 1

        left_trees = find_left_trees(tree, x, y)
        right_trees = find_right_trees(tree, x, y)
        top_trees = find_top_trees(tree, x, y)
        bottom_trees = find_bottom_trees(tree, x, y)

        tree_scenic_score = len(left_trees) * len(right_trees) * len(top_trees) * len(bottom_trees)
        if tree_scenic_score > max_scenic_score:
            max_scenic_score = tree_scenic_score

print(f"PART ONE:")
print(f"Visible Perimeter Trees: {visible_perimiter_trees}")
print(f"Visible Interior Trees: {visible_interior_trees}")
print(f"Total Visible Trees: {visible_perimiter_trees + visible_interior_trees}")

print(f"PART TWO:")
print(f"Max Scenic Score: {max_scenic_score}")