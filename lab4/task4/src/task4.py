def brackets(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for i, element in enumerate(s):
        if element in '([{':
            stack.append((element, i + 1))
        elif element in ')]}':
            if not stack:
                return i + 1
            top, index = stack.pop()
            if top != pairs[element]:
                return i + 1
    if stack:
        return stack[-1][1]

    return "Success"