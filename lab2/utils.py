import random

def read_data(p):
    with open(p) as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines() if line.strip()]

    if len(lines) == 1 and len(lines[0]) == 1:
        return lines[0][0]
    if len(lines[0]) > 1 and len(lines) == 1 and "," not in lines[0]:
        return list(map(int, lines[0]))

    if len(lines) == 2 and len(lines[0]) == 1:
        n = lines[0][0]
        arr = lines[1]
        return n, arr
    elif len(lines) == 4:
        n = lines[0][0]
        a = lines[1]
        k = lines[2][0]
        b = lines[3]
        return n, a, k, b
    elif len(lines[0]) == 1 and len(lines) > 2:
        n = lines[0][0]
        A = [lines[i] for i in range(1, n + 1)]
        B = [lines[i] for i in range(n + 1, 2 * n + 1)]
        return n, A, B


def write_data(res, p):
    with open(p, "w") as file:
        if isinstance(res, list):
            if isinstance(res[0], list):
                for row in res:
                    file.write(' '.join(map(str, row)) + '\n')
            else:
                file.write(' '.join(map(str, res)) + '\n')
        else:
            file.write(str(res))

def generations(case, n, k, inp):
    if case == "bin":
        a = [random.randint(1, 50) for i in range(n)]
        b = []
        for i in range(k):
            if random.choice([True, False]):
                b.append(random.choice(a))
            else:
                b.append(random.randint(1, 100))
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            file.write(' '.join(map(str, a)) + '\n')
            file.write(f"{k}\n")
            file.write(' '.join(map(str, b)) + '\n')
        return n, a, k, b
    if case == "matrix":
        A = [[random.randint(0, 100) for i in range(n)] for i in range(n)]
        B = [[random.randint(0, 100) for i in range(n)] for i in range(n)]
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            for row in A:
                file.write(' '.join(map(str, row)) + '\n')
            for row in B:
                file.write(' '.join(map(str, row)) + '\n')
    else:
        if case == "random":
            a = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        elif case == "reversed":
            a = list(range(n, 0, -1))
        with open(inp, "w") as file:
            file.write(str(n) + '\n')
            file.write(' '.join(map(str, a)) + '\n')
        return n, a
