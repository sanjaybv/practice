def chunked_palindrome(string, low, high):
    if low > high:
        return 0
    if high == low:
        return 1

    stack_front = []
    stack_back = []

    while high >= low:
        stack_front.append(string[low])
        stack_back.append(string[high])
        low += 1
        high -= 1
        if ''.join(stack_front) == ''.join(reversed(stack_back)):
            return 2 + chunked_palindrome(string, low, high)
    
    return 1

print chunked_palindrome('volvo', 0, 4)
print chunked_palindrome('helloiamhello', 0, 12)
print chunked_palindrome('ghiabcdefhelloadamhelloabcdefghi', 0,
        len('ghiabcdefhelloadamhelloabcdefghi')-1)
