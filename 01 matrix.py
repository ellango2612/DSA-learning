from collections import deque
# 542: given mxn matrix mat, return the distance of the nearest 0 for each cell. The distance between 2 adj cells is 1.
#  -> my first thought: multi-source BFS again - we start bfs from all 0s: first put all of them on q, then increment count
# var by level, when popping off from queue, we look for that cell's neis and check if they are within bounds + == 1, if yes,
# assign that cell = count+1 ==> return the new mat

def binarymatrix(mat):
    if not mat or not mat[0]:
        return []
    m = len(mat)
    n = len(mat[0])
    count = 0
    visited = set()

    new_m = [0]*m
    for i in range(m):
        new_m[i] = [0]*n

    queue = deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i,j))
                visited.add((i,j))
    
    while queue:
        for i in range(len(queue)):
            curr_r, curr_c = queue.popleft()
            for nr,nc in [(curr_r+1,curr_c),(curr_r,curr_c+1),(curr_r-1,curr_c),(curr_r,curr_c-1)]:
                if 0<=nr<m and 0<=nc<n and mat[nr][nc] == 1 and (nr,nc) not in visited:
                    new_m[nr][nc] = count+1
                    queue.append((nr,nc))
                    visited.add((nr,nc))
        count+=1
    return new_m
    

