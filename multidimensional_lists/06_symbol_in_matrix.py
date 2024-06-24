row = int(input())
matrix = [[x for x in input()] for _ in range(row)]
symbol = input()

for row_index in range(row):
    for col_index in range(row):
        if matrix[row_index][col_index] == symbol:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{symbol} does not occur in the matrix")