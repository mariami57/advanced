from collections import deque
price_per_bullet = int(input())
size_of_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())
n_bullets_used = 0
total_bullets = 0
new_barrel = size_of_barrel
while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()
    n_bullets_used += 1
    total_bullets += 1

    if bullet > lock:
        locks.appendleft(lock)
        print("Ping!")
    else:
        print("Bang!")

    if n_bullets_used == size_of_barrel:
        if not bullets:
            break
        else:
            print("Reloading!")
            new_barrel -= 1
            n_bullets_used = 0

bullets_cost = total_bullets * price_per_bullet
money_earned = intelligence_value - bullets_cost
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

