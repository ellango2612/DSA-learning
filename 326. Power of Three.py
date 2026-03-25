# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

def powerofthree(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n%3 != 0:
        return False
    return powerofthree(n//3)

# O(logn) time and space

# doing recursively:

