import random


def read_data(p, num):
    with open(p) as f:
        if num == 1:
            n = int(f.readline())
            arr = list(map(int, f.readline().split()))
            return n, arr
        if num == 5:
            arr = list(map(int, f.readline().split(',')))
            return arr
        if num == 2:
            n = int(f.readline())
            return n
        if num == 9:
            n = int(f.readline())
            points = [(int(i.split()[0]), int(i.split()[1])) for i in f.readlines()]
            return n, points
        if num == 3:
            n, k = map(int, f.readline().split())
            arr = list(map(int, f.readline().split()))
            return n, k, arr
        if num == 0:
            arr = list(map(int, f.readline().split()))
            return arr

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
            file.write(','.join(map(str, a)) + '\n')
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

