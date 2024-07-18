file = open("numbers.txt", "r")

total_amount = 0

for line in file.readlines():
    total_amount += int(line.strip())

print(total_amount)