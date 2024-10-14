f = open('../txtf/input.txt')
a, b = f.readline().split()
f.close()

bin_sum = bin(int(a, 2) + int(b, 2))[2:]

f = open('../txtf/output.txt', 'w')
f.write(bin_sum)
f.close()