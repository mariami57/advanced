size = int(input())
matrix = []
current_pos = []

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

best_direction = ""
best_path = []
max_eggs = float("-inf")

for row in range(size):
    matrix.append(input().split())
    if "B" in matrix[row]:
        current_pos = [row, matrix[row].index("B")]

for direction, coordinates in directions.items():
    r = int(current_pos[0]) + int(coordinates[0])
    c = int(current_pos[1]) + int(coordinates[1])

    path = []
    collected_eggs = 0
    while (0 <= r < size and 0 <= c < size) and matrix[r][c] != "X":
        collected_eggs += int(matrix[r][c])
        path.append([r, c])

        r += int(coordinates[0])
        c += int(coordinates[1])

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_path = path
        best_direction = direction



print(best_direction)
print(*best_path, sep="\n")
print(max_eggs)

