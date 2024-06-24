n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
first_diagonal = []
second_diagonal = []
for row_index in range(n):
    second_diagonal.append(matrix[row_index][n - row_index - 1])
    for col_index in range(n):
        if row_index == col_index:
            first_diagonal.append(matrix[row_index][col_index])

print(f"Primary diagonal: {', '.join(str(a) for a in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(a) for a in second_diagonal)}. Sum: {sum(second_diagonal)}")

