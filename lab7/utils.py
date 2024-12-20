import random
import string

def read_data(p, num):
    with open(p) as f:
        if num == 6:
            n = int(f.readline())
            arr = list(map(int, f.readline().split()))
            return n, arr
        if num == 7:
            pattern = f.readline().strip()
            s = f.readline().strip()
            return pattern, s
        if num == 4:
            n = int(f.readline())
            a = list(map(int, f.readline().split()))
            m = int(f.readline())
            b = list(map(int, f.readline().split()))
            return n, a, m, b
        if num == 1:
            n, k = map(int, f.readline().split())
            arr = list(map(int, f.readline().split()))
            return n, k, arr

def write_data(res, p):
    with open(p, "w", encoding='utf-8') as file:
        if isinstance(res, list):
            file.write(' '.join(map(str, res)))
        elif isinstance(res, str):
            file.write(res)
        elif isinstance(res, tuple):
            file.write(f"{res[0]}" + '\n')
            file.write(f"{' '.join(map(str, res[1]))}")
        else:
            file.write(str(res))

def generations(case, n, k, inp):
    if case == "coins":
        money = n
        coins = [random.randint(1, 1000) for i in range(k)]
        with open(inp, "w") as file:
            file.write(f"{money} {k}\n")
            file.write(' '.join(map(str, coins)) + '\n')
        return money, k, coins
    if case == "sequence":
        a = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        b = [random.randint(-10 ** 9, 10 ** 9) for i in range(k)]
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            file.write(' '.join(map(str, a)) + '\n')
            file.write(f"{k}\n")
            file.write(' '.join(map(str, b)) + '\n')
        return n, a, k, b
    if case == "max":
        a = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            file.write(' '.join(map(str, a)) + '\n')
        return n, a
    elif case == "pattern":
        pattern = ''.join(random.choice(string.ascii_lowercase + '*?') for i in range(n))
        string_s = ''.join(random.choice(string.ascii_lowercase) for i in range(k))
        with open(inp, 'w') as f:
            f.write(pattern + '\n')
            f.write(string_s + '\n')
        return pattern, string_s
