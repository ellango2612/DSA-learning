#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

'''
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''
 
def containsDuplicate(nums):
    hash_map = {}
    for index, value in nums.enumerate():
        if value in hash_map:
            return True
        hash_map[value] = index
    return false
    
# Time: O(n) - worst case - hash collisions: O(n^2)
# Space: O(n)
             
