'''
Given an int array nums and an integer val, remove all occurrences of val in nums in-place. The order doesn't matter. Output = number of elements left in nums
'''

# Idea: 
# 

def removeElement(self, nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            nums.replace(nums[i], '')
    return len(nums)