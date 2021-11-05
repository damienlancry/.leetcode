#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getlen(head):
    if not head:
        return 0
    else:
        return 1 + getlen(head.next)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if not headA or not headB:
            return
        m = getlen(headA)
        n = getlen(headB)

        if m > n:
            for _ in range(m - n):
                headA = headA.next

        if n > m:
            for _ in range(n - m):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next


# @lc code=end
