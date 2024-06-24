n = int(input())
matrix = []

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}
collected_teabags = 0
alice_pos = []

for row in range(n):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[row][alice_pos[1]] = "*"

while collected_teabags < 10:
    direction = input()
    alice_pos[0] += + directions[direction][0]
    alice_pos[1] += directions[direction][1]

    if not (0 <= alice_pos[0] < n and 0 <= alice_pos[1] < n):
        break

    if matrix[alice_pos[0]][alice_pos[1]] == "R":
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        break

    elif matrix[alice_pos[0]][alice_pos[1]].isdigit():
        collected_teabags += int(matrix[alice_pos[0]][alice_pos[1]])

    matrix[alice_pos[0]][alice_pos[1]] = "*"


if collected_teabags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*r) for r in matrix]



