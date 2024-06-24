def forecast(*weather_info):
    locations = {}
    for location, weather in weather_info:
        if location not in locations:
            locations[location] = weather

    sorted_locations = {sorted(locations.items(), key=lambda x: x[1])}
    sunny = ""
    cloudy = ""
    rainy = ""

    for l in sorted_locations:
        if l[1] == "Sunny":
            sunny += l
        elif l[1] == "Cloudy":
            cloudy += l
        elif l[1] == "Rainy":
            rainy += l
    return sorted_locations


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))