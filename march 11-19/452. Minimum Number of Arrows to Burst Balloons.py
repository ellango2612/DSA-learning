# essentially, this prob is asking for the number of groups of overlapping intervals.
# thoughts: group all overlapping intervals together then return the number of groups
# actually, better thought and the actual way to solve this prob: sort the array by end time, then, start count at 1 cuz we always need at least 1 arrow
# then, we have 2 cases: if overlapping: pass, if not, add 1 to count. in both cases we update the new end.

def minArrows(points):
    if not points:
        return 0
    count = 1
    points.sort(key=lambda x: x[1])
    end = points[0][1]
    for i in range(1, len(points)):
        if points[i][0] <= end:
            pass
        else:
            count+=1
            end = points[i][1]
        
    return count

# O(nlogn) time and O(1) constant space

