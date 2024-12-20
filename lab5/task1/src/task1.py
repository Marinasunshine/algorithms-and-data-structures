def check_heap(arr):
    n = len(arr)
    for i in range(1, n + 1):
        left = 2 * i
        right = 2 * i + 1
        if left <= n and arr[i - 1] > arr[left - 1]:
            return "NO"
        if right <= n and arr[i - 1] > arr[right - 1]:
            return "NO"
    return "YES"
