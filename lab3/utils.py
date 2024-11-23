import random


def read_data(p):
    with open(p) as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines() if line.strip()]

    if len(lines) == 1 and len(lines[0]) == 1:
        return lines[0][0]
    if "," in lines[0] and len(lines[0]) > 1:
        return list(map(int, lines[0]))
    if len(lines) == 1 and len(lines[0]) > 1:
        return list(map(int, lines[0]))

    if len(lines[0]) == 1 and len(lines) > 1:
        n = lines[0][0]
        if len(lines[1]) == 2:
            points = [tuple(map(int, line)) for line in lines[1:]]
            return n, points
        else:
            arr = lines[1]
            return n, arr
    elif len(lines[0]) == 2:
        n, k = lines[0]
        arr = lines[1]
        return n, k, arr

def write_data(res, p):
    with open(p, "w", encoding='utf-8') as file:
        if isinstance(res, list):
            file.write(' '.join(map(str, res)))
        elif isinstance(res, str):
            file.write(res)
        elif isinstance(res, float):
            file.write(f"{res:.4f}")
        else:
            file.write(str(res))

def generations(case, n, k, inp):
    if case == "matreshka":
        a = [random.randint(1, 50) for i in range(n)]
        with open(inp, "w") as file:
            file.write(f"{n} {k}\n")
            file.write(' '.join(map(str, a)) + '\n')
        return n, k, a
    elif case == "h":
        a = [random.randint(0, 1000) for i in range(n)]
        with open(inp, "w") as file:
            file.write(' '.join(map(str, a)) + '\n')
        return a
    elif case == "points":
        points = [(random.randint(-10 ** 9, 10 ** 9), random.randint(-10 ** 9, 10 ** 9)) for i in range(n)]
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            for x, y in points:
                file.write(f"{x} {y}\n")
        return n, points
    else:
        if case == "random":
            a = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        elif case == "reversed":
            a = list(range(n, 0, -1))
        with open(inp, "w") as file:
            file.write(str(n) + '\n')
            file.write(' '.join(map(str, a)) + '\n')
        return n, a

def generation_random_n(inp):
    n = random.randint(1, 10**6)
    with open(inp, "w") as file:
        file.write(str(n))

