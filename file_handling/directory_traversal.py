import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            extensions[extension] = extensions.get(extension, []) + [filename]

        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


directory = input()
extensions = {}
result = []
try:
    save_extensions(directory)
except FileNotFoundError:
    print("Directory not found")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for ex, file in extensions:
    result.append(f".{ex}")
    for f in sorted(file):
        result.append(f"- - - {f}")

with open("p04_directory_traversal/result.txt", "w") as result_file:
    result_file.write('\n'.join(result))
    