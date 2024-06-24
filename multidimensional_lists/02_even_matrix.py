row = int(input())

matrix = []
for i in range(row):
    row_data =[int(x) for x in input().split(", ")]
    matrix.append([element for element in row_data if element % 2 == 0])
    # for element in row_data:
    #     if element % 2 == 0:
    #         sub_list.append(element)
    # matrix.append(sub_list)

print(matrix)