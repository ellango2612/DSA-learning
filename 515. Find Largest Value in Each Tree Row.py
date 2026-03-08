# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

#  thoughts: bfs level-wise. at every level, record the max value and add that to return list

def largestValue(self, root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    queue = deque([root])
    res = []

    while queue:
        current_max=0
        for i in range(len(queue)):
            current = queue.popleft()
            current_max= max(current_max, current.val)
            for i in (current.left, current.right):
                if i: queue.append(i)
        res.append(current_max)
    return res

# Input: root = [1,3,2,5,3,null,9], q = [5,3,9], current = 1, current_max = 9, res = [1,3,]
# Output: [1,3,9]