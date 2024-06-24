from collections import deque

water = int(input())

name = input()
names_deque = deque()

while name != "Start":
    names_deque.append(name)
    name = input()

command = input()

while command != "End":
    command = command.split()
    if command[0] == "refill":
        water += int(command[1])
    elif command[0].isdigit():
        person = names_deque.popleft()
        if water >= int(command[0]):
            water -= int(command[0])
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    command = input()

print(f"{water} liters left")


