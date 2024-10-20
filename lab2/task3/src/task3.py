def merge(l, r):
    res = []
    i = j = inversions = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            inversions += len(l) - i
            j += 1

    res.extend(l[i:])
    res.extend(r[j:])

    return res, inversions


def merge_sort(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2
    l, l_inversions = merge_sort(a[:mid])
    r, r_inversions = merge_sort(a[mid:])
    merged, split_inv = merge(l, r)

    return merged, l_inversions + r_inversions + split_inv


def check_and_write(input_f, output_f):
    with open(input_f) as f1:
        n = int(f1.readline())
        a = list(map(int, f1.readline().split()))

    if not 1 <= n <= 10 ** 5:
        with open(output_f, 'w') as f:
            f.write('Число не входит в диапазон')
        return

    for element in a:
        if abs(element) > 10 ** 9:
            with open(output_f, 'w') as f:
                f.write('Число превосходит допустимое значение')
            return

    merged, inversions = merge_sort(a)

    with open(output_f, 'w') as f:
        f.write(str(inversions))


check_and_write('../txtf/input.txt', '../txtf/output.txt')