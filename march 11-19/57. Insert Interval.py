# given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] and intervals is sorted in ascending order by starti. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and 
# intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# thoughts: either the new interval overlap with 1 or 2 intervals or it doesn't.
# if it does, merge it, if not, add it

def addInterval(intervals, newInterval):
    if not intervals:
        return [newInterval]
    res = []
    # before
    for interval in intervals:
        if newInterval is None:
            res.append(interval)
        elif interval[1] < newInterval[0]:
            res.append(interval)
        elif interval[0] > newInterval[1]:
            res.append(newInterval)
            res.append(interval)
            newInterval = None
        else:
            newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
    if newInterval is not None:
        res.append(newInterval)
    return res

    # after

    # merging
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5] , res = [[1,5]]
# Output: [[1,5],[6,9]]

# O(n) time and place