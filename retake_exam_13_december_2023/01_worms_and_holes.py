from collections import deque

worms = [int(x) for x in input().split()]
worms_copy = worms.copy()
holes = deque(int(x) for x in input().split())
matches = 0
while worms and holes:
    current_worm = worms.pop()
    if current_worm <= 0:
        continue
    current_hole = holes.popleft()
    if current_hole != current_worm:
        worms.append(current_worm - 3)
    else:
        matches += 1


print(f"Matches: {matches}" if matches else f"There are no matches.")

if not worms and matches == len(worms_copy):
    print("Every worm found a suitable hole!")

elif not worms and matches != len(worms_copy):
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(str(w) for w in worms)}")


print(f"Holes left: {', '.join(str(h) for h in holes)}" if holes else f"Holes left: none")


