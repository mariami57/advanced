n = int(input())
elements_list = [input().split() for _ in range(n)]
elements = set()
for element in elements_list:
    for el in element:
        elements.add(el)
print(*elements, sep="\n")