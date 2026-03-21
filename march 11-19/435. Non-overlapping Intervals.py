# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. 
# For example, [1, 2] and [2, 3] are non-overlapping.

# thoughts: we need to remove the interval that is bigger??

# 1. Sort by end time
# Track end of last kept interval
# If current interval doesn't overlap → keep it, update end
# If overlaps → increment removal counter
# 2. Then loop thru intervals, if see overlapping ones, remove the one with bigger end time

def removeInterval(intervals):
    intervals.sort(key=lambda x:x[1]) #sort by end time
    end = intervals[0][1]
    count = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    return count

# O(nlogn) time and O(1) space (only var count)