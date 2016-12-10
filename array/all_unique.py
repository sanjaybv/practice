def all_unique(string):
    seen_char = set()

    for char in string:
        if char in seen_char:
            return False
        seen_char.add(char)

    return True

print all_unique('Hello')
print all_unique('World')
print all_unique('')
