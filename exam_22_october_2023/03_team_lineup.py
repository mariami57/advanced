def team_lineup(*players):
    countries_dict = {}
    for pair in players:
        countries_dict[pair[1]] = countries_dict.get(pair[1], []) + [pair[0]]

    sorted_countries_dict = sorted(countries_dict.items(), key=lambda x: (- len(x[1]), x[0]))
    result = ""
    for key, values in sorted_countries_dict:
        result += f"{key}:\n"
        for value in values:
            result += f"  -{value}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


