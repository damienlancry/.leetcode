#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        dummyhead = ListNode(0, head)
        pleft = dummyhead
        left = head
        while True:
            while left and left.val < x:
                pleft = pleft.next
                left = left.next
            if not left:
                return head
            pright = left
            right = left.next
            while right and right.val >= x:
                pright = pright.next
                right = right.next
            if not right:
                return head
            pleft.next = right
            pright.next = right.next
            right.next = left
            if head == left:
                head = right
            pleft = right


# @lc code=end
