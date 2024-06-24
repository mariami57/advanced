n, m = [int(x) for x in input().split()]
neighborhood = []
start_pos = []

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

DELIVERY_BOY_POSITION = "B"
ADDRESS = "A"
OBSTACLE = "*"
RESTAURANT = "P"
ROAD = "-"

for row in range(n):
    neighborhood.append(list(input()))
    if DELIVERY_BOY_POSITION in neighborhood[row]:
        start_pos = [row, neighborhood[row].index("B")]

boy_pos = start_pos
pizza_collected = False
while True:
    command = input()
    if command in directions:
        new_r = boy_pos[0] + directions[command][0]
        new_c = boy_pos[1] + directions[command][1]
        new_pos = [new_r, new_c]

        if not (0 <= new_r < n and 0 <= new_c < m):
            print("The delivery is late. Order is canceled.")
            neighborhood[start_pos[0]][start_pos[1]] = " "
            break
        else:
            if neighborhood[new_pos[0]][new_pos[1]] == OBSTACLE:
                new_pos = boy_pos
                continue
            elif neighborhood[new_pos[0]][new_pos[1]] == RESTAURANT:
                neighborhood[new_pos[0]][new_pos[1]] = "R"
                print("Pizza is collected. 10 minutes for delivery.")
                pizza_collected = True
            elif neighborhood[new_pos[0]][new_pos[1]] == ADDRESS:
                if pizza_collected:
                    neighborhood[new_pos[0]][new_pos[1]] = "P"
                    print("Pizza is delivered on time! Next order...")
                    break
            if neighborhood[new_pos[0]][new_pos[1]] == ROAD:
                neighborhood[new_pos[0]][new_pos[1]] = "."

        boy_pos = [new_pos[0], new_pos[1]]


[print("".join(row))for row in neighborhood]


