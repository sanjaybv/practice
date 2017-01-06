def count_ones(number):
    if not number:
        return 0
    return count_ones(number >> 1) + (1 & number)

def next_num(number):
    num_ones = count_ones(number)
    while number < (2 ** 32) - 1:
        number += 1
        if num_ones == count_ones(number):
            return number

print next_num(5)
