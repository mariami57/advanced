from collections import deque

clothes = deque([int(x)for x in input().split()])
rack_capacity = int(input())
n_racks = 1
clothes_sum = 0
for cloth in clothes.copy():
    clothes_sum += cloth
    clothes.popleft()
    if clothes_sum == rack_capacity and clothes:
        n_racks += 1
        clothes_sum = 0
    elif clothes_sum > rack_capacity:
        n_racks += 1
        clothes_sum = cloth

print(n_racks)



