def print_bin(num):
    if not 0 <= num <= 1:
        return "ERROR"

    bin_digits = []
    while num > 0 and len(bin_digits) < 32:
        num = num * 2
        if num >= 1:
            bin_digits.append('1')
            num -= 1
        else:
            bin_digits.append('0')

    if num == 0:
        return ''.join(bin_digits)
    return "ERROR", num, ''.join(bin_digits)

print print_bin(0.1)
