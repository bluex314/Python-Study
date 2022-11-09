# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergerd_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergerd_lists.append(self.__merge_2_lists(l1, l2))
            lists = mergerd_lists
        return lists[0]

    def __merge_2_lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

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
    h23 = ListNode(10)
    head2.next = h22
    h22.next = h23

    head3 = ListNode(0)
    h32 = ListNode(5)
    h33 = ListNode(7)
    head3.next = h32
    h32.next = h33

    m_list = []
    m_list.append(head)
    m_list.append(head2)
    m_list.append(head3)

    ans = s.mergeKLists(m_list)

    while ans:
        if ans.next:
            print(ans.val, end='->')
        else:
            print(ans.val)
        ans = ans.next

