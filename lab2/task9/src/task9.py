def matrix_mult(n, X, Y):
    Z = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k] * Y[k][j]

    return Z