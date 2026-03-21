# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# thoughts: if a LL is a palindrome, it is == its reverse.

def palindromeLL(head):
    #  find mid
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse from slow.next
    prev = None
    curr = slow
    while curr:
        new_node = curr.next
        curr.next = prev
        prev = curr
        curr = new_node

    # compare
    current = head
    while prev:
        if prev.val == current.val:
            prev = prev.next
            current = current.next
        else:
            return False
    return True
    
    # this approach is a little wonky: if we modify the list in-place, there are no points of comparison anymore. so, better approach:
    # 1. find mid, 2. reverse the 2nd half, 3. compare the reversed half with the og head and return True if we can reach the end of the revesred half
    # Input: head = [1,2,2,1], slow=2, fast = 2, prev = 2(1), curr = 2(2), nn=1
# Output: true


# O(n) time and O(1) space
