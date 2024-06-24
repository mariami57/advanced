word = input()

char_dict = {}

for char in word:
    char_dict[char] = char_dict.get(char, 0)+1

for char, times in sorted(char_dict.items()):  # (("a", 1), ("b", 3))
    print(f"{char}: {times} time/s")

# word = input()
#
#
# for symbol in sorted(set(word)):
#     print(f"{symbol}: {word.count(symbol)} time/s")