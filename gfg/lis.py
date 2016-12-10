# Longest Increasing Subsequence

import sys

def lis(nums):
    if len(nums) == 0:
        return score

    lis_array = [1]*len(nums)

    for i in xrange(len(nums)):
        for j in xrange(i):
            if nums[j] < nums[i] and lis_array[i] < lis_array[j] + 1:
                lis_array[i] = lis_array[j] + 1

    return max(lis_array)

for _ in range(int(raw_input())):
    raw_input()
    nums = map(int, raw_input().strip().split())
    print lis(nums)
