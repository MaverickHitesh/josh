# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists

# Runtime: 36 ms, faster than 76.77% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.4 MB, less than 32.18% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    # this is for the edge case
    # l1 = [1,2,3]; l2 = [1,3,4,5,6]; merged = [1,1,2,3,4,5,6]
    if l1:
        cur.next = l1
    elif l2:
        cur.next = l2

    return dummy.next