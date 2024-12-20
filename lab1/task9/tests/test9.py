import time
import tracemalloc

start = time.perf_counter()
tracemalloc.start()

f = open('../txtf/input.txt')
a, b = f.readline().split()
f.close()

n = len(a)

if not 1 <= n <= 10**3:
    with open('../txtf/output.txt', 'w') as f:
        f.write('Число не входит в диапазон')
    exit()

carry = 0
c = ['0'] * (n + 1)

for i in range(n - 1, -1, -1):
    sum_bit = int(a[i]) + int(b[i]) + carry
    c[i + 1] = str(sum_bit % 2)
    carry = sum_bit // 2

c[0] = str(carry)

f = open('../txtf/output.txt', 'w')
f.write(''.join(c).lstrip('0') or '0')
f.close()

print(time.perf_counter() - start, 'c')
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, 'Mb')