def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res

def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def check_and_write(input_f, output_f):
    with open(input_f) as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))

    if not 1 <= n <= 2 * 10**4:
        with open(output_f, 'w') as f:
            f.write('Число не входит в диапазон')
        return

    for element in a:
        if abs(element) > 10**9:
            with open(output_f, 'w') as f:
                f.write('Число превосходит допустимое значение')
            return

    sorted_a = merge_sort(a)
    with open(output_f, 'w') as f:
        f.write(' '.join(map(str, sorted_a)))

check_and_write('../txtf/input.txt', '../txtf/output.txt')