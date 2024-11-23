import random

def partition(a, l, r):
    """"Разбиение для обычной сортировки"""
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j = j + 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    """"Обычная быстрая сортировка"""
    if l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m = partition(a, l, r)
        randomized_quick_sort(a, l, m - 1)
        randomized_quick_sort(a, m + 1, r)



def randomized_quick_sort_best(a, l, r):
    """Улучшенная версия быстрой сортировки"""
    if l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition_best(a, l, r)
        randomized_quick_sort_best(a, l, m1 - 1)
        randomized_quick_sort_best(a, m2 + 1, r)

def partition_best(a, l, r):
    """Трёхстороннее разделение"""
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            a[m1], a[i] = a[i], a[m1]
            if m1 != m2:
                m2 += 1
                a[m2], a[m1] = a[m1], a[m2]
        elif a[i] == x:
            m2 += 1
            a[m2], a[i] = a[i], a[m2]
    a[l], a[m1] = a[m1], a[l]
    return m1, m2