from collections import deque


def fill_the_box(height, length, width, *args):
    space = height * length * width
    cubes = deque(args)
    while cubes[0] != "Finish":
        current_cube = cubes.popleft()
        space -= current_cube
        if space <= 0:
            break

    if space > 0:
        return f"There is free space in the box. You could put {space} more cubes."
    else:
        return f"No more free space! You have {sum(c for c in cubes if c != 'Finish') + abs(space)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
