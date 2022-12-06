import string

sacks = None
with open('input.txt', 'r') as f:
    sacks = f.read().splitlines()

alphabet = list(string.ascii_letters)
priority_sum = 0

# for sack in sacks:
#     comp1 = sack[:len(sack)//2]
#     comp2 = sack[len(sack)//2:]
#     for item in comp1:
#         if item in comp2:
#             priority_sum += alphabet.index(item) + 1
#             break

for group_sacks in [[sacks[i:i+3]] for i in range(0, len(sacks), 3)]:
    sack0 = group_sacks[0][0]
    sack1 = group_sacks[0][1]
    sack2 = group_sacks[0][2]
    for char in sack0:
        if char in sack1 and char in sack2:
            priority_sum += alphabet.index(char) + 1
            break

print(priority_sum)