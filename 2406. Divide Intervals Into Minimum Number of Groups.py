# given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
# divide the intervals into one or more groups such that each interval is in exactly one group, 
# and no two intervals that are in the same group intersect each other.
# Return the minimum number of groups you need to make.

# Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

# thoughts: need to divide the list of intervals into as few groups overlapping as possible. maybe sort first? then do greedy: put overlapping ones in another group
# -> do the same thing with that new group??

def divideIntervals(intervals):
    events = []
    for interval in intervals:
        events.append((interval[0], 1))
        events.append((interval[1], -1))
    events.sort(key=lambda x:(x[0], -x[1])) # touching = overlapping since intervals are inclusive
    max_count = 0
    current_count = 0
    for start, end in events:
        current_count += end
        max_count = max(max_count, current_count)
    return max_count



# O(nlogn) time and O(n) space
    

'''
point 1: [1,5]                    → 1 interval
point 2: [1,5],[2,4]              → 2 intervals, end = 4
point 3: [1,5],[2,4],[3,7]        → 3 intervals ← peak
point 6: [1,5],[3,7]              → 3 intervals ← peak
point 7: [3,7],[5,8]              → 2 intervals
point 8: [6,8]  

events = [(1,1), (2,1), (3,1), (4,-1), (5,-1), (6,1), (7,-1), (8,-1)]
current_count = 0
max_count = 3
'''