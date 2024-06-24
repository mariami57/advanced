row, columns = [int(x) for x in input().split()]
matrix = [[int(a) for a in input().split()] for _ in range(row)]
max_sum = float("-inf")
sub_matrix = []

for row_index in range(row-2):
    for col_index in range(columns - 2):
       first_row = matrix[row_index][col_index:col_index+3]
       second_row = matrix[row_index+1][col_index:col_index+3]
       third_row = matrix[row_index+2][col_index:col_index+3]

       total_sum = sum(first_row) + sum(second_row) + sum(third_row)
       if total_sum >= max_sum:
           max_sum = total_sum
           sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")

[print(*row) for row in sub_matrix]

