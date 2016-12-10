def string_replace(string):
    string = list(string)
    read_index = write_index = len(string) - 1
    
    while string[read_index] == ' ':
        read_index -= 1

    while read_index >= 0:
        char = string[read_index]
        if char == ' ':
            string[write_index-2:write_index+1] = list(r'%20')
            write_index -= 3
        else:
            string[write_index] = char
            write_index -= 1
        read_index -= 1

    return ''.join(string)

print string_replace('asdf asdfmvr asdf sdc      ')
print string_replace('asdf')

