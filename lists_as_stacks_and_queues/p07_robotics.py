from collections import deque
from datetime import timedelta, datetime


robots = {}


for r in input().split(";"):
    name, time = r.split("-")
    robots[name] = [int(time), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()
product = input()

while product != "End":
    products.append(product)
    product = input()

while products:
    factory_time += timedelta(0, 1)
    current_product = products.popleft()

    free_robots = []
    for names, values in robots.items():
        if robots[names][1] != 0:
            robots[names][1] -= 1
        if robots[names][1] == 0:
            free_robots.append([names, values])

    if not free_robots:
        products.append(current_product)
        continue
    name, time = free_robots[0]
    robots[name][1] = time[0]

    print(f"{name} - {current_product} [{factory_time.strftime('%H:%M:%S')}]")

