from collections import deque

command = input()
names = deque()

while command != "End":
    if command == "Paid":
        while names:
            print(names.popleft())
    else:
        names.append(command)

    command = input()

print(f"{len(names)} people remaining.")