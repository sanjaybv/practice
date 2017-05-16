def next_big(array):
    stack = []
    B = [0] * len(array)

    for i, elem in enumerate(array):
        while stack and elem > array[stack[-1]]:
            B[stack.pop()] = i - stack[-1]
        stack.append(i)

    return B

A = [7, 4, 3, 6, 9]
print next_big(A)
