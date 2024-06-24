size = int(input())
movement_commands = input().split(", ")
hazelnuts_collected = 0
matrix = []
position = []

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}
TOTAL_HAZELNUTS = 3
SQUIRREL = "s"
HAZELNUT = "h"
EMPTY = "*"
TRAP = "t"
flag = False

for row in range(size):
    line = list(input())
    matrix.append(line)
    if SQUIRREL in line:
        position = [row, matrix[row].index(SQUIRREL)]
        matrix[position[0]][position[1]] = EMPTY

for command in movement_commands:
    r = position[0] + directions[command][0]
    c = position[1] + directions[command][1]

    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == HAZELNUT:
            hazelnuts_collected += 1
            if hazelnuts_collected == TOTAL_HAZELNUTS:
                print("Good job! You have collected all hazelnuts!")
                matrix[r][c] = EMPTY
                position = [r, c]
                break
        elif matrix[r][c] == TRAP:
            print("Unfortunately, the squirrel stepped on a trap...")
            break
        elif matrix[r][c] == EMPTY:
            position = [r, c]
            flag = True
    else:
        print("The squirrel is out of the field.")
        flag = True
        break
    position[0] = r
    position[1] = c

if not flag and hazelnuts_collected < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_collected}")







