n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = ((int(x) for x in c.split(",")) for c in input().split())

directions = (
    (-1, 0),    #UP
    (1, 0),     #DOWN
    (0, -1),    #LEFT
    (0, 1),     #RIGHT
    (-1, -1),   #UP-LEFT
    (-1, 1),    #UP-RIGHT
    (1, -1),    #DOWN-LEFT
    (1, 1),      #DOWN-RIGHT
    (0, 0)
)

for row, column in bombs:
    if matrix[row][column] <= 0:
        continue
    for x, y in directions:
        r, c = row + x, column + y
        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][column] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]


