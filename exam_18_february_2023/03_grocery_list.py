def shop_from_grocery_list(budget, grocery_list, *products_info):
    grocery_list = set(grocery_list)
    purchased_products = set()
    for product_name, price in products_info:
        if budget < price:
            break
        if product_name not in purchased_products and budget >= price and product_name in grocery_list:
            purchased_products.add(product_name)
            budget -= price
            if budget <= 0:
                budget = 0

    if purchased_products == grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        diff = list(grocery_list.difference(purchased_products))
        result = ""
        result += "You did not buy all the products. Missing products: "
        for p in diff:
            result += f"{p}." if p == diff[-1] else f"{p}, "
        return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

