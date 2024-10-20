import random

n = random.randint(100000, 100000)
letters = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(n))

with open('../txtf/input.txt', 'w') as f:
    f.write(f"{n}\n{letters}")