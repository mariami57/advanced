rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
max_sum = float("-inf")
sub_matrix = []
for row_index in range(rows-1):
    for col_index in range(cols-1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index+1]
        below_el = matrix[row_index+1][col_index]
        diagonal_el = matrix[row_index+1][col_index+1]

        total_sum = current_el + next_el + below_el + diagonal_el

        if total_sum > max_sum:
            max_sum = total_sum
            sub_matrix = [[current_el, next_el], [below_el, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
