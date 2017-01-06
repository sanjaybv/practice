def comparator(a, b):
    if a > b:
        return -1
    if a < b:
        return 1
    return 0

print sorted([1, 7, 3, 2, 5, 8, 4, 8, 1, 7], cmp=comparator)
