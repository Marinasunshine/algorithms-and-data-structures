def longest_lengths(arr):
    n = len(arr)
    lengths = [1] * n
    prev = [-1] * n
    max_len = 1
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j
                if lengths[i] > max_len:
                    max_len = lengths[i]
                    max_index = i

    l = []
    index = max_index
    while index != -1:
        l.append(arr[index])
        index = prev[index]
    l.reverse()

    return max_len, l