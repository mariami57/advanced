def cookbook(*cooking_info):
    arrangement = {}
    dishes = {}
    for meal, cuisine, ingredients in cooking_info:
        if cuisine not in arrangement:
            arrangement[cuisine] = [meal]
        else:
            arrangement[cuisine].append(meal)
        if cuisine not in dishes and meal not in dishes:
            dishes[cuisine, meal] = ingredients
        else:
            dishes[cuisine, meal] += ingredients

    arrangement_sorted = sorted(arrangement.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for c, dish in arrangement_sorted:
        result += f"{c} cuisine contains {len(dish)} recipes:\n"
        if isinstance(dish, list):
            for d in sorted(dish):
                result += f"  * {d} -> Ingredients: "
                for key, values in dishes.items():
                    if d in key:
                        result += f"{', '.join(values)}\n"
        else:
            result += f"{dish}\n"
            for key, values in dishes.items():
                if dish in key:
                    result += f"{', '.join(values)}\n"

    return result



print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))



