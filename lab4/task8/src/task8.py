def postfix(data):
    stack = []

    for element in data:
        if element.isdigit() or (element[0] == '-' and len(element) > 1):
            stack.append(int(element))
        else:
            b = stack.pop()
            a = stack.pop()
            if element == '+':
                stack.append(a + b)
            elif element == '-':
                stack.append(a - b)
            elif element == '*':
                stack.append(a * b)

    return stack[0]