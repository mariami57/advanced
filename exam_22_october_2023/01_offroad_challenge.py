from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_index = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())
altitude_list = deque()
altitude = 0
while initial_fuel:
    result = initial_fuel.pop() - consumption_index.popleft()
    altitude += 1
    if result >= amount_of_fuel_needed.popleft():
        print(f"John has reached: Altitude {altitude}")
        altitude_list.append(altitude)
        if not amount_of_fuel_needed:
            print("John has reached all the altitudes and managed to reach the top!")
            break
    else:
        print(f"John did not reach: Altitude {altitude}")
        print(f"John failed to reach the top.")
        if altitude_list:
            print('Reached altitudes: ', end='')
            while altitude_list:
                current_altitude = altitude_list.popleft()
                end_char = ', ' if altitude_list else ''
                print(f'Altitude {current_altitude}', end=end_char)
        else:
             print("John didn't reach any altitude.")

        break

else:
    print('John has reached all the altitudes and managed to reach the top!')





