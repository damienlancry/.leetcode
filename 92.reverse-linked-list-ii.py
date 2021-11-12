#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevleftnode = dummy
        leftnode = head
        for _ in range(left - 1):
            prevleftnode = prevleftnode.next
            leftnode = leftnode.next
        prevrightnode = prevleftnode.next
        rightnode = leftnode.next
        for _ in range(right - left):
            temp = rightnode.next
            rightnode.next = prevrightnode
            prevrightnode = rightnode
            rightnode = temp
        leftnode.next = rightnode
        prevleftnode.next = prevrightnode
        return dummy.next


# @lc code=end
