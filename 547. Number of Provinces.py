#  n citites, some are connected. province = group of (un)directly connected cities. given nxn isConnected matrix, return
# number of provinces; 8:08-23

#  thoughts: find number of connected components.

def numberofrovinces(isConnected):
    if not isConnected:
        return 0
    n = len(isConnected)
    visited = set()
    provinces = 0

    def dfs(city):
        visited.add(city)
        for i in range(n):
            if isConnected[i][city] == 1 and i not in visited:
                dfs(i)
    for i in range(n):
        if i not in visited:
            dfs(i)
            provinces+=1
    return provinces

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2; n = 3, visited = (0,1,2), provinces = 2.
