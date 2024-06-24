n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum_diagonal = 0

for row_index in range(n):
    for col_index in range(n):
        if row_index == col_index:
            sum_diagonal += matrix[row_index][col_index]

print(sum_diagonal)