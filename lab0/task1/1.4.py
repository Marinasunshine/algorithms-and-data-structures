f = open('input.txt')
a, b = map(int, f.readline().split())
f.close()

f = open('output.txt', 'w')
if (-10**9 <= a <= 10**9) and (-10**9 <= b <= 10**9):
    f.write(str(a + b**2))
else:
    print('Числа не подходят под условие')
f.close()
