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