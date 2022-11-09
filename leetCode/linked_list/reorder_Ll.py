# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tail = head
        # re-order till count // 2
        count = 1
        # find the nth node
        while head.next:
            tail = head.next
            count += 1
        run_count = 0
        while head:
            if run_count == (count//2):
                return head
            temp = head.next.next
            head.next = tail
            