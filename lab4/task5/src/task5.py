def stack_max(commands):
    stack = []
    max_stack = []
    result = []

    for command in commands:
        if command[0] == 'push':
            value = int(command[1])
            stack.append(value)
            if not max_stack or value >= max_stack[-1]:
                max_stack.append(value)
        elif command[0] == 'pop':
            if stack:
                value = stack.pop()
                if value == max_stack[-1]:
                    max_stack.pop()
        elif command[0] == 'max':
            if max_stack:
                result.append(str(max_stack[-1]))

    return result