# lets try count sort

def relativeSort(arr1, arr2):
    #  first count occurrences

    # second add them in order to array called arr1_transformed
    n = len(arr1)
    m = len(arr2)
    occurrences = [0]*1001
    for i in arr1:
        occurrences[i] += 1

    
    arr1_transformed = []
    for i in arr2:
        small_arr = [i] * occurrences[i]
        arr1_transformed.extend(small_arr)
    
    remain = []
    for i in range(len(occurrences)):
        if i not in arr2 and occurrences[i] > 0:
            remaining = [i]*occurrences[i]
            remain.extend(remaining)
    # remain.sort() (already sorted since we iteration in ascending order)
    arr1_transformed.extend(remain)
    return arr1_transformed

    # arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6], Output: [22,28,8,6,17,44], occurrences [..], arr1_transformed = [22 (22*1), 28, 8, 6, 17,44]
    # O(n+k where k = 1001) time and O(k) or O(1) space