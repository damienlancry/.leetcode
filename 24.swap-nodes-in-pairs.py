#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = head.next.next
        oldhead = head
        newhead = head.next
        newhead.next = oldhead
        oldhead.next = tmp
        newhead.next.next = self.swapPairs(tmp)
        return newhead


# @lc code=end
