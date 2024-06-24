def eat_cookies(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if matrix[r][c].isalpha():

            if matrix[r][c] == "V":
                nice_kids += 1

            matrix[r][c] = "-"
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


n_presents = int(input())
neighbourhood_size = int(input())
matrix = []
nice_kids_gifted = 0
total_nice_kids = 0
santa_pos = []
directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

for row in range(neighbourhood_size):
    matrix.append(input().split())
    if "S" in matrix[row]:
        santa_pos = [row, matrix[row].index("S")]
        matrix[santa_pos[0]][santa_pos[1]] = "-"

    total_nice_kids += matrix[row].count("V")

command = input()

while command != "Christmas morning":
    santa_pos = [santa_pos[0] + directions[command][0],
                 santa_pos[1] + directions[command][1]
                 ]
    house = matrix[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_gifted += 1
        n_presents -= 1

    elif house == "C":
        n_presents, nice_kids_gifted = eat_cookies(n_presents, nice_kids_gifted)

    matrix[santa_pos[0]][santa_pos[1]] = "-"

    if n_presents <= 0 or nice_kids_gifted == total_nice_kids:
        break

    command = input()

matrix[santa_pos[0]][santa_pos[1]] = "S"

if n_presents <= 0 and nice_kids_gifted < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]
if nice_kids_gifted == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_gifted} nice kid/s.")




