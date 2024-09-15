f = open('input.txt')
a, b = map(int, f.readline().split())
f.close()

f = open('output.txt', 'w')
f.write(str(a + b**2))
f.close()
