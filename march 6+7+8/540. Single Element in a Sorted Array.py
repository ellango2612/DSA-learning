# given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# return the single element that appears only once.
# your solution must run in O(log n) time and O(1) space.

# first off, from the prompt of "sorted array" and "running in O(logn) time and O(1) space", we can see we need a solution 
# with binary search and no extra space consuming data structures (hash map, etc.)
# notice that the index of all the duplicated ints before the single ele starts at an even index, whereas the pairs after start at an
# odd. 
# we can use bit manipulation: XOR: flipping bit, so if nums[mid] == nums[mid^1], then if this is true, the single ele 
# is after, but if not it's before. it will be mid when loop ends.

def singleElement(nums):
    lo = 0
    hi = len(nums)-1
    while lo < hi:
        mid = lo+(hi-lo)//2
        if nums[mid]==nums[mid^1]:
            lo = mid+1
        else:
            hi = mid
    return nums[lo]
# e.g: Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2 -> lo = 0, hi = 8, mid = 4 (False bc 3!=4) -> hi = 3, mid = 1 (true bc 1=1), lo = 2, hi = 3, mid = 2
# (false bc 2!=3) -> hi = 1

# 2nd example: nums = [3,3,7,7,10,11,11] lo = 0, hi = 6, mid = 3 (True bc 7=7) -> lo = 4, mid = 5 (false bc 11!=10), 
# hi = 4
# (false bc 2!=3) -> hi = 1




