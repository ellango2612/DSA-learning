# directed graph of n nodes from 0 to n - 1.
# graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i,
# meaning there is an edge from node i to each node in graph[i]
# A node is a terminal node if there are no outgoing edges
# A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


# first instinct: topological sort: 
# - reverse the graph (all edges)
# - do bfs starting from terminal nodes (multi-source)
# - keep an array outdegree to record number of one's node outdegrees before reversing
# - seed queue in bfs with terminal node 
# - process bfs, checking if outdegree[node] == 0 after decrementing 1 (if its safe)
# - if yes, add to queue. sort it. return.

def eventualSafeState(graph):
    if not graph:
        return []
    n = len(graph)
    reverse = [[] for _ in range(n)]
    outdegree = [0]*n
    for i in range(n):
        length = len(graph[i])
        for j in range(length):
            outdegree[i]+=1
            reverse[graph[i][j]].append(i)
    res = set()

    # def bfs(node):
    queue = deque([node for node in range(n) if outdegree[node]==0])
    for i in queue:
        res.add(i)
    while queue:
        current = queue.popleft()
        for nei in (reverse[current]):
            outdegree[nei] -= 1
            if outdegree[nei] == 0:
                res.add(nei)
                queue.append(nei)
    return sorted(res)
                     

# O(n + e) time, O(n + e) spac