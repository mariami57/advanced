SIZE = 8
matrix = []
positions = [[], []]

for row in range(SIZE):
    matrix.append(input().split())
    if "w" in matrix[row]:
        positions[0] = [row, matrix[row].index("w")]
    elif "b" in matrix[row]:
        positions[1] = [row, matrix[row].index("b")]

if abs(positions[0][1] - positions[1][1]) != 1:
    if SIZE - positions[0][0] - 1 <= positions[1][0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97+positions[1][1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97+positions[0][1])}8.")

else:
    place = (positions[0][0] + positions[1][0]) // 2
    if positions[0][0] % 2 == positions[1][0] % 2:
        print(f"Game over! Black win, capture on {chr(97+positions[0][1])}{SIZE - place}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")