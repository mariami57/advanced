from collections import deque

empty_stack = deque()
n_commands = int(input())

for _ in range(n_commands):
    command = input().split()
    if len(command) == 2:
        empty_stack.appendleft(int(command[1]))
    if empty_stack:
        if int(command[0]) == 2:
            removed = empty_stack.popleft()
        elif int(command[0]) == 3:
            print(max(empty_stack))
        elif int(command[0]) == 4:
            print(min(empty_stack))

print(*empty_stack, sep=", ")

