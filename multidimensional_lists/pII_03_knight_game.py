n = int(input())
matrix = [list(input()) for _ in range(n)]


directions = {
    "up right": [-2, 1],
    "up left": [-2, -1],
    "middle right up": [-1, 2],
    "middle left up": [-1, -2],
    "middle right down": [1, 2],
    "middle left down": [1, -2],
    "down right": [2, 1],
    "down left": [2, -1]
}

removed_knights = 0
while True:
    max_n_attacks = 0
    knight_with_max_attacks_pos = []
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                n_attacks = 0

                for key, value in directions.items():
                    pos_row = row + directions[key][0]
                    pos_col = col + directions[key][1]

                    if 0 <= pos_row < n and 0 <= pos_col < n:
                        if matrix[pos_row][pos_col] == "K":
                            n_attacks += 1

                if n_attacks > max_n_attacks:
                    max_n_attacks = n_attacks
                    knight_with_max_attacks_pos = [row, col]

    if knight_with_max_attacks_pos:
        matrix[knight_with_max_attacks_pos[0]][knight_with_max_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)