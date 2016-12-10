def is_perm(string_1, string_2):
    if len(string_1) != len(string_2):
        return False

    freq_char = [0] * 256

    for char in string_1:
        freq_char[ord(char)] += 1

    for char in string_2:
        freq_char[ord(char)] -= 1
        if freq_char[ord(char)] < 0:
            return False

    return True

print is_perm('hello', 'world')
print is_perm('hello', 'lolhe')
print is_perm('hello', 'worasdld')
print is_perm('', '')
