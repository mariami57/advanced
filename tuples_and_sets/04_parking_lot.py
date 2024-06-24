n_of_commands = int(input())

cars = set()

for _ in range(n_of_commands):
    direction, number_car = input().split(", ")
    if direction == "IN":
        cars.add(number_car)
    elif direction == "OUT" and number_car in cars:
        cars.remove(number_car)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")