def add_songs(*songs):
    titles = {}
    for name, lyrics in songs:
        titles[name] = titles.get(name, []) + lyrics

    result = ""
    for song, words in titles.items():
        result += f"- {song}\n"
        if words:
            result += "\n".join(words)
            result += "\n"

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
