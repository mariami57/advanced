rows, cols = [int(x) for x in input().split()]
matrix = [[a for a in input().split()]for _ in range(rows)]
same = 0
for row_index in range(rows-1):
    for col_index in range(cols-1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] and matrix[row_index][col_index] == matrix[row_index+1][col_index]and matrix[row_index][col_index] == matrix[row_index+1][col_index + 1]:
            same += 1

print(same)
