'''
You are given an integer array heights where heights[i] represents the height of the 
ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6], i = 2, j = 7, maxArea = 36

Output: 36
'''

# have a local max and keep updating it

def maxArea(self, heights):
    maxArea = 0
    i, j = 0, len(heights) - 1
    while i < j:
        maxArea = max(maxArea, (j-i)*min(heights[i], heights[j]))
        if heights[i]<= heights[j]:
                i += 1
        else:
                j -= 1
    return maxArea