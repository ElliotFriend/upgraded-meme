import string

sacks = None
with open('input.txt', 'r') as f:
    sacks = f.read().splitlines()

alphabet = list(string.ascii_letters)

priority_sum = 0

for sack in sacks:
    # print(f"{sack[:len(sack)//2]} - {sack[len(sack)//2:]}")
    comp1 = sack[:len(sack)//2]
    comp2 = sack[len(sack)//2:]
    for item in comp1:
        if item in comp2:
            # print(f"{item}: {alphabet.index(item) + 1}pts")
            priority_sum += alphabet.index(item) + 1
            break

print(priority_sum)