def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice = []
    naughty = []
    for command in args:
        num, category = command.split("-")
        num = int(num)
        exists = False
        name = None

        for kid_num, kid_name in santa_list:
            if num == kid_num and exists:
                exists = False
                break
            if num == kid_num:
                name = kid_name
                exists = True

        if exists:
            santa_list.remove((num, name))
            if category == "Nice":
                nice.append(name)
            elif category == "Naughty":
                naughty.append(name)

        for nm, cat in kwargs.items():
            exists = False
            n = None

            for kid_num, kid_name in santa_list:
                if nm == kid_name and exists:
                    exists = False
                    break
                if nm == kid_name:
                    n = kid_num
                    exists = True

            if exists:
                santa_list.remove((n, nm))
                if category == "Nice":
                    nice.append(nm)
                elif category == "Naughty":
                    naughty.append(nm)

    return nice, naughty


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
