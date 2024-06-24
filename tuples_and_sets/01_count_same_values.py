numbers = tuple(input().split())
unique_num = []
for num in numbers:
    if num not in unique_num:
        unique_num.append(num)
        count = numbers.count(num)
        print(f"{float(num)} - {count} times")
