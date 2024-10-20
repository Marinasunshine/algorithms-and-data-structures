def binary_search(a, target):
    l = 0
    r = len(a) - 1

    while l <= r:
        mid = (l + r) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

def check_and_write(input_f, output_f):
    with open(input_f) as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))
        k = int(f.readline())
        b = list(map(int, f.readline().split()))

    if not 1 <= n <= 10 ** 5:
        with open(output_f, 'w') as f:
            f.write('Число не входит в диапазон')
        return

    for element in a:
        if not (1 <= element <= 10 ** 9):
            with open(output_f, 'w') as f:
                f.write('Число превосходит допустимое значение')
            return

    if not 1 <= k <= 10 ** 5:
        with open(output_f, 'w') as f:
            f.write('Число  не входит в диапазон')
        return

    for element in b:
        if not (1 <= element <= 10 ** 9):
            with open(output_f, 'w') as f:
                f.write('Число в массиве b превосходит допустимое значение')
            return


    res = [binary_search(a, x) for x in b]
    with open(output_f, 'w') as f:
        f.write(' '.join(map(str, res)))


check_and_write('../txtf/input.txt', '../txtf/output.txt')