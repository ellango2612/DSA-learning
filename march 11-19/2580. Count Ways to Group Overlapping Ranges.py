# given a 2D integer array ranges where ranges[i] = [starti, endi] (both inclusive) are contained in the ith range.

# split ranges into two (possibly empty) groups such that:

# Each range belongs to exactly one group.
# Any two overlapping ranges must belong to the same group.
# Two ranges are said to be overlapping if there exists at least one integer that is present in both ranges.

# For example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges.
# Return the total number of ways to split ranges into two groups. Since the answer may be very large, return it modulo 109 + 7.

# -> prob summary: we can merge all intervals that are overlapping in 1 group since they HAVE TO be in 1 group
# there will be k merged intervals correlating to 2^k groups. since this number might be too big, return 2^k mod (10^9+7)

def countWays(ranges):
    # first, merge all intervals into res
    ranges.sort()
    res = [ranges[0]]
    for i in range(1, len(ranges)):
        if ranges[i][0] <= res[-1][1]:
            new_start = min(ranges[i][0], res[-1][0])
            new_end = max(ranges[i][1], res[-1][1])
            res[-1] = [new_start, new_end]
        else:
            res.append(ranges[i])
    
    # count ways
    ways = len(res)
    return (2**ways) % (10**9 +7)

# O(nlogn) time and O(n) space