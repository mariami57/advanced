SIZE = 6
ROVER = "E"
WATER_DEPOSIT = "W"
METAL_DEPOSIT = "M"
CONCRETE_DEPOSIT = "C"
ROCK = "R"
EMPTY = "-"

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

matrix = []
rover_pos = []
water = 0
metal = 0
concrete = 0

for row in range(SIZE):
    line = input().split()
    matrix.append(line)
    if ROVER in line:
        rover_pos = [row,matrix[row].index(ROVER)]
        matrix[rover_pos[0]][rover_pos[1]] = EMPTY

while True:
    command = input().split(", ")
    for direction in command:
        if direction == "up" and rover_pos[0] == 0:
            r = SIZE - 1
        elif direction == "down" and rover_pos[0] == SIZE - 1:
            r = 0
        else:
            r = rover_pos[0] + directions[direction][0]
        if direction == "left" and rover_pos[1] == 0:
            c = SIZE - 1
        elif direction == "right" and rover_pos[1] == SIZE - 1:
            c = 0
        else:
            c = rover_pos[1] + directions[direction][1]

        if matrix[r][c] == WATER_DEPOSIT:
            print(f"Water deposit found at ({r}, {c})")
            water += 1
        elif matrix[r][c] == METAL_DEPOSIT:
            metal += 1
            print(f"Metal deposit found at ({r}, {c})")
        elif matrix[r][c] == CONCRETE_DEPOSIT:
            concrete += 1
            print(f"Concrete deposit found at ({r}, {c})")
        elif matrix[r][c] == ROCK:
            print(f"Rover got broken at ({r}, {c})")
            break

        rover_pos[0] = r
        rover_pos[1] = c
    break


if metal and water and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

