# Given an integer n, return true if it is a power of four. Otherwise, return false.

def powerFour(n):
    return n>0 and (n & (n-1) == 0) and 0xAAAAAAAA == 0