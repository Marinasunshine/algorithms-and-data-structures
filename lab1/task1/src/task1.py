f = open('../txtf/input.txt')
n = int(f.readline())
a = list(map(int, f.readline().split()))
f.close()

if not 1 <= n <= 10**3:
    with open('../txtf/output.txt', 'w') as f:
        f.write('Число не входит в диапазон')
    exit()

for element in a:
    if abs(element) > 10 ** 9:
        with open('../txtf/output.txt', 'w') as f:
            f.write('Число превосходит допустимое значение')
        exit()

for i in range(1, n):
    cur_el = a[i]
    j = i - 1
    while j >= 0 and a[j] > cur_el:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = cur_el

f = open('../txtf/output.txt', 'w')
f.write(' '.join(map(str, a)))
f.close()

