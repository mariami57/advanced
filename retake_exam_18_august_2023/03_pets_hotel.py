from collections import deque


def accommodate_new_pets(room, max_kg, *pets):
    animals_deque = deque(pets)
    pet_dict = {}
    result = deque()
    while room > 0 and animals_deque:
        for pet_info in pets:
            animals_deque.popleft()
            if max_kg >= pet_info[1]:
                pet_dict[pet_info[0]] = pet_dict.get(pet_info[0], 0) + 1
                room -= 1
                if room <= 0 or not animals_deque:
                    break

    sorted_pets = sorted(pet_dict.items(), key=lambda x: x[0])

    result.append(f"Accommodated pets:")
    for p, n in sorted_pets:
        result.append(f"{p}: {n}")

    if not animals_deque:
        result.appendleft(f"All pets are accommodated! Available capacity: {room}.")
        string_for_print = ""
        for row in result:
            string_for_print += f"{row}\n"
        return string_for_print
    else:
        result.appendleft(f"You did not manage to accommodate all pets!")
        string_for_print = ""
        for row in result:
            string_for_print += f"{row}\n"
        return string_for_print


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


