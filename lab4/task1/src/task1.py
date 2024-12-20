def stacks(commands):
    stack = []
    result = []

    for command in commands:
        if command[0] == '+':
            stack.append(int(command.split()[1]))
        elif command == '-':
            result.append(stack.pop())

    return result