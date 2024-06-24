n = int(input())
matrix = [[int(row) for row in input().split()] for _ in range(n)]

command = input().split()
while command[0] != "END":
    action, row, column, number = command[0], int(command[1]), int(command[2]), int(command[3])
    if 0 <= row < n and 0 <= column < n:
        if action == "Add":
            matrix[row][column] += number
        elif action == "Subtract":
            matrix[row][column] -= number
    else:
        print("Invalid coordinates")

    command = input().split()

[print(*b) for b in matrix]