def merge(a, l, r, l_start, r_end, f):
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    while i < len(l):
        res.append(l[i])
        i += 1

    while j < len(r):
        res.append(r[j])
        j += 1

    a[l_start:r_end + 1] = res
    f.write(f"{l_start + 1} {r_end + 1} {a[l_start]} {a[r_end]}\n")
    return a

def merge_sort(a, l, r, f):
    if l < r:
        mid = (l + r) // 2
        merge_sort(a, l, mid, f)
        merge_sort(a, mid + 1, r, f)
        merge(a, a[l:mid + 1], a[mid + 1:r + 1], l, r, f)
    return a

def check_and_write(input_f, output_f):
    with open(input_f) as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))

    if not (1 <= n <= 10 ** 5):
        with open(output_f, 'w') as f:
            f.write('Число не входит в диапазон')
        return

    for element in a:
        if abs(element) > 10 ** 9:
            with open(output_f, 'w') as f:
                f.write('Число превосходит допустимое значение')
            return

    with open(output_f, 'w') as f:
        merge_sort(a, 0, n - 1, f)
        f.write(' '.join(map(str, a)))


check_and_write('../txtf/input.txt', '../txtf/output.txt')