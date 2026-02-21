# # 934. Given an nxn binary matric grid where 1 = land and 0 = water; an island = 4-directionally connected group of 1's not connected to any other 1's.
# # There are exactly 2 islands in grid. 
# # You may change 0's to 1's to connect the 2 islands to form 1 island.
# # Return the smallest numebr of 0's you must flip to connect the 2 islands.

# thought process: DFS (to mark the first island) then multi-source BFS (to find the shortest path to the other island)

from collections import deque

def shortestBridge(grid):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    # cols = len(grid[0]) ; nxn matrix
    visited = set()
    queue = deque()
    found = False # mark as soon as we found the second island

    def dfs(r,c):
        # operation: finding all 1's in 1 island and mark visited
        if grid[r][c] == 1 and (r,c) not in visited:
            queue.append([r,c,0])
            visited.add((r,c))
            # recurse on 4 neighbors
            for nr,nc in [(r+1,c), (r,c+1),(r,c-1),(r-1,c)]:
                if 0<=nr<rows and 0<=nc<rows and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    dfs(nr,nc)

        # finding the first 1 (first island) to kick off dfs
        for r in range(rows):
            if found:
                break
            for c in range(rows):
                if grid[r][c] == 1:
                    dfs(r,c)
                    found = True
                    break

    # BFS to find the second island - when reaching the first 1
    while queue:
        r,c,dist = queue.popleft()
        for nr,nc in [(r+1,c), (r,c+1),(r,c-1),(r-1,c)]:
            if 0<=nr<rows and 0<=nc<rows and (nr,nc) not in visited:
                if grid[nr][nc] == 1:
                    return dist
                else:
                    visited.add((nr,nc))
                    queue.append([nr,nc,dist+1])
    return -1


        


    
