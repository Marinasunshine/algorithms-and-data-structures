f = open('../txtf/input.txt')
a = list(map(int, f.readline().split()))
v = int(f.readline())
f.close()

if not 0 <= len(a) <= 10**3:
    with open('../txtf/output.txt', 'w') as f:
        f.write('Число не входит в диапазон')
    exit()

for el in a:
    if -10**3 > el:
        with open('../txtf/output.txt', 'w') as f:
            f.write('Число превосходит допустимое значение')
        exit()

if 10**3 < v:
    with open('../txtf/output.txt', 'w') as f:
        f.write('Число превосходит допустимое значение')
    exit()

indexes = []
for i in range(len(a)):
    if a[i] == v:
        indexes.append(i)

f = open('../txtf/output.txt', 'w')
if len(indexes) > 1:
    f.write(f"{len(indexes)}: " + ', '.join(map(str, indexes)))
elif len(indexes) == 1:
    f.write(str(indexes[0]))
else:
    f.write("-1")
f.close()

