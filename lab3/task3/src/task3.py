def scarecrow_sort(n, k, matr):
    groups = [[] for i in range(k)]
    for i in range(n):
        groups[i % k].append(matr[i])
    for group in groups:
        group.sort()
    sorted_matr = [groups[i % k][i // k] for i in range(n)]
    return "ДА" if sorted_matr == sorted(matr) else "НЕТ"
