def lcs(a, b, i, j, matrix):
    if i >= len(a) or j >= len(b):
        return 0
    if matrix[i][j] != -1:
        return matrix[i][j]
    if a[i] == b[j]:
        result = 1 + lcs(a, b, i+1, j+1, matrix)
    else:
        result = max(
                lcs(a, b, i+1, j, matrix),
                lcs(a, b, i, j+1, matrix)
                )
    matrix[i][j] = result
    return result

matrix = [[-1]*6 for _ in xrange(6)]
print lcs('abcdef', 'aabcde', 0, 0, matrix)
for l in matrix:
    print l
