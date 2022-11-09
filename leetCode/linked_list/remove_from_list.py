# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        ll_len = self.find_ll_len(head)
        node_i_to_remove = ll_len - n + 1
        count = 1
        current = head
        prev = None
        while current:
            if count == node_i_to_remove:
                if prev:
                    prev.next = current.next
                else:
                    return current.next
            prev = current
            current = current.next
            count += 1

        return head

    def find_ll_len(self, head: [ListNode]):
        if head:
            count = 1
            while head.next:
                count += 1
                head = head.next
        return count


    def floyd_tortoise_hair_algo(self, head, n):
        s = f = head
        # if only one node is present
        if not f.next:
            return head.next

        for _ in range(n): f = f.next

        if not f:
            return head.next

        # finding the node to remove
        while f.next:
            f = f.next
            s = s.next
        # s + 1 is the node is the node to remove
        s.next = s.next.next
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    head.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    n = 5

    #ans = s.removeNthFromEnd(head, n)
    ans = s.floyd_tortoise_hair_algo(head, n)
    while ans:
        if ans.next:
            print(ans.val, end='->')
        else:
            print(ans.val)
        ans = ans.next