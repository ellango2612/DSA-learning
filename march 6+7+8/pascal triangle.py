# 118. Pascal Triangle: Given an int numRows, return first numRows of Pascal's Triangle
# input: numRows = 5, output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def pascalTriangle(numRows):
    triangle = [0]*numRows #MUST init with something
    for i in range(numRows):
        triangle[i] = [1] * (i+1)
        for j in range (1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

# O(n^2) time, O(n^2) space
