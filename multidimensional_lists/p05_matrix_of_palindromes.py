r, c = [int(x)for x in input().split()]
start_index = ord('a')

for row in range(start_index, start_index+r):
    for column in range(row, row + c):
        print(chr(row), chr(column), chr(row), sep="", end=" ")

    print()

