def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for cheese, quantities in sorted_dict:
        result += cheese + "\n"
        for quantity in sorted(quantities, reverse=True):
            result += f"{quantity}\n"

    return result

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

