# 374
# This question reads like a direct implementation of binary search

def guessNumber(n):
    lo = 1
    hi = n
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if guess(mid) == -1:
            hi = mid-1
        elif guess(mid) == 1:
            lo = mid+1
        else:
            return mid
        
# tracing an example: Input: n = 10, pick = 6 -> output: 6, lo = 1, hi = 10, mid = 5, lo = 6 -> mid = 8 -> hi = 7
# -> mid = 6 -> return 6 -> yay!!!!

