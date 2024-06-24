from collections import deque

chocolate = deque(int(x)for x in input().split(", "))
milk = deque(int(x)for x in input().split(", "))

milkshakes = 0
while chocolate and milk and milkshakes < 5:
    if milk[0] <= 0 and chocolate[-1] <= 0:
        milk.popleft()
        chocolate.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue

    if milk[0] == chocolate[-1]:
        milk.popleft()
        chocolate.pop()
        milkshakes += 1
    else:
        milk.append(milk.popleft())
        chocolate[-1] -= 5


if milkshakes < 5:
    print("Not enough milkshakes.")
elif milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")

print(f"Chocolate: {', '.join(str(x) for x in chocolate) if chocolate else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk) if milk else 'empty'}")
