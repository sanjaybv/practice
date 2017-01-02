# Longest Increasing Subsequence

def lis(array, index, cache):
    if index >= len(array):
        return None
    if cache.get(index):
        return cache[index]

    max_length = 0
    for i in xrange(index+1, len(array)):
        if array[i] > array[index]:
            cur_length = lis(array, i, cache)
            if cur_length > max_length:
                max_length = cur_length

    cache[index] = max_length + 1
    
    return cache[index]

print lis([1, 3, 4, 2], 0, {})
