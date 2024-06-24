from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]
created_items = {}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    result = current_textile + current_medicament

    if result == 30:
        created_items["Patch"] = created_items.get("Patch", 0) + 1
    elif result == 40:
        created_items["Bandage"] = created_items.get("Bandage", 0) + 1
    elif result >= 100:
        created_items["MedKit"] = created_items.get("MedKit", 0) + 1
        if result > 100:
            result -= 100
            medicaments[-1] += result
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")


elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
for item, number in sorted_items:
    print(f"{item} - {number}")


if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")



