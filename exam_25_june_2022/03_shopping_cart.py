def shopping_cart(*args):
    products = {
    "Soup": [],
    "Pizza": [],
    "Dessert": []

    }
    if "Stop" in args:
        stop_index = args.index("Stop")
        left_part = args[:stop_index]
        for meal, product in left_part:
            if meal == "Soup":
                if product not in products["Soup"] and len(products["Soup"]) < 3:
                    products["Soup"].append(product)
            elif meal == "Pizza":
                if product not in products["Pizza"] and len(products["Pizza"]) < 4:
                    products["Pizza"].append(product)
            elif meal == "Dessert":
                if product not in products["Dessert"] and len(products["Dessert"]) < 2:
                    products["Dessert"].append(product)
    else:
        for meal, product in args:
            if meal == "Soup":
                if product not in products["Soup"] and len(products["Soup"]) < 3:
                    products["Soup"].append(product)
            elif meal == "Pizza":
                if product not in products["Pizza"] and len(products["Pizza"]) < 4:
                    products["Pizza"].append(product)
            elif meal == "Dessert":
                if product not in products["Dessert"] and len(products["Dessert"]) < 2:
                    products["Dessert"].append(product)

    sorted_products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    if any (products.values()):
        for m, p in sorted_products:
            result += f"{m}:\n"
            if p:
                for item in sorted(p):
                    result += f" - {item}\n"
    else:
        result += "No products in the cart!"

    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

