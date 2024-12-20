def find_max(n, arr, m):
    dequeue = []
    result = []

    for i in range(n):
        if dequeue and dequeue[0] < i - m + 1:
            dequeue.pop(0)
        while dequeue and arr[dequeue[-1]] < arr[i]:
            dequeue.pop()
        dequeue.append(i)
        if i >= m - 1:
            result.append(arr[dequeue[0]])

    return result