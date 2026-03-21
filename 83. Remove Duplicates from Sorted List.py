# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# thoughts: iterative? O(n) time and O(1) space

def removeDuplicates(head):
    if not head:
        return
    curr = head
    # dummy = 
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

# O(n) time and O(1) space
