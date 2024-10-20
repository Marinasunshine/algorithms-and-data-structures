import random

a = [str(random.randint(-10**9, 10**9)) for i in range(random.randint(1000, 10 ** 3))]

with open('../txtf/input.txt', 'w') as f:
    f.write(f"{len(a)}\n")
    f.write(' '.join(a))
