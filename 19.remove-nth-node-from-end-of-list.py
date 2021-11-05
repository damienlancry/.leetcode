#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        def len(head):
            i = 0
            while head:
                head = head.next
                i += 1
            return i

        sz = len(head)
        current = head
        for _ in range(sz - n - 1):
            current = current.next
        if sz == n:
            return head.next

        prev = current
        current = current.next
        print(prev.val, current.val)
        while current.next:
            current.val = current.next.val
            current, prev = current.next, current
        prev.next = None
        return head


# @lc code=end
