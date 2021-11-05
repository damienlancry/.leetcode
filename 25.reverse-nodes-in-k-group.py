#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def is_long_enough(head, k):
        for _ in range(k):
            if head is None:
                return False
            else:
                head = head.next
        return True

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1 or not self.is_long_enough(head, k):
            return head
        else:
            oldhead = head
            prev = head
            curr = head.next
            for _ in range(k - 1):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            oldhead.next = self.reverseKGroup(curr, k)
            return prev


# @lc code=end
