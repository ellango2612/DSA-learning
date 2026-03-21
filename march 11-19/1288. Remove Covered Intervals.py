# remove all intervals that are covered by another interval in the list intervals

# thoughts: remove all intervals nested inside another (FULLY overlapped)

def removeIntervals(intervals):
    count = len(intervals)
    intervals.sort(key=lambda x: (x[0], -x[1])) # sort by beginning, but if not end descending
    maxEnd = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][1] <= maxEnd:
            count -= 1
        else:
            maxEnd = intervals[i][1]
    return count
    

# Input: intervals = [[1,4],[2,8],[3,6]], n = 3, firstInt = [2,8]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

# O(nlogn) time and O(1) space