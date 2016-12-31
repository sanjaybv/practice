def merge(A, B, size_a):
    a_index = size_a - 1
    b_index = len(B) - 1
    merge_index = size_a + len(B) - 1

    while a_index >= 0 and b_index >= 0:
        if A[a_index] > B[b_index]:
            A[merge_index] = A[a_index]
            a_index -= 1
        else:
            A[merge_index] = B[b_index]
            b_index -= 1
        merge_index -= 1

    while a_index >= 0:
        A[merge_index] = A[a_index]
        merge_index -= 1
        a_index -= 1


    while b_index >= 0:
        A[merge_index] = B[b_index]
        merge_index -= 1
        b_index -= 1

A = [0, 4, 7, 0, 0, 0]
B = [2, 6, 10]
merge(A, B, 3)
print A
