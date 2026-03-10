# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

def numberIslands(grid):
    if not grid or not grid[0]:
        return 0
    m = len(grid)
    n = len(grid[0])
    visited = set()
    islands = 0

    def dfs(r,c):
        visited.add((r,c))
        for nr, nc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
            if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and grid[nr][nc] == '1':
                dfs(nr,nc)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i,j) not in visited:
                dfs(i,j)
                islands += 1
    return islands

# O(mn) time and O(mn) space