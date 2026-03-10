# given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

def sumUnique(nums):
    hash_map = {}
    for i in range(len(nums)):
        hash_map[nums[i]] = 1 + hash_map.get((nums[i]),0)
    res = 0
    for item in hash_map:
        if hash_map[item] == 1:
            res+=item
    return res