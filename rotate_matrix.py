import numpy as np

def rotate(matrix):
    N = matrix.shape[0]

    # transpose
    for i in range(N):
        for j in range(i, N):
            (matrix[i, j], matrix[j, i]) = (matrix[j, i], matrix[i, j])

    print
    print matrix
    print

    # flip horizontally
    for i in range(N/2):
        temp = matrix[:, i].copy()
        matrix[:, i] = matrix[:, N-i-1]
        matrix[:, N-i-1] = temp

matrix = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])

print matrix
rotate(matrix)
print matrix
