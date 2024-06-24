n = int(input())

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

SUBMARINE = "S"
EMPTY = "-"
MINE = "*"
CRUISER = "C"

sub_pos = []
battlefield = []
n_mines = 0
n_cruisers = 0

for row in range(n):
    line = list(input())
    battlefield.append(line)
    if SUBMARINE in line:
        sub_pos = [row, battlefield[row].index(SUBMARINE)]
        battlefield[sub_pos[0]][sub_pos[1]] = EMPTY

command = input()

while True:
    if command in directions:
        r = sub_pos[0] + directions[command][0]
        c = sub_pos[1] + directions[command][1]
        if 0 <= r < n and 0 <= c < n:
            if battlefield[r][c] == MINE:
                n_mines += 1

                if n_mines == 3:
                    print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
                    battlefield[r][c] = SUBMARINE
                    break
            elif battlefield[r][c] == CRUISER:
                n_cruisers += 1
                if n_cruisers == 3:
                    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                    battlefield[r][c] = SUBMARINE
                    break

            battlefield[r][c] = EMPTY
            sub_pos[0] = r
            sub_pos[1] = c
            command = input()
[print(*row, sep="") for row in battlefield]
