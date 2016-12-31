from numpy import random

class BitSet(object):
    def __init__(self, N):
        self._bytes = bytearray(N/8 + 1)

    def set(self, index):
        byte_index = index / 8;
        offset = index % 8;
        self._bytes[byte_index] = 1<<offset | self._bytes[byte_index]

    def get(self, index):
        byte_index = index / 8;
        offset = index % 8;
        return 1<<offset & self._bytes[byte_index]

def get_dup(numbers):
    bit_set = BitSet(32000)
    for num in numbers:
        if bit_set.get(num):
            print num
        else:
            bit_set.set(num)

numbers = random.randint(0, 32000, size=1000)
get_dup(numbers)
