import random

def read_data(p, num):
    with open(p) as f:
        if num == 1 or num == 2:
            n = int(f.readline())
            arr = list(map(int, f.readline().split()))
            return n, arr
        if num == 3:
            S, n = map(int, f.readline().split())
            packets = [tuple(map(int, line.strip().split())) for line in f.readlines()]
            return S, n, packets
        if num == 6:
            n = int(f.readline())
            operations = [line.strip() for line in f.readlines()]
            return n, operations
        if num == 0:
            arr = list(map(int, f.readline().split()))
            return arr


def write_data(res, p):
    with open(p, "w", encoding='utf-8') as file:
        if isinstance(res, list):
            file.write(' '.join(map(str, res)))
        elif isinstance(res, str):
            file.write(res)
        else:
            file.write(str(res))

def write_data_3_6(res, p):
    with open(p, "w") as file:
        if isinstance(res, list):
            file.write('\n'.join(map(str, res)))

def generations(case, n, S, inp):
    if case == "heap":
        a = [random.randint(1, 2 * 10 ** 9) for i in range(n)]
        is_heap = random.choice([True, False])
        if is_heap:
            for i in range(n // 2):
                left = 2 * i + 1
                right = 2 * i + 2
                if left < n and a[i] > a[left]:
                    a[i], a[left] = a[left], a[i]
                if right < n and a[i] > a[right]:
                    a[i], a[right] = a[right], a[i]
        else:
            random.shuffle(a)
        with open(inp, "w") as file:
            file.write(str(n) + '\n')
            file.write(' '.join(map(str, a)) + '\n')
        return n, a
    elif case == "tree":
        parents = [-1] * n
        root = random.randint(0, n - 1)
        parents[root] = -1
        for i in range(n):
            if i != root:
                parent_candidates = [j for j in range(n) if j != i and parents[j] == -1]
                if parent_candidates:
                    parents[i] = random.choice(parent_candidates)
                else:
                    break
        with open(inp, "w") as file:
            file.write(f"{n}\n")
            file.write(' '.join(map(str, parents)) + '\n')
        return parents
    elif case == "packets":
        packets = [(random.randint(0, 10 ** 6), random.randint(0, 10 ** 3)) for i in range(n)]
        packets.sort(key=lambda x: x[0])
        with open(inp, "w") as file:
            file.write(f"{S} {n}\n")
            for Ai, Pi in packets:
                file.write(f"{Ai} {Pi}\n")
        return S, n, packets
    elif case == "queue":
        with open(inp, "w") as f:
            f.write(f"{n}\n")
            for i in range(n):
                operation_type = random.choice(["A", "X", "D"])
                if operation_type == "A":
                    op = f"A {random.randint(1, 1000)}"
                elif operation_type == "X":
                    op = "X"
                elif operation_type == "D":
                    x = random.randint(1, i + 1)
                    current_value = random.randint(1, 1000)
                    new_value = random.randint(-1000, current_value - 1)
                    op = f"D {x} {new_value}"
                f.write(f"{op}\n")


