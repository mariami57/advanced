def find_player():
    for r in range(row):
        if "P" in matrix[r]:
            return r,  matrix[r].index("P")


def check_valid_index(row_index, col_index, player=False):
    global wins

    if 0 <= row_index < row and 0 <= col_index < col:
        return True
    if player:
        wins = True


def bunnies_positions():
    positions = []
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == "B":
                positions.append([r,c])
    return positions


def bunnies_move(positions):
    for r, c in positions:
        for bunny_move in commands.values():
            new_r, new_c = r + bunny_move[0], c + bunny_move[1]

            if check_valid_index(new_r,new_c):
                matrix[new_r][new_c] = "B"


def show_results(status="won"):
    [print(*r, sep ="")for r in matrix]
    print(f"{status}: {player_row} {player_col}")

    raise SystemExit


def check_player_alive(r, c):
    if matrix[r][c] == "B":
        show_results("dead")

row, col = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(row)]
directions = input()
wins = False
commands = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}

player_row, player_col = find_player()
matrix[player_row][player_col] = "."

for direction in directions:
    player_movement_row, player_movement_col = player_row + commands[direction][0], player_col + commands[direction][1]

    if check_valid_index(player_movement_row,player_movement_col, True):
        player_row,player_col = player_movement_row, player_movement_col

    bunnies_move(bunnies_positions())

    if wins:
        show_results()

    check_player_alive(player_row, player_col)


