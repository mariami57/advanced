def movie_organizer(*movie_info):
    movie_dict = {}
    for name, genre in movie_info:
        if genre not in movie_dict:
            movie_dict[genre] = [name]
        else:
            movie_dict[genre].append(name)

    sorted_movie_dict = sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for type, movie in sorted_movie_dict:
        sorted_movies = sorted(movie)
        result += f"{type} - {len(movie)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"

    return result


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))



