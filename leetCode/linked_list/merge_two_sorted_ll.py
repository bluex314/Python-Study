# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1:[ListNode], list2: [ListNode]) -> [ListNode]:
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next

            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

            return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    h2 = ListNode(1)
    h3 = ListNode(3)
    head.next = h2
    h2.next = h3

    head2 = ListNode(2)
    h22 = ListNode(3)
    h33 = ListNode(4)
    head2.next = h22
    h22.next = h33

    ans = s.mergeTwoLists(head, head2)

    while ans:
        if ans.next:
            print(ans.val, end='->')
        else:
            print(ans.val)
        ans = ans.next

