# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

def removeVal(head, val):
    if not head:
        return
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while dummy.next:
        if dummy.next.val == val:
            dummy.next = dummy.next.next
        else:
            dummy = dummy.next

    return curr.next

#  Input: head = [1,2,6,3,4,5,6], val = 6, dummy = 3, dummy.next = 2
# Output: [1,2,3,4,5]