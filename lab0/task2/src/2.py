f = open('../txtf/input2.txt')
n = int(f.readline())
f.close()
f = open('../txtf/output2.txt', 'w')
f0, f1 = 0, 1
if 0 <= n <= 1:
    f.write(str(n))
elif 2 <= n <= 45:
    for i in range(2, n + 1):
        f0, f1 = f1, f0 + f1
    f.write(str(f1))
else:
    print('Число не подходит под ограничения')

f.close()




