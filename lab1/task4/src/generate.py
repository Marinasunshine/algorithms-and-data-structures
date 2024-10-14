import random

A = [str(random.randint(-1000, 1000)) for i in range(random.randint(0, 1000))]
V = str(random.randint(-1000, 1000))

with open('../txtf/input.txt', 'w') as f:
    f.write(' '.join(A) + '\n' + V)