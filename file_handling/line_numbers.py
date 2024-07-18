from string import punctuation

with open("p01_even_lines/text.txt", "r") as text_file:
    text = text_file.readlines()


output_file = open("p02_line_numbers/output.txt", "w")

for row in range(len(text)):
    letters,marks = 0, 0

    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {row+1}: {text[row].strip()}({letters})({marks})\n")

