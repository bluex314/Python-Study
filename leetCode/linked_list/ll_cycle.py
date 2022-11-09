# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: [ListNode]) -> bool:
        hash_head = {}
        while head:
            if head in hash_head:
               return True
            hash_head[head] = 1
            head = head.next
        return False


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    head.next = h2
    h2.next = h3
    h3.next = h2
    print(s.hasCycle(head))