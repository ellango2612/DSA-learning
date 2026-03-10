from collections import deque
# 104. Max depth of binary tree
# Given root of a bin tree, return its max depth (number of nodes along the longest path from root -> farthest node)

# DFS solution:
def maxDepthofBinaryTree(root):
    if not root:
        return 0
    
    return 1+ max(maxDepthofBinaryTree(root.left), maxDepthofBinaryTree(root.right))

# Time: O(n) - n is number of nodes, space O(h) - number of levels

#  BFS:
def maxDepth(root):
    if not root: 
        return 0
    depth = 0
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right) 
            depth+=1

    return depth