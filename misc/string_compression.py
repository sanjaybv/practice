def compress(string):
    comp_string = []
    last_char = ''
    last_char_count = 0

    for char in string:
        if last_char == char:
            last_char_count += 1
        else:
            if last_char:
                comp_string.append(last_char)
                comp_string.append(str(last_char_count))
            last_char = char
            last_char_count = 1
    comp_string.append(last_char)
    comp_string.append(str(last_char_count))

    return ''.join(comp_string) if len(string) > len(comp_string) else string

print compress('aaaaaabcd')
