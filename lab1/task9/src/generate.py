import random

n = random.randint(1, 1000)
a = ''.join(random.choice('01') for _ in range(n))
b = ''.join(random.choice('01') for _ in range(n))

with open('../txtf/input.txt', 'w') as f:
    f.write(a + ' ' + b)