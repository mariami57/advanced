expression = list(input())
parentheses = []
for index in range(len(expression)):

    if expression[index] == "(":
        parentheses.append(index)
    elif expression[index] == ")":
        start_index = parentheses.pop()
        end_index = index+1

        print("".join(expression[start_index:end_index]))
