numbers = set(int(n) for n in input().split())
target_num = int(input())
diff_list = []
for number in numbers:
    diff = target_num - number
    if (diff in numbers and diff not in diff_list) and number != diff:
        print(f"{number} + {diff} = {target_num}")
        diff_list.append(diff)
        diff_list.append(number)