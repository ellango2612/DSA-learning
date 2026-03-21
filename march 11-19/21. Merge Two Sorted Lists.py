# given the heads of two sorted linked lists list1 and list2, Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

#  thoughts: use recursion: the base cases are:
#  1. if the heads of both lists == None or one of them is None -> return the other
# 2. if one head < the other, return mergesorted(that head's next node, the other head)

def mergeSortedLists(list1, list2):
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    elif list1.val < list2.val:
        list1.next = mergeSortedLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeSortedLists(list1, list2.next)
        return list2
    
# O(n+m) time and O(n+m) space