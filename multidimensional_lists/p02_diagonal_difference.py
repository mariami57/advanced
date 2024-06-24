n = int(input())
first = 0
second = 0
for index in range(n):
    data = [int(x) for x in input().split()]
    first += data[index]
    second += data[n-index-1]

print(abs(first - second))
