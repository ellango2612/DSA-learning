# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], 
# return true if and only if all the given nodes form exactly one valid binary tree.
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# thoughts: 
# ninary tree properties: - have 1 root; each node has at most 2 children; - no cycles; all nodes are connected (in visted)
# -> have a visited set and bfs traverse from node 0 (starting, supposed root) and check if its children form no cycles

def validateBinaryTree(n, leftChild, rightChild):
    # find root (s):
    children = [i for i in leftChild and rightChild if i != -1]
    roots = [i for i in range(n) if i not in children]
    if len(roots) != 1:
        return False #disconnected forest
    root = roots[0]
    visited = set()
    queue = deque(root)
    visited.add(root)
    while queue:
        current = queue.popleft()
        for i in (leftChild[current], rightChild[current]):
            if i not in visited and i != -1:
                queue.append(i)
                visited.add(i)
            elif i in visited:
                return False
    if len(visited) == n:
        return True

# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true; q = (), visited = (0,1,2,3) -> true