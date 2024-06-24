from collections import deque

time = deque(int(x) for x in input().split())
n_tasks = [int(x) for x in input().split()]

ducks_counts = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while time and n_tasks:
    current_time = time.popleft()
    current_task = n_tasks.pop()
    result = current_task * current_time
    if 0 < result <= 60:
        ducks_counts["Darth Vader Ducky"] += 1
    elif 60 < result <= 120:
        ducks_counts["Thor Ducky"] += 1
    elif 120 < result <= 180:
        ducks_counts["Big Blue Rubber Ducky"] += 1
    elif 180 < result <= 240:
        ducks_counts["Small Yellow Rubber Ducky"] += 1
    else:
        current_task -= 2
        n_tasks.append(current_task)
        time.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

print(f"Darth Vader Ducky: {ducks_counts['Darth Vader Ducky']}")
print(f"Thor Ducky: {ducks_counts['Thor Ducky']}")
print(f"Big Blue Rubber Ducky: {ducks_counts['Big Blue Rubber Ducky']}")
print(f"Small Yellow Rubber Ducky: {ducks_counts['Small Yellow Rubber Ducky']}")

