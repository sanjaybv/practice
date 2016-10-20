def print_perm(char_set, string):
    if not len(char_set):
        print string
    for char in char_set:
        new_char_set = char_set.copy()
        new_char_set.remove(char)
        print_perm(new_char_set, string+char)

print_perm(set(['a', 'b', 'c']), '')
