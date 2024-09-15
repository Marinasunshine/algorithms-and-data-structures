import psutil
process = psutil.Process()
f = open('input.txt')
n = int(f.readline())
f.close()

f = open('output.txt', 'w')
f0, f1 = 0, 1
if 0 <= n <= 1:
    f.write(str(n))
if 2 <= n <= 10**7:
    for i in range(2, n + 1):
        f0, f1 = f1, (f0 + f1) % 10
    f.write(str(f1))
else:
    print('Число не подходит под ограничения')

f.close()
print(process.memory_info().rss / 2**20, 'Мб')