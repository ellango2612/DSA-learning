# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

#  thought process: compate num with every int^2 where int ranges from 1 -> num//2, and use binary search in that range

def perfectSquare(num):
    lo = 1
    hi = max(1, num//2)
    while lo <= hi:
        mid = lo+(hi-lo)//2
        if mid*mid == num:
            return True
        elif mid*mid < num:
            lo = mid+1
        else:
            hi = mid -1
    return False

# trace thru an example: num = 16 => true; lo = 1, hi = 8, mid = 4 -> True
# Time: O(logn), space: O(1)