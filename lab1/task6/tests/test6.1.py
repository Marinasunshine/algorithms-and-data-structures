f = open('../txtf/output.txt')
a = list(map(int, f.readline().split()))

def is_sorted(a, reverse):
   return all(a[i] >= a[i + 1] if reverse else a[i] <= a[i + 1] for i in range(len(a) - 1))

print(is_sorted(a, False))