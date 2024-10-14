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

def bubble_sort(a, reverse):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (a[j] > a[j + 1] and not reverse) or (a[j] < a[j + 1] and reverse):
                a[j], a[j + 1] = a[j + 1], a[j]

bubble_sort(a,  False)
f = open('../txtf/output.txt', 'w')
f.write(' '.join(map(str, a)))
f.close()