r, c = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(r)]

row_range = range(r)
column_range = range(c)

while True:
    command, *indices = [int(b) if b.isdigit() else b for b in input().split()]
    if command == "END":
        break

    if command == "swap" and len(indices) == 4 and {indices[0], indices[2]}.issubset(row_range) and {indices[1], indices[3]}.issubset(column_range):
        matrix[indices[0]][indices[1]], matrix[indices[2]][indices[3]] = matrix[indices[2]][indices[3]],  matrix[indices[0]][indices[1]]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
