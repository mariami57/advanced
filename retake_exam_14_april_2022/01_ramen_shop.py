from collections import deque

ramen = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while ramen and customers:
    current_ramen = ramen.pop()
    current_customer = customers.popleft()
    if current_customer == current_ramen:
        continue
    elif current_customer > current_ramen:
        current_customer -= current_ramen
        customers.appendleft(current_customer)
    elif current_customer < current_ramen:
        current_ramen -= current_customer
        ramen.append(current_ramen)

if not customers:
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join(str(r) for r in ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(c) for c in customers)}")