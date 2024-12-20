def is_match(pattern, s):
    m = len(pattern)
    n = len(s)
    match = [[False] * (n + 1) for i in range(m + 1)]
    match[0][0] = True

    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            match[i][0] = match[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == '*':
                match[i][j] = match[i - 1][j] or match[i][j - 1]
            elif pattern[i - 1] == '?' or pattern[i - 1] == s[j - 1]:
                match[i][j] = match[i - 1][j - 1]

    if match[m][n]:
        return "YES"
    else:
        return "NO"