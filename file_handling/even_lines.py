import os

symbols = ("-", ",", ".", "!", "?")

path = os.path.join("p01_even_lines", "text.txt")

with open(path, "r") as read_file:
    my_list = read_file.readlines()

for row in range(0, len(my_list), 2):
    for s in symbols:
        my_list[row] = my_list[row].replace(s, "@")

    print(*my_list[row].split()[::-1])