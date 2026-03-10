# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwise.

# thoughts: trigger dfs(0) and add all rooms can be visited to visited set. if by the end len(visited) == n -> true
# n = len(rooms)-1

def keysandrooms(rooms):
    n = len(rooms)
    visited = set()

    def dfs(room):
        visited.add(room)
        for i in rooms[room]:
            if i not in visited:
                dfs(i) 
    
    dfs(0)
    if len(visited) == n:
        return True
    return False

# Input: rooms = [[1],[2],[3],[]], visited = (0,1,2,3), 

# O(n+e) time, where n = number of rooms and e = number of keys across all rooms
# O(n) space (storing number of rooms in total)