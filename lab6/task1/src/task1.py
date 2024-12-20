def set_operations(commands):
    s = set()
    result = []

    for command in commands:
        action = command[0]
        value = int(command[1])

        if action == 'A':
            s.add(value)
        elif action == 'D':
            s.discard(value)
        elif action == '?':
            result.append("Y" if value in s else "N")

    return result