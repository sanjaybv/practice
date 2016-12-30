def is_set(number, index):
    return bool(1<<index & number)

def subsets(elements):
    all_subsets = []
    for number in xrange(2 ** len(elements)):
        subset = []
        for i in xrange(len(elements)):
            if is_set(number, i):
                subset.append(elements[i])
        all_subsets.append(subset)
    return all_subsets

print subsets(['a', 'b', 'c'])
