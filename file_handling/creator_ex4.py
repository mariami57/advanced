import os

path = os.path.join("advanced", "file_handling", "my_new_file.txt")

with open(path, "a") as file:
    file.write("Some content")

try:
    os.remove(path)

except FileNotFoundError:
    print("File already deleted!")


if os.path.exists(path):
    os.remove(path)
else:
    print("File already deleted!")