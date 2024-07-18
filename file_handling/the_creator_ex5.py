import os
import re

words_path = os.path.join("ex_5", "words.txt")

with open(words_path) as word_file:
    searched_words_as_text = word_file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]


input_path = os.path.join("ex_5", "input.txt")

with open(input_path) as input_file:
    input_text = input_file.read().lower()


words_count = {}

for word in searched_words:
    pattern = re.compile(rf"\b{word}\b")
    result = re.findall(pattern, input_text)
    words_count[word] = result.count(word)

sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

output_path = os.path.join("ex_5", "output.txt")
with open(output_path, "a") as file:
    for w, c in sorted_words_count:
        file.write(f"{w} - {c}\n")







