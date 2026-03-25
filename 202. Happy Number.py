# Write an algorithm to determine if a number n is happy.

# thoughts with hints for the first time: detecting cycle. if a number is gotten back to twice, there is a cycle and we return false

def happyNumber(n):
    visited = set()

    total = 0
    while n not in visited:
        visited.add(total)
        for i in range(len(str(n))):
            total += (int(str(n)[i]))**2
        if total == 1:
            return True
        n = total
            

    return False

# O(logn) time and O(logn) space
def happyNumber(n):

    def nextNum(num):
        res = 0
        while num > 0:
            res += (num%10)**2
            num //= 10
        return res
    
    seen = set()
    def happy(n, seen):
        m = nextNum(n)
        if m == 1:
            return True
        if m not in seen:
            seen.add(m)
            happy(m, seen)
        elif m in seen:
            return False
        
    happy(n, seen)
# 19: m = 82, seen = (82,...)