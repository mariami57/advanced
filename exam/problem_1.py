from collections import deque

money = [int(x) for x in input().split()]
food = deque(int(x) for x in input().split())
counter_food = 0
while food and money:
    current_money = money.pop()
    current_food = food.popleft()
    if current_food < current_money:
        diff = current_money - current_food
        if money:
            next_money = money.pop()
            money.append(next_money+diff)
        else:
            money.append(diff)
        counter_food += 1
    elif current_food == current_money:
        counter_food += 1

if not counter_food:
    print("Henry remained hungry. He will try next weekend again.")

elif counter_food == 1:
    print(f"Henry ate: {counter_food} food.")

elif 1 < counter_food < 4:
    print(f"Henry ate: {counter_food} foods.")

if counter_food >= 4:
    print(f"Gluttony of the day! Henry ate {counter_food} foods.")

