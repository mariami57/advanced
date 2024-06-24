n, m = [int(x) for x in input().split(",")]
area = []
mouse_pos = []
count_cheese = 0
directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

MOUSE = "M"
CHEESE = "C"
EMPTY = "*"
WALL = "@"
TRAP = "T"


for row in range(n):
    line = list(input())
    area.append(line)

    if MOUSE in line:
        mouse_pos = [row, area[row].index(MOUSE)]
        area[mouse_pos[0]][mouse_pos[1]] = EMPTY

    if CHEESE in line:
        count_cheese += line.count(CHEESE)

command = input()

while command != "danger":
    if command in directions:
        r = mouse_pos[0] + directions[command][0]
        c = mouse_pos[1] + directions[command][1]
        if 0 <= r < n and 0 <= c < m:
            if area[r][c] == WALL:
                r = mouse_pos[0]
                c = mouse_pos[1]
                command = input()
                continue
            if area[r][c] == CHEESE:
                area[r][c] = "*"
                count_cheese -= 1
                if count_cheese == 0:
                    area[r][c] = "M"
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
            elif area[r][c] == TRAP:
                area[r][c] = "M"
                print("Mouse is trapped!")
                break
            mouse_pos[0] = r
            mouse_pos[1] = c

        else:
            area[mouse_pos[0]][mouse_pos[1]] = "M"
            print("No more cheese for tonight!")
            break

    command = input()

else:
    area[r][c] = "M"
    print("Mouse will come back later!")

[print("".join(row)) for row in area]


