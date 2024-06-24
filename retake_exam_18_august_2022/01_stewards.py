from collections import deque
seats = input().split(", ")
first_sequence = deque(int(x) for x in input().split(", "))
second_sequence = deque(int(x) for x in input().split(", "))
matched_seats = []
rotations = 0

while first_sequence and second_sequence:
    num1 = first_sequence.popleft()
    num2 = second_sequence.pop()
    result = num2 + num1
    char = chr(result)
    seat_one = str(num1) + char
    seat_two = str(num2) + char
    if seat_one in seats:
        if seat_one not in matched_seats:
            matched_seats.append(seat_one)
    elif seat_two in seats:
        if seat_two not in matched_seats:
            matched_seats.append(seat_two)
    else:
        first_sequence.append(num1)
        second_sequence.appendleft(num2)
    rotations += 1
    if len(matched_seats) == 3:
        break
    if rotations == 10:
        break

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")