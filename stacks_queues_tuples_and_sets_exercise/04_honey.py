from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(y) for y in input().split()]
symbols = deque(x for x in input().split())
total_honey = 0
calculations = {
    "+": lambda a, b: a+b,
    "-": lambda a, b: a-b,
    "*": lambda a, b: a*b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
    else:
        total_honey += abs(calculations[symbols.popleft()](current_bee, current_nectar))

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(y) for y in nectar)}")
