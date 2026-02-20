# # 934. Given an nxn binary matric grid where 1 = land and 0 = water; an island = 4-directionally connected group of 1's not connected to any other 1's.
# # There are exactly 2 islands in grid. 
# # You may change 0's to 1's to connect the 2 islands to form 1 island.
# # Return the smallest numebr of 0's you must flip to connect the 2 islands.

# from collections import deque

# def shortestBridge(grid):
#     if not grid or not grid[0]:
#         return -1
#     rows = len(grid)
#     cols = len(grid[0])
#     visited = set()
#     queue = deque()
#     found = False

#     def dfs(i,j):
#         # operation: finding all 1's in the first island and mark visited
#         if grid[i][j] == 1 and (i,j) not in visited:
#             queue.aapend([i,j])
#             visited.add((i,j))
#             # recurse on 4 neighbors
#             for nr,nc in [(r+1,c), (r,c+1),(r,c-1),(r-1,c)]:
#                 if grid[nr][nc] == 1 and (nr,nc) not in visited:
#                     dfs(nr,nc)
#         # finding the first 1 to kick off dfs
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1 and (r,c) not in visited:
#                     found = True
    
#     r,c = queue.popleft()
#     for nr,nc in [(r+1,c), (r,c+1),(r,c-1),(r-1,c)]:
        


    
