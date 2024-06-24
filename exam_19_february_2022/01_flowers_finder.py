from collections import deque

flowers = {
    "rose": [],
    "tulip": [],
    "lotus": [],
    "daffodil": []

}

vowels = deque(input().split())
consonants = input().split()
found_flowers = ""
flag = False
while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    list_of_letters = [current_vowel, current_consonant]
    for letter in list_of_letters:
        if letter in "rose":
            flowers["rose"].append(letter)
            if len("rose") == len(flowers["rose"]):
                found_flowers = "rose"
                flag = True
                break
        if letter in "tulip":
            flowers["tulip"].append(letter)
            if len("tulip") == len(flowers["tulip"]):
                found_flowers = "tulip"
                break
        if letter in "lotus":
            flowers["lotus"].append(letter)
            if len("lotus") == len(flowers["lotus"]):
                found_flowers = "lotus"
                flag = True
                break
        if letter in "daffodil":
            flowers["daffodil"].append(letter)
            if letter == "d" and flowers["daffodil"].count("d") == 1 or letter == "f" and flowers["daffodil"].count("f") == 1:
                flowers["daffodil"].append(letter)
            if len("daffodil") == len(flowers["daffodil"]):
                found_flowers = "daffodil"
                flag = True
                break
    if flag:
        break

if found_flowers:
    print(f"Word found: {found_flowers}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
