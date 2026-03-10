# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]], res = [[1,6],]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# thoughts: we can pass thru the array once and compare 2 intervals at a time. the overlapping intervals have traits:
# start_i  <= end_j and start_j <= end_i -> merge: min(start_i, start_j), max(end_i, end_j)

def merge_intervals(intervals):
    # we sort first so that we only need to compare each interval with the one before it 
    intervals.sort()
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            new_start = min(intervals[i][0], res[-1][0])
            new_end = max(intervals[i][1], res[-1][1])
            res[-1] = [new_start, new_end]
        else:
            res.append(intervals[i])
    return res

# one pass, but we sorted: O(nlogn), space: O(n) (res)