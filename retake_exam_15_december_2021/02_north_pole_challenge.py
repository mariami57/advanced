def check_coordinates(coordinate):
    m_r = your_pos[0] + directions[coordinate][0]
    m_c = your_pos[1] + directions[coordinate][1]

    if direction == 'up' or direction == 'down':
        if not (0 <= m_r < row):
            m_r = row - 1 if m_r < 0 else 0
    elif direction == 'left' or direction == 'right':
        if not (0 <= m_c < col):
            m_c = col - 1 if m_c < 0 else 0

    return m_r, m_c


row, col = [int(x) for x in input().split(", ")]
matrix = []
your_pos = []
total_items = 0
collected_items = []
flag = False
YOU = "Y"
DECORATIONS = "D"
GIFTS = "G"
COOKIES = "C"
EMPTY = "."

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

for r in range(row):
    matrix.append(input().split())
    if YOU in matrix[r]:
        your_pos = [r, matrix[r].index(YOU)]
        matrix[your_pos[0]][your_pos[1]] = "x"
    if DECORATIONS in matrix[r] or GIFTS in matrix[r] or COOKIES in matrix[r]:
        total_items += matrix[r].count(DECORATIONS)
        total_items += matrix[r].count(GIFTS)
        total_items += matrix[r].count(COOKIES)


command = input()
while command != "End":
    direction, steps = command.split("-")
    turns = 0
    while int(steps) != turns:
        current_row, current_col = check_coordinates(direction)
        if matrix[current_row][current_col].isalpha() and matrix[current_row][current_col] != "x":
            collected_items.append(matrix[current_row][current_col])

        if len(collected_items) == total_items:
            matrix[current_row][current_col] = YOU
            print("Merry Christmas!")
            flag = True
            break

        your_pos[0] = current_row
        your_pos[1] = current_col

        matrix[current_row][current_col] = "x"
        turns += 1

    if flag:
        break

    command = input()
    if command == "End":
        matrix[your_pos[0]][your_pos[1]] = YOU


print("You've collected:")
print(f"- {collected_items.count(DECORATIONS)} Christmas decorations")
print(f"- {collected_items.count(GIFTS)} Gifts")
print(f"- {collected_items.count(COOKIES)} Cookies")

[print(*x, sep=" ") for x in matrix]

