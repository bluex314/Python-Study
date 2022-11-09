# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        # 1 -> 2
        # 1 <- 2
        # head -> next_node
        if head is None or head.next is None:
            return head

        # prev = None
        # while head.next:
        #    nxt = head.next
        #    head.next = prev
        #    prev = head
        #    head = nxt
        # head.next = prev
        # return head
        # # 1 -> 2 -> 3
        # 1 <- 2 <- 3
        nxt = self.reverseList(head.next)
        head.next.next = head # 2 is head
        # 2's next node is 3
        # 3's next node after reverse should be 2
        # so head.next.next that is 3.next = head = 3
        # head.next = None heads 2.next = None
        head.next = None
        return nxt

def print_ll(ans):
    while ans:
        if ans.next:
            print(ans.val, end='->')
        else:
            print(ans.val)
        ans = ans.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    head.next = h2
    h2.next = h3
    print_ll(head)
    ans = s.reverseList(head)
    print_ll(ans)
