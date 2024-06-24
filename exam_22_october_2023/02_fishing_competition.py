n = int(input())
quantity = 0
fishing_area = []
fisherman_pos = []
whirlpool_flag = False
directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

for row in range(n):
    fishing_area.append(list(input()))
    if "S" in fishing_area[row]:
        fisherman_pos = [row, fishing_area[row].index("S")]
        fishing_area[fisherman_pos[0]][fisherman_pos[1]] = "-"

command = input()

while command != "collect the nets":
    new_pos_r = fisherman_pos[0] + directions[command][0]
    new_pos_c = fisherman_pos[1] + directions[command][1]


    if command == "right" and new_pos_c >= n:
        new_pos_c = 0
    elif command == "left" and new_pos_c < 0:
        new_pos_c = n-1
    elif command == "up" and new_pos_r < 0:
        new_pos_r = n-1
    elif command == "down" and new_pos_r >= n:
        new_pos_r = 0
    new_position = str(fishing_area[new_pos_r][new_pos_c])

    if new_position.isdigit():
        quantity += int(new_position)

    fisherman_pos = [new_pos_r,new_pos_c]
    fishing_area[fisherman_pos[0]][fisherman_pos[1]] = "-"

    if new_position == "W":
        print("You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: ", end="")
        print("[", end="")
        print(*fisherman_pos, sep=",", end="")
        print("]")
        whirlpool_flag = True
        break

    command = input()
fishing_area[fisherman_pos[0]][fisherman_pos[1]] = "S"

if not whirlpool_flag:
    if quantity >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - quantity} tons of fish more.")

    if quantity > 0:
        print(f"Amount of fish caught: {quantity} tons.")

    [print("".join(row)) for row in fishing_area]