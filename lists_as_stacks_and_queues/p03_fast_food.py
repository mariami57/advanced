from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))


while orders:
    removed_order = orders.popleft()
    if removed_order <= food_quantity:
        food_quantity -= removed_order

    else:
        print(f"Orders left:", removed_order, *orders)
        break

else:
    print("Orders complete")


