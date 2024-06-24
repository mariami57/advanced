n = int(input())
airspace = []
jet_pos = []
armour = 300
enemy_total = 4

JET_FIGHTER = "J"
ENEMY = "E"
REPAIR = "R"
EMPTY = "-"

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

for row in range(n):
    airspace.append(list(input()))
    if JET_FIGHTER in airspace[row]:
        jet_pos = [row, airspace[row].index(JET_FIGHTER)]
        airspace[jet_pos[0]][jet_pos[1]] = EMPTY

command = input()

while enemy_total and armour:
    if command in directions:
        r = jet_pos[0] + directions[command][0]
        c = jet_pos[1] + directions[command][1]
        if 0 <= r < n and 0 <= c < n:
            if airspace[r][c] == ENEMY:
                enemy_total -= 1
                if enemy_total == 0:
                    print("Mission accomplished, you neutralized the aerial threat!")
                    airspace[r][c] = JET_FIGHTER
                    break
                else:
                    armour -= 100
                    if armour == 0:
                        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
                        airspace[r][c] = JET_FIGHTER
                        break
            if airspace[r][c] == "R":
                armour = 300
            airspace[r][c] = EMPTY
            jet_pos[0] = r
            jet_pos[1] = c
    command = input()


[print(*row, sep="") for row in airspace]
