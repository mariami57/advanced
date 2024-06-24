def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = [num for num in kwargs["odd"] if num % 2 != 0]
    if "even" in kwargs:
        kwargs["even"] = [num for num in kwargs["even"] if num % 2 == 0]

    return dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

