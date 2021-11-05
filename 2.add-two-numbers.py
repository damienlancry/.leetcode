#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(l1, l2, carry):
            if not l1 and not l2:
                if carry:
                    return ListNode(1, None)
                else:
                    return None
            if not l1:
                l1 = ListNode(0, None)
            if not l2:
                l2 = ListNode(0, None)
            val = l2.val + l1.val + carry
            carry, val = divmod(val, 10)
            l1.val = val
            l1.next = helper(l1.next, l2.next, carry)
            return l1

        return helper(l1, l2, 0)


# @lc code=end
