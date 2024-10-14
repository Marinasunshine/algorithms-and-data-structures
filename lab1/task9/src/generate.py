import random

a = ''.join(random.choice('01') for _ in range(random.randint(1, 1000)))
b = ''.join(random.choice('01') for _ in range(random.randint(1, 1000)))

with open('../txtf/input.txt', 'w') as f:
    f.write(a + ' ' + b)