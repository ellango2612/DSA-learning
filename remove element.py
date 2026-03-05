# Remove Element: 3:02-15
# Given an int array nums and int val, remove all occurences of val in nums in-place. Order might be changed. Return num of eles not equal to val.
# consider nums of eles in nums that are not val k, to get accepted, must: 
# 1. change nums so that first k eles contains eles not equal to val; 2. return k

def removeElement(self, nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = float('inf')
        else:
            count += 1
    nums.sort()
    return count

# nums = [2,2,inf, inf], val = 3, count = 2
# Time: O(logn), Space: O(1)

# great job! March 5 2026, try to do the 2nd way (O(n) time complexity) soon