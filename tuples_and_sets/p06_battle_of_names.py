n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n+1):
    name = input()
    sum_current_name = 0

    for char in name:
        sum_current_name += ord(char)
    score_name = sum_current_name // i
    if score_name % 2 == 0:
        even_set.add(score_name)
    else:
        odd_set.add(score_name)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_odd_set == sum_even_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_odd_set > sum_even_set:
    print(*odd_set.difference(even_set), sep=", ")
elif sum_odd_set < sum_even_set:
    print(*even_set.symmetric_difference(odd_set), sep=", ")

