# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. 
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# thoughts: to get k complete rows, we need: 1+2+....+k coins = (k+1)k/2 coins at least.
# we are looking for the largest k where (k+1)k/2 <= n
#  we are searching in a range [1,n] where a condition is met -> binary search

def arrangingcoins(n):
    lo = 1
    hi = n
    max_so_far = 0
    while lo <= hi:
        mid = lo+(hi-lo)//2
        if mid*(mid+1)//2 <= n:
            max_so_far=max(max_so_far,mid) 
            lo = mid+1
        else:
            hi = mid-1
    return max_so_far

# Input: n = 8; Output: 3 - trace: lo = 1, hi = 8, max_so_far = 0, mid = 4, max_so_far = 4, lo = 5, mid = 6, hi = 5, mid = 5
# time: O(logn), space: O(1)