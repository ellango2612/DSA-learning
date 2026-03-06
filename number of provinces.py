from collections import deque
# 547. Number of provinces
#  There are n cities. Some are connected and some not. Find number of provinces
# -> connected components . use DFS; given an nxn matrix isConnected, return number of provinces.

# dfs: we trigger dfs when found a city not visited. dfs will add all city connected to it to visited list and add 1 to count
def numProvinces(isConnected):
    provinces = 0
    visited = set()
    n = len(isConnected)

    def dfs(city):
        visited.add(city)
        for i in range(n):
            if isConnected[i][city] == 1 and i not in visited:
                # visited.add(i)
                dfs(i)

    for i in range(n):
        if i not in visited:
            dfs(i)
            provinces += 1

    return provinces

# O(n^2) time due to traversing a matrix and O(n) extra space (store visited set)


# bfs: triggered when found a city not visited (new province), bfs: add this city to visited and queue, then pop from q and 
# add all cities connected to it to q -> 1 province
# edge case: isConnected is empty

def numProvinces(isConnected):
    if not isConnected:
        return 0
    provinces = 0
    queue = deque()
    visited = set()
    n = len(isConnected)
    def bfs(city):
        queue.append(city)
        visited.add(city)
        while queue:
            current = queue.popleft()
            for i in range(n):
                if isConnected[i][current] == 1 and i not in visited:
                    queue.append(i)
                    visited.add(i)
        for i in range(n):
            if i not in visited:
                bfs(i)
                provinces+=1
    return provinces



# dfs
# def numberOfProvinces(isConnected):
#     if not isConnected:
#         return 0
#     n = len(isConnected)
#     visited = set()
#     res = 0
#     def dfs(city):
#         visited.add(city)
#         for i in range(n):
#             if isConnected[city][i] == 1 and i not in visited:
#                 dfs(i)

#     for i in range(n):
#         if i not in visited:
#             dfs(i)
#             res+=1

#     return res

# # Time: O(n^2), space: O(n)

# # bfs
# def numberOfProvinces(isConnected):
#     if not isConnected:
#         return 0
#     provinces = 0
#     visited = set()

#     def bfs(city):
#         queue = deque([city])
#         visited.add(city)
#         while queue:
#             current = queue.popleft()
#             for i in range(len(isConnected)):
#                 if isConnected[i][current] == 1 and i not in visited:
#                     visited.add(i)
#                     queue.append(i)
#     for i in range(len(isConnected)):
#         if i not in visited:
#             bfs(i)
#             provinces+=1
#     return provinces




