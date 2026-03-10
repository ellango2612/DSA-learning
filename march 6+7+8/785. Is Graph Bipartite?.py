def bipartiteGraph(graph):
    if not graph:
        return
    n = len(graph)
    color = [-1]*n # -1 is unvisited, 0 or 1 = colored, color [0,1,1,1], queue =(0,1)

    def bfs(node):
        queue = deque([node])
        color[node] = 0
        while queue:
            current = queue.popleft()
            for nei in graph[current]:
                if color[nei] == color[current]:
                    return False
                elif color[nei] == -1:
                    color[nei] = 1-color[current]
                    queue.append(nei)
        return True
    for node in range(n):
        if color[node] == -1:
            if not bfs(node):
                return False
    return True
            
