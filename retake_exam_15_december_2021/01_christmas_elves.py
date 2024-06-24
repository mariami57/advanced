from collections import deque

elf_energy = deque(int(x) for x in input().split())
materials = [int(x) for x in input().split()]
turns = 0
total_used_energy = 0
total_toys = 0
cookie = 1
hot_chocolate = 2

while elf_energy and materials:
    current_elf = elf_energy.popleft()
    current_materials = materials[-1]

    if current_elf < 5:
        continue

    turns += 1
    current_toys = 0

    if turns % 3 == 0:
        current_materials *= 2
        current_toys += 1

    if current_elf >= current_materials:
        total_used_energy += current_materials
        current_elf -= current_materials

        if turns % 5 == 0:
            current_toys = 0
        else:
            current_toys += 1
            current_elf += cookie
        materials.pop()

    else:
        current_elf *= hot_chocolate
        current_toys = 0

    total_toys += current_toys
    elf_energy.append(current_elf)


print(f"Toys: {total_toys}")

print(f"Energy: {total_used_energy}")

if elf_energy:
    print(f"Elves left: {', '.join(str(e) for e in elf_energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(m) for m in materials)}")

