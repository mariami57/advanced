n, m = (int(x) for x in input().split())
matrix = []
touched_opponents = 0
moves = 0
blindman_pos = []

BLIND = "B"
OPPONENT = "P"
OBSTACLE = "O"
EMPTY = "-"
TOTAL_OPPONENTS = 3

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

for row in range(n):
    line = input().split()
    matrix.append(line)
    if BLIND in line:
        blindman_pos = [row, matrix[row].index(BLIND)]
        matrix[blindman_pos[0]][blindman_pos[1]] = EMPTY

command = input()

while command != "Finish":
    if command in directions:
        desired_row = blindman_pos[0] + directions[command][0]
        desired_col = blindman_pos[1] + directions[command][1]

        if 0 <= desired_row < n and 0 <= desired_col < m:
            if matrix[desired_row][desired_col] == OBSTACLE:
                command = input()
                continue
            elif matrix[desired_row][desired_col] == OPPONENT:
                touched_opponents += 1
                if touched_opponents == TOTAL_OPPONENTS:
                    moves += 1
                    matrix[desired_row][desired_col] = EMPTY
                    blindman_pos = [desired_row, desired_col]
                    break
            moves += 1
            matrix[desired_row][desired_col] = EMPTY
            blindman_pos = [desired_row, desired_col]

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
