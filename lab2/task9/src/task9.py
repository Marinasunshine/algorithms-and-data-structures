def matrix_mult(n, X, Y):
    Z = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k] * Y[k][j]

    return Z


def check_and_write(input_f, output_f):
    with open(input_f) as f:
        n = int(f.readline())

        A = []
        for i in range(n):
            A.append(list(map(int, f.readline().split())))

        B = []
        for i in range(n):
            B.append(list(map(int, f.readline().split())))

    C = matrix_mult(n, A, B)
    with open(output_f, 'w') as f:
        for r in C:
            f.write(' '.join(map(str, r)) + '\n')

check_and_write('../txtf/input.txt', '../txtf/output.txt')