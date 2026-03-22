# Given the heads of two singly linked-lists headA and headB, 
# return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

def intersection(headA, headB):
    ptr_A = headA
    ptr_B = headB
    while ptr_A != ptr_B:
        ptr_A = ptr_A.next if ptr_A else headB
        ptr_B = ptr_B.next if ptr_B else headA
    return ptr_B

# O(m+n) time and O(1) space since just using 2 ptrs and no extra DS

