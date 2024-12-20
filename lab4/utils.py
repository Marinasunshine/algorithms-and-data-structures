import random

def read_data(p, num):
    with open(p) as f:
        if num == 1:
            n = int(f.readline())
            operations = [line.strip() for line in f.readlines() if line.strip()]
            return n, operations
        if num == 4:
            line = f.readline()
            return line
        if num == 5:
            n = int(f.readline())
            operations = [line.strip().split() for line in f.readlines() if line.strip()]
            return n, operations
        if num == 7:
            n = int(f.readline())
            arr = list(map(int, f.readline().split()))
            m = int(f.readline())
            return n, arr, m
        if num == 8:
            n = int(f.readline())
            data = f.readline().strip().split()
            return n, data

def write_data(res, p):
    with open(p, "w") as file:
        if isinstance(res, list):
            file.write('\n'.join(map(str, res)))
        else:
            file.write(str(res))

def write_data_7(res, p):
    with open(p, "w") as file:
        if isinstance(res, list):
            file.write(' '.join(map(str, res)))

def generations(case, n, k, inp):
    if case == "stack":
        commands = []
        stack_size = 0
        for i in range(n):
            if stack_size == 0:
                number = random.randint(-10 ** 9, 10 ** 9)
                commands.append(f"+ {number}")
                stack_size += 1
            else:
                if random.choice([True, False]):
                    number = random.randint(-10 ** 9, 10 ** 9)
                    commands.append(f"+ {number}")
                    stack_size += 1
                else:
                    commands.append("-")
                    stack_size -= 1
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            for command in commands:
                file.write(command + "\n")
        return commands
    elif case == "brackets":
        brackets = "[]{}()"
        others = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,;.:!? "
        chars = [random.choice(brackets + others) for i in range(n)]
        for i in range(n):
            pos = random.randint(0, n - 1)
            if chars[pos] in brackets:
                chars[pos] = random.choice(brackets.replace(chars[pos], ""))
            else:
                chars[pos] = random.choice(brackets)
        with open(inp, "w") as file:
            file.write(''.join(chars) + "\n")
        return ''.join(chars)
    elif case == "stack_max":
        commands = []
        current_stack = []
        for i in range(n):
            command_type = random.choices(["push", "pop", "max"], weights=[2, 1, 1])[0]
            if command_type == "push":
                value = random.randint(0, 10 ** 5)
                commands.append(f"push {value}")
                current_stack.append(value)
            elif command_type == "pop" and current_stack:
                commands.append("pop")
                current_stack.pop()
            elif command_type == "max" and current_stack:
                commands.append("max")
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            file.write("\n".join(commands) + "\n")
        return commands
    if case == "moving_max":
        array = [random.randint(0, 10 ** 5) for i in range(n)]
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            file.write(" ".join(map(str, array)) + "\n")
            file.write(f"{k}\n")
        return n, array, k
    if case == "postfix":
        operators = ["+", "-", "*"]
        expression = []
        stack_size = 0
        for i in range(n):
            if stack_size < 2:
                expression.append(str(random.randint(0, 9)))
                stack_size += 1
            else:
                if random.choice([True, False]):
                    expression.append(str(random.randint(0, 9)))
                    stack_size += 1
                else:
                    expression.append(random.choice(operators))
                    stack_size -= 1
        while stack_size > 1:
            expression.append(random.choice(operators))
            stack_size -= 1
        with open(inp, "w") as file:
            file.write(f"{len(expression)}\n")
            file.write(" ".join(expression) + "\n")
        return len(expression), expression
