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

    if max_sum < 0:
        return [max(a)]

    return a[start:end + 1]


