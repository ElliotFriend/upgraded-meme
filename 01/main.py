elf_lists = None
with open('input.txt', 'r') as f:
    elf_lists = f.read().splitlines()

lists_dict = {}

carrying_calories = []
elf_cal = 0

for item in elf_lists:
    if item != '':
        elf_cal += int(item)
    else:
        carrying_calories.append(elf_cal)
        elf_cal = 0

carrying_calories.sort(reverse=True)
print(carrying_calories)

print(f"Max Calorie Carrier has: {carrying_calories[0]}")
print(
    f"Top Three Carriers have: {carrying_calories[0] + carrying_calories[1] + carrying_calories[2]}")


