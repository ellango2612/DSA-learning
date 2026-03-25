# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
# starting from 0 and 1. 
# Given n, calculate F(n)


def fib(n):
    if n == 0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
# REMEMBER: O(2^n) time and O(n) space because WE WILL HAVE SAVED N+1 SPACES (every time calling n, n-1, n-2, etc.) UNTIL RETURNING
#  -> space complexity = depth of the call stack