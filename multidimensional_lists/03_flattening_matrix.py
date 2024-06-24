rows = int(input())
matrix = []
for _ in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    for el in row_data:
        matrix.append(el)

print(matrix)