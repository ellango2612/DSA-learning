# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

def sameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.value == q.value:
        return sameTree(p.left,q.left) and sameTree(p.right,q.right)
