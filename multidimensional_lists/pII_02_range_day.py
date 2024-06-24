def move(direction, steps):
    r = player_pos[0] + (directions[direction][0] * steps)
    c = player_pos[1] + (directions[direction][1] * steps)

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return player_pos

    if matrix[r][c] == "x":
        return player_pos

    return [r, c]


def shoot(direction):
    r = player_pos[0] + directions[direction][0]
    c = player_pos[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
total_targets = 0
targets_hit = 0
targets_hit_position = []
matrix = []

directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

for row in range(SIZE):
    matrix.append(input().split())

    if "A" in matrix[row]:
        player_pos = [row, matrix[row].index("A")]

    total_targets += matrix[row].count("x")


for _ in range(int(input())):
    command = input().split()
    if command[0] == "move":
        player_pos = move(command[1], int(command[2]))

    elif command[0] == "shoot":
        targets_hit_pos = shoot(command[1])

        if targets_hit_pos:
            targets_hit_position.append(targets_hit_pos)
            targets_hit += 1

        if targets_hit == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break

if total_targets > targets_hit:
    print(f"Training not completed! {total_targets - targets_hit} targets left.")

print(*targets_hit_position, sep="\n")



