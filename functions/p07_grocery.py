def grocery_store(**products):
    sorted_products = sorted(products.items(), key=lambda kvp: (-kvp[1], - len(kvp[0]), kvp[0]))

    return "\n".join(f'{p}: {q}' for p, q in sorted_products)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

