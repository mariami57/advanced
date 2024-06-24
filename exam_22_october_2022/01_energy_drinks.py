from collections import deque
caffeine_mg = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))
total_caffeine = 0
while caffeine_mg and energy_drinks:
    current_caffeine = caffeine_mg.pop()
    current_eg_drink = energy_drinks.popleft()
    result = current_caffeine * current_eg_drink
    if result+total_caffeine <= 300:
        total_caffeine += result
    else:
        energy_drinks.append(current_eg_drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

result = ""
if energy_drinks:
    result += "Drinks left: "
    for e in energy_drinks:
        result += str(e) if e == energy_drinks[-1] else f"{str(e)}, "
    print(result)
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")