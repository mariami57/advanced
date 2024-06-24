def age_assignment(*names, **kvp):
    result = []
    for key, value in kvp.items():
        for name in names:
            if name[0] == key:
                result.append(f"{name} is {value} years old.")
                break
    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))