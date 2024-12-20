import random
import string

def read_data(p, num):
    with open(p) as f:
        if num == 5:
            votes = [line.strip().split() for line in f.readlines()]
            return votes
        if num == 1 or num == 4 or num == 2:
            n = int(f.readline())
            operations = [line.strip().split() for line in f.readlines()]
            return n, operations

def write_data(res, p):
    with open(p, "w") as file:
        for item in res:
            file.write(f'{item[0]} {item[1]}\n')

def write_data_2(res, p):
    with open(p, "w") as f:
        f.write("\n".join(res) + "\n")

def generations(case, n, inp):
    if case == "set":
        operations = []
        for i in range(n):
            op_type = random.choice(["A", "D", "?"])
            x = random.randint(-10 ** 18, 10 ** 18)
            operations.append(f"{op_type} {x}")
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            file.write('\n'.join(operations) + '\n')
        return operations
    if case == "command":
        keys = ["".join(random.choices(string.ascii_lowercase, k=random.randint(1, 20))) for i in range(n)]
        operations = []
        for i in range(n):
            op_type = random.choice(["put", "get", "prev", "next", "delete"])
            key = random.choice(keys)
            if op_type == "put":
                value = "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 20)))
                operations.append(f"{op_type} {key} {value}")
            else:
                operations.append(f"{op_type} {key}")
        with open(inp, "w") as file:
            file.write(f"{n}\n" + "\n".join(operations) + "\n")
        return operations
    if case == "phone":
        numbers = [str(random.randint(1000000, 9999999)) for i in range(n)]
        names = ["Mom", "Dad", "Police", "Tom", "Obama", "Cat"]
        operations = []
        for i in range(n):
            op = random.choice(['add', 'del', 'find'])
            number = random.choice(numbers)
            if op == 'add':
                name = random.choice(names)
                operations.append(f"{op} {number} {name}")
            else:
                operations.append(f"{op} {number}")
        with open(inp, "w") as file:
            file.write(f"{n}\n" + "\n".join(operations) + "\n")
        return operations
    if case == "votes":
        candidates = ["McCain", "Obama", "ivanov", "petr", "tourist", "bur"]
        s = []
        for i in range(n):
            candidate = random.choice(candidates)
            votes = random.randint(1, n)
            s.append(f"{candidate} {votes}")
        with open(inp, "w") as file:
            file.write("\n".join(s) + "\n")
        return s
