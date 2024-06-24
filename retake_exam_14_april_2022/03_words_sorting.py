def words_sorting(*words):
    some_dict = {}
    for word in words:
        sum_of_chars = 0
        for char in word:
            sum_of_chars += ord(char)
        some_dict[word] = sum_of_chars

    values_sum = 0
    for s in some_dict.values():
        values_sum += s
    if values_sum % 2 == 0:
        sorted_dict = sorted(some_dict.items(), key=lambda x: x[0])
    else:
        sorted_dict = sorted(some_dict.items(), key=lambda x: -x[1])

    result = ""
    for key, value in sorted_dict:
        result += f"{key} - {value}\n"

    return result


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

