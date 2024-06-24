first_set = set(int(a) for a in input().split())
second_set = set(int(b) for b in input().split())
n = int(input())

actions = {"Add First": lambda x:[first_set.add(int(el)) for el in x],
           "Add Second": lambda x:[second_set.add(int(el))for el in x],
           "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
           "Remove Second": lambda x: [second_set.discard(int(el))for el in x],
           "Check Subset": lambda x: print(second_set.issubset(first_set) or first_set.issubset(second_set)),
           }


for _ in range(n):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command

    actions[command](data)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")


