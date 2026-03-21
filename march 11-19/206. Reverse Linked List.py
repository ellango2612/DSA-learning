# Given the head of a singly linked list, reverse the list, and return the reversed list.

def reverseLL(head):
    if not head:
        return
    curr = head
    prev = None
    while curr:
        node = curr.next
        curr.next = prev
        prev = curr
        curr = node
    return prev

# list = [1,4,7,8], curr = 8, prev = 7, node = None->8->7->4->1->None
