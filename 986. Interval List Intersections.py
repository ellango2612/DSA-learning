#  given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
# Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.

# thoughts: find overlapping parts among these 2 lists -> add it to a res = [] and return
# loop until the end of the larger list => O(n)

def intersection(firstList, secondList):
    res = []
    n, m = len(firstList), len(secondList)
    i, j = 0, 0
    while i<n and j<m:
        lo = max(firstList[i][0], secondList[j][0])
        hi = min(firstList[i][1], secondList[j][1])
        if lo <= hi:
            res.append([lo, hi])
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1
    return res
    
# thought process again: need to end the loop when EITHER i or j is out of bounds -> while i<n and j<m:
# overlapping when max(start) <= min (end), also, only increment the one with MIN(END)

