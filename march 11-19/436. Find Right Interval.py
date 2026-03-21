import bisect

# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique. 
# -> we can't sort bc we have to return in order (past), nope, we can, just keep track of og ids.
# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. 
# Note that i may equal j.
# -> can be overlapped by the border and pick the lowest start[j] possible

# Return an array of right interval indices for each interval i. 
# If no right interval exists for interval i, then put -1 at index i.

'''
Since you need to find the smallest start >= end for each interval, that's a classic binary search problem.
Approach:

Store all (start, original_index) pairs in a sorted structure
For each interval's end, binary search for the smallest start >= end
If found, record that index; else -1
'''

# def rightInterval(intervals):
#     n = len(intervals)
#     res = [-1]*n
    
#     # sort by start time and retain the orginal indices of each interval
#     starts = sorted([(intervals[i][0], i) for i in range(n)])
#     for i in range(n):
#         idx = bisect.bisect_left(starts, (intervals[i][1],))
#         res[i] = starts[idx][1] if idx < n else -1
#     return res


def rightInterval(intervals):
    n = len(intervals)
    res = [-1]*n

    new_array = sorted([(intervals[i][0], i) for i in range(n)])
    # find leftmost start[i] >= end[j (=i-1)]
    for i in range(n):
        idx = bisect.bisect_left(new_array[0], intervals[i][1])
        if idx < n:
            res[i] = new_array[idx][1]
    return res

#  O(nlogn) time, O(n) space