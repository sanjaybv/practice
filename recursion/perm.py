def permutation(elements):
    if len(elements) <= 1:
        return [elements]
    
    perms = []
    for elem in elements:
        elements_copy = list(elements)
        elements_copy.remove(elem)
        for perm in permutation(elements_copy):
            t = [elem]
            t.extend(perm)
            perms.append(t)
    
    return perms

p =  permutation(list('abcde'))
print len(p)
#for x in p:
 #   print x
