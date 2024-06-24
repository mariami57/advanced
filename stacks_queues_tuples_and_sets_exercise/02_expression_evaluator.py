from math import floor
from collections import deque

expression = deque(input().split())
index = 0

while index < len(expression):
    symbol = expression[index]
    if symbol == "+":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
    elif symbol == "-":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif symbol == "*":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif symbol == "/":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))

    if symbol in "+-*/":
        del expression[1]
        index = 1

    index += 1

print(floor(int(expression[0])))
















# import math
# from functools import reduce
#
# expression = input().split()
# index = 0
#
# calculations = {
#     "*": lambda i: reduce(lambda a,b: a*b, map(int, expression[:i])),
#     "/": lambda i: reduce(lambda a,b: a/b, map(int, expression[:i])),
#     "+": lambda i: reduce(lambda a,b: a+b, map(int, expression[:i])),
#     "-": lambda i: reduce(lambda a,b: a-b, map(int, expression[:i]))
# }
#
# while index < len(expression):
#     element = expression[index]
#
#     if element in "*/+-":
#         expression[0] = calculations[element](index)
#         [expression.pop(1) for _ in range(index)]
#         index = 1
#     index += 1
#
# print(math.floor(int(expression[0])))
#
