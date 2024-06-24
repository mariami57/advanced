from collections import deque

monster_armour = deque([int(x) for x in input().split(",")])
strike_strength = [int(s) for s in input().split(",")]
total_monsters_killed = 0

while monster_armour and strike_strength:
    current_strength = strike_strength.pop()
    current_monster = monster_armour.popleft()
    if current_strength >= current_monster:
        total_monsters_killed += 1
        current_strength -= current_monster
        if strike_strength:
            strike_strength[-1] += current_strength
        elif not strike_strength and current_strength > 0:
            strike_strength.append(current_strength)
    else:
        current_monster -= current_strength
        monster_armour.append(current_monster)

if not monster_armour:
    print("All monsters have been killed!")

if not strike_strength:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {total_monsters_killed}")


