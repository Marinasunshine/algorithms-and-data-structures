def max_sub(a):
    max_sum = curr_sum = a[0]
    start = end = 0

    for i in range(1, len(a)):
        if curr_sum + a[i] < a[i]:
            curr_sum = a[i]
            start = i
        else:
            curr_sum += a[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i

    return a[start:end + 1]

def check_and_write(input_f, output_f):
    with open(input_f) as f:
        n = int(f.readline().strip())
        a = list(map(int, f.readline().strip().split()))

    if not 1 <= n <= 2 * 10**4:
        with open(output_f, 'w') as f:
            f.write('Число не входит в диапазон')
        return

    for element in a:
        if abs(element) > 10**9:
            with open(output_f, 'w') as f:
                f.write('Число превосходит допустимое значение')
            return

    maxi = max_sub(a)
    with open(output_f, 'w') as f:
        f.write(' '.join(map(str, maxi)))

check_and_write('../txtf/input.txt', '../txtf/output.txt')