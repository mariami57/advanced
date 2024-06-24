rows, columns = [int(x)for x in input().split(",")]
matrix = []
matrix_sum = 0
for _ in range(rows):
    sub_matrix = [int(el) for el in input().split(", ")]
    matrix_sum += sum(sub_matrix)
    matrix.append(sub_matrix)

print(matrix_sum)
print(matrix)