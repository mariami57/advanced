from collections import deque

some_string = deque(x for x in input().split())
colours = "red", "blue", "yellow",
secondary_colours = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

found_colours = []

while some_string:
    first_part = some_string.popleft()
    second_part = some_string.pop() if some_string else ""
    if first_part + second_part in colours or first_part + second_part in secondary_colours:
        found_colours.append(first_part + second_part)
    elif second_part + first_part in colours or second_part + first_part in secondary_colours:
        found_colours.append(second_part + first_part)
    else:
        for el in (first_part[:-1], second_part[:-1]):
            if el:
                some_string.insert(len(some_string)// 2, el)

for colour in set(secondary_colours.keys()).intersection(found_colours):
    if not secondary_colours[colour].issubset(found_colours):
        found_colours.remove(colour)
print(found_colours)