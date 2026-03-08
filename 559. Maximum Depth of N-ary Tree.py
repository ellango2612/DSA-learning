# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

def maxDepth(self, root):
    if not root:
        return 0
    if not root.children:
        return 1
    return 1+ max(maxDepth(child) for child in root.children)

# O(n) time and O(h) space - recursion stack for tree; 
# recursive dfs (stack): O(n) time and O(h) space - O(h) = O(logn) for balanced tree and O(n) for worst case skewed tree
# O(n) space for iterative bfs - queue can hold up tp n nodes at once
