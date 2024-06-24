row, column = [int(x) for x in input().split(", ")]
sum_columns = 0
matrix = []

for _ in range(row):
    row_data = [int(r) for r in input().split()]
    matrix.append(row_data)

for i in range(column):
    sum_columns = 0
    for row_index in range(row):
        sum_columns += matrix[row_index][i]
    print(sum_columns)