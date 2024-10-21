def check_and_write(input_f, output_f, sort_func):
    with open(input_f) as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))

    if not 1 <= n <= 2 * 10 ** 4:
        with open(output_f, 'w') as f:
            f.write('Число не входит в диапазон')
        return

    for element in a:
        if abs(element) > 10 ** 9:
            with open(output_f, 'w') as f:
                f.write('Число превосходит допустимое значение')
            return

    sorted_a = sort_func(a)
    with open(output_f, 'w') as f:
        f.write(' '.join(map(str, sorted_a)))