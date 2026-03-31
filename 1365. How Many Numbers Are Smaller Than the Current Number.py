# Implement count sort

# step 1: count the occurences of each ele in nums

# 2: count number of smaller eles than nums: it's the number of smaller eles of the previous item + number of occurrences of the previous item

# 3: transform that into res: formatted: counts of smaller eles accordingly to how eles appear in nums

def countSmaller(nums):
    occurrences = [0]*101
    for i in nums:
        occurrences[i] += 1
    smaller_array = [0]*101
    for i in range(1, len(occurrences)):
        smaller_array[i] = occurrences[i-1]+smaller_array[i-1]
    
    res = [0]*len(nums)
    for i in range(len(nums)):
        res[i] = smaller_array[nums[i]]
    return res

# O(n+k) time, O(k) space where k = 102 -> O(n) time and O(1) space by using count sort!!
