import time
import tracemalloc

start = time.perf_counter()
tracemalloc.start()

f = open('../txtf/input.txt')
n = int(f.readline())
a = list(map(int, f.readline().split()))
f.close()

if not 1 <= n <= 10**3:
    with open('../txtf/output.txt', 'w') as f:
        f.write('Число не входит в допустимый диапазон')
    exit()

for element in a:
    if abs(element) > 10 ** 9:
        with open('../txtf/output.txt', 'w') as f:
            f.write('Число превосходит допустимое значение')
        exit()

for i in range(1, n):
    curr_el = a[i]
    j = i - 1
    while j >= 0 and a[j] < curr_el:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = curr_el

f = open('../txtf/output.txt', 'w')
f.write(' '.join(map(str, a)))
f.close()

print(time.perf_counter() - start, 'c')
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, 'Mb')