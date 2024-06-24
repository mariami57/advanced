from collections import deque

expression = deque(input())
balanced_expression = expression.copy()
pop_flag = False
for symbol in expression:
    if pop_flag:
        pop_flag = False
        continue
    if symbol == "(" and ")" in balanced_expression:
        balanced_expression.popleft()
        if balanced_expression[-1] == ")":
            balanced_expression.pop()
        else:
            balanced_expression.popleft()
            pop_flag = True
    elif symbol == "{" and "}" in balanced_expression:
        balanced_expression.popleft()
        if balanced_expression[-1] == "}":
            balanced_expression.pop()
        else:
            balanced_expression.popleft()
            pop_flag = True
    elif symbol == "[" and "]" in balanced_expression:
        balanced_expression.popleft()
        if balanced_expression[-1] == "]":
            balanced_expression.pop()
        else:
            balanced_expression.popleft()
            pop_flag = True


if balanced_expression:
    print("NO")
else:
    print("YES")