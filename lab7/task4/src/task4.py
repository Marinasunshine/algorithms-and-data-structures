def length(a, b):
    len1 = len(a)
    len2 = len(b)
    prev_row = [0] * (len2 + 1)
    curr_row = [0] * (len2 + 1)

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if a[i - 1] == b[j - 1]:
                curr_row[j] = prev_row[j - 1] + 1
            else:
                curr_row[j] = max(prev_row[j], curr_row[j - 1])
        prev_row, curr_row = curr_row, [0] * (len2 + 1)

    return prev_row[len2]