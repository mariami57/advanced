from collections import deque
petrol_pumps = int(input())
trucks = deque()
for truck in range(petrol_pumps):
    amount, distance = input().split()
    trucks.append([int(amount), int(distance)])
tank = 0
index = 0
trucks_copy = trucks.copy()
while trucks_copy:
    amount, distance = trucks_copy.popleft()
    tank += amount
    if tank < distance:
        trucks.rotate(-1)
        trucks_copy = trucks.copy()
        index += 1
        tank = 0
    else:
        tank -= distance

print(index)