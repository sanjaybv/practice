def quicksort(array, low, high):
    if high - low <= 0:
        return

    pivot = array[low]
    high_start = low + 1
    for current in xrange(high_start, high+1):
        if array[current] < pivot:
            array[current], array[high_start] = \
                    array[high_start], array[current]
            high_start += 1
    array[low], array[high_start-1] = array[high_start-1], array[low]

    quicksort(array, low, high_start - 2)
    quicksort(array, high_start, high)

array = [5, 6237, 334573, 93, 45, 02, 1, 8, 4, 7]
quicksort(array, 0, 9)
print array
