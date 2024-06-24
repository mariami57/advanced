n = int(input())
kilometers = 0
racing_number = input()
matrix = []
car_pos = [0, 0]
CAR = "C"
TUNNEL = "T"
EMPTY = "."
FINISH = "F"
tunnel_pos_one = []
tunnel_pos_two = []

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

for row in range(n):
    line = input().split()
    matrix.append(line)
    if TUNNEL in line and not tunnel_pos_one:
        tunnel_pos_one = [row, matrix[row].index(TUNNEL)]
    elif TUNNEL in line and tunnel_pos_one:
        tunnel_pos_two = [row, matrix[row].index(TUNNEL)]

command = input()

while command != "End":
    if command in directions:
        r = car_pos[0] + directions[command][0]
        c = car_pos[1] + directions[command][1]
        if r == tunnel_pos_one[0] and c == tunnel_pos_one[1]:
            r = tunnel_pos_two[0]
            c = tunnel_pos_two[1]
            matrix[tunnel_pos_one[0]][tunnel_pos_one[1]] = "."
            kilometers += 20
        elif r == tunnel_pos_two[0] and c == tunnel_pos_two[1]:
            r = tunnel_pos_one[0]
            c = tunnel_pos_one[1]
            matrix[tunnel_pos_two[0]][tunnel_pos_two[1]] = "."
            kilometers += 20
        elif matrix[r][c] == FINISH:
            kilometers += 10
            matrix[r][c] = CAR
            print(f"Racing car {racing_number} finished the stage!")
            break
        matrix[r][c] = "."
        kilometers += 10
        car_pos[0] = r
        car_pos[1] = c
    command = input()
else:
    matrix[car_pos[0]][car_pos[1]] = CAR
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {kilometers} km.")

[print(*row, sep="") for row in matrix]