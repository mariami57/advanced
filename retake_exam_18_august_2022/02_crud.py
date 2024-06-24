SIZE = 6
matrix = []

for row in range(SIZE):
    line = input().split()
    matrix.append(line)

position = input()
my_pos = []
for p in position:
    if p.isdigit():
        my_pos.append(int(p))
directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

command = input().split(", ")

while command[0] != "Stop":
    if command[1] in directions:
        r = my_pos[0] + directions[command[1]][0]
        c = my_pos[1] + directions[command[1]][1]
        if matrix[r][c] == ".":
            if command[0] == "Create":
                matrix[r][c] = command[2]
        elif matrix[r][c].isalpha() or matrix[r][c].isdigit():
            if command[0] == "Update":
                matrix[r][c] = command[2]
            elif command[0] == "Delete":
                matrix[r][c] = "."
            elif command[0] == "Read":
                print(matrix[r][c])
        my_pos[0] = r
        my_pos[1] = c
        command = input().split(", ")

[print(*row) for row in matrix]







