from collections import deque
food_supplies = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))


peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)

])

list_of_peaks = []
for _ in range(7):
    if not stamina or not food_supplies:
        break
    current_food = food_supplies.pop()
    current_stamina = stamina.popleft()
    result = current_food + current_stamina
    peak_to_climb = peaks.popleft()
    if result >= peak_to_climb[1]:
        list_of_peaks.append(peak_to_climb[0])
    else:
        peaks.appendleft(peak_to_climb)
    if len(list_of_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break


if len(list_of_peaks) < 5:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")


if list_of_peaks:
    print(f"Conquered peaks: ")
    for peak in list_of_peaks:
        print(peak)
