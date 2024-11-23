def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11, A12, A21, A22 = [r[:mid] for r in A[:mid]], [r[mid:] for r in A[:mid]], [r[:mid] for r in A[mid:]], [r[mid:] for r in A[mid:]]
    B11, B12, B21, B22 = [r[:mid] for r in B[:mid]], [r[mid:] for r in B[:mid]], [r[:mid] for r in B[mid:]], [r[mid:] for r in B[mid:]]

    P1 = strassen(A11, sub_matrix(B12, B22))
    P2 = strassen(add_matrix(A11, A12), B22)
    P3 = strassen(add_matrix(A21, A22), B11)
    P4 = strassen(A22, sub_matrix(B21, B11))
    P5 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    P6 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))
    P7 = strassen(sub_matrix(A11, A21), add_matrix(B11, B12))

    C11 = add_matrix(sub_matrix(add_matrix(P5, P4), P2), P6)
    C12 = add_matrix(P1, P2)
    C21 = add_matrix(P3, P4)
    C22 = sub_matrix(sub_matrix(add_matrix(P1, P5), P3), P7)

    C = [[0] * n for i in range(n)]
    for i in range(mid):
        C[i][:mid], C[i][mid:], C[i + mid][:mid], C[i + mid][mid:] = C11[i], C12[i], C21[i], C22[i]

    return C
