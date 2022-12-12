#!/usr/bin/env python3

import re, pprint, heapq

from collections import defaultdict

contents = None
with open('input.txt', 'r') as f:
    contents = f.read()
# print(contents)

# probly def functions here
def split_monkeys(contents):
    return contents.split('\n\n')

monkeys = split_monkeys(contents)
m_dict = {}
monkey_inspected_items = defaultdict(int)

for m in monkeys:
    monkey = m.splitlines()
    numb = re.search(r'\d', monkey[0])[0]
    # print(numb)
    items = re.search(r'Starting items: (.*)', monkey[1]).group(1).split(', ')
    # print(items)
    operation = re.search(r'Operation: new = (.*)', monkey[2]).group(1)
    # print(operation)
    divisor = int(re.search(r'\d+$', monkey[3])[0])
    # print(divisor)
    true_throw = re.search(r'\d$', monkey[4])[0]
    # print(true_throw)
    false_throw = re.search(r'\d$', monkey[5])[0]
    # print(false_throw)
    monkey_inspected_items[numb] = 0
    m_dict[numb] = {
        "items": items,
        "operation": operation,
        "divisor": divisor,
        "true_throw": true_throw,
        "false_throw": false_throw
    }
def monkey_throw(catcher, worry):
    global m_dict

    m_dict[catcher]['items'].append(worry)


def monkey_turn(monkey):
    # global m_dict

    for i in range(0, len(monkey['items'])):

        old = int(monkey['items'].pop(0))
        # print(f"\tinspecting item: {old}")
        new = eval(monkey['operation']) // 3
        # print(f"\tnew worry level: {new}")
        # print(new)
        # print(f"\tmonkey test: {new} / {monkey['divisor']}")
        if new % monkey['divisor'] == 0:
            # print(f"\tTEST TRUE throwing to monkey: {monkey['true_throw']}")
            monkey_throw(monkey['true_throw'], new)
            # m_dict['true_throw']['items'].append(new)
        else:
            # print(f"\tTEST FALSE throwing to monkey: {monkey['false_throw']}")
            monkey_throw(monkey['false_throw'], new)
            # m_dict['false_throw']['items'].append(new)

# pprint.pprint(m_dict)

for i in range(0, 20):
    for m in m_dict:
        # print(f"monkey {m}")
        monkey_inspected_items[m] += len(m_dict[m]['items'])
        monkey_turn(m_dict[m])
        # print(f"")

# monkey_business =
monkey_business = 1
monkey_business_dict = heapq.nlargest(2, monkey_inspected_items.items(), key=lambda i: i[1])
for k, v in monkey_business_dict:
    monkey_business *= v
# print(monkey_business)
# pprint.pprint(m_dict)
# pprint.pprint(dict(monkey_inspected_items))
print(f"Part 01: {monkey_business}")
print(f"Part 02: {None}")
