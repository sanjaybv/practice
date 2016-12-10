#code

def partition(nums, low, high):
    if high == low:
        return low

    fh = low+1
    c = low+1
    while c <= high:
        if nums[c] > nums[low]:
            nums[fh], nums[c] = nums[c], nums[fh]
            fh += 1
        c += 1
    fh -= 1
    nums[fh], nums[low] = nums[low], nums[fh]
    return fh

def print_nums(nums):
    for num in nums:
        print num, 
    print

def k_largest(nums, k):
    low = 0
    high = len(nums) - 1
    
    while True:
        
        pivot = partition(nums, low, high)
        print pivot
        if pivot == k-1:
            lar = nums[:k]
            lar.sort()
            lar.reverse()
            print_nums(lar)
            return
        elif pivot > k:
            high = pivot - 1
        else:
            low = pivot + 1

k = int(raw_input())
k_largest(map(int, raw_input().strip().split()), k)
