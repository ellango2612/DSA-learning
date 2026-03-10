from collections import deque
# 994. Given nxm grid where each cell is 1 of: 0 (empty), 1 (fresh orange), 2 (rotten orange). Every minute, every nei
# to a rotten orange becomes rotten. return min # minutes so that there are no fresh oranges. if impossible, return -1

# 11:24 - 38 (reality: 11:43)
# thoughts: need to use MULTI_SOURCE bfs for level-wise traversal. need to keep track of the number of fresh oranges - when this is 0, 
# we return number of mins it takes, else -1; bfs: first, add all rotten, unvisited oranges into the q. then. rot their neis
# if they're fresh oranges and push them onto q, after every layer, increment the minutes var. until the q is empty
# if the count of frsh oranges == 0, return minutes, else -1
# input: grid = [[2,2,2], [2,1,0], [0,1,1]] -> 4, fresh = 1, queue = ((2,1)), mins = 3

def rottingOranges(grid):
    if not grid or not grid[0]:
        return -1
    n = len(grid)
    m = len(grid[0])
    # count number of fresh
    fresh = 0
    mins = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                fresh+=1
            if grid[i][j] == 2:
                queue.append((i,j))

    # def bfs(r,c):
    while queue:
        for i in range(len(queue)):
            curr_r, curr_c = queue.popleft()
            for nei_r,nei_c in [(curr_r+1, curr_c), (curr_r, curr_c+1), (curr_r-1, curr_c), (curr_r, curr_c-1)]:
                if 0<=nei_r<n and 0<=nei_c<m and grid[nei_r][nei_c] == 1:
                    grid[nei_r][nei_c] = 2
                    queue.append((nei_r, nei_c))
                    fresh -= 1
        mins += 1

    # for (i,j) in queue:
    #     # bfs(i,j)
            
    if fresh == 0:
        return max(0,mins-1)

    return -1

