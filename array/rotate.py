def rotate(matrix):
    size = len(matrix)
    for i in xrange(0, size/2):
        for j in xrange(i, size-i-1):
            top = matrix[i][j]
            matrix[i][j] = matrix[size-j-1][i]
            matrix[size-j-1][i] = matrix[size-i-1][size-j-1]
            matrix[size-i-1][size-j-1] = matrix[j][size-i-1]
            matrix[j][size-i-1] = top

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
rotate(a)
print a

b = [[]]
rotate(b)
print b

c = [[1, 2], [3, -4]]
rotate(c)
print c
