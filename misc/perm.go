def print_perm(char_set, str):
    print char_set
    if not len(char_set):
        print str
    for char in char_set:
        str += char
        new_char_set = char_set.copy()
        new_char_set.remove(char)
        print_perm(new_char_set, str)

print_perm(set(['a', 'b', 'c']), '')
