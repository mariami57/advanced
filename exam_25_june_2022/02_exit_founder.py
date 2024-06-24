players = input().split(", ")
matrix = []
wall_flag_pl_one = False
wall_flag_pl_two = False
turn = 1
SIZE = 6
EXIT = "E"
TRAP = "T"
WALL = "W"
EMPTY = "."

for _ in range(SIZE):
    matrix.append(input().split())

while True:
    coordinates = []
    input_line = list(input())
    for c in input_line:
        if c.isdigit():
            coordinates.append(int(c))
    if wall_flag_pl_one and turn % 2 != 0:
        wall_flag_pl_one = False
        turn += 1
        continue
    if wall_flag_pl_two and turn % 2 == 0:
        wall_flag_pl_two = False
        turn += 1
        continue
    if 0 <= coordinates[0] < SIZE and 0 <= coordinates[1] < SIZE:
        if turn % 2 != 0:
            if matrix[coordinates[0]][coordinates[1]] == EXIT:
                print(f"{players[0]} found the Exit and wins the game!")
                break
            elif matrix[coordinates[0]][coordinates[1]] == TRAP:
                print(f"{players[0]} is out of the game! The winner is {players[1]}.")
                break
            elif matrix[coordinates[0]][coordinates[1]] == WALL:
                print(f"{players[0]} hits a wall and needs to rest.")
                wall_flag_pl_one = True
                turn += 1
                continue
            turn += 1

        elif turn % 2 == 0:
            if matrix[coordinates[0]][coordinates[1]] == EXIT:
                print(f"{players[1]} found the Exit and wins the game!")
                break
            elif matrix[coordinates[0]][coordinates[1]] == TRAP:
                print(f"{players[1]} is out of the game! The winner is {players[0]}.")
                break
            elif matrix[coordinates[0]][coordinates[1]] == WALL:
                print(f"{players[1]} hits a wall and needs to rest.")
                wall_flag_pl_two = True
                turn += 1
                continue
            turn += 1



