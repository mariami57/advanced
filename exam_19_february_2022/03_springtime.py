def start_spring(**objects):
    collections = {}
    for obj, type in objects.items():
        collections[type] = collections.get(type, []) + [obj]
    sorted_collections = sorted(collections.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for k, v in sorted_collections:
        result += f"{k}:\n"
        for value in sorted(v):
            result += f"-{value}\n"
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


