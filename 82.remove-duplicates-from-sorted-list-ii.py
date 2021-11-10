#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # find first value that has no duplicate
        while head and head.next and head.val == head.next.val:
            val = head.val
            while head and head.val == val:
                head = head.next
        if not head or not head.next:
            return head
        # now head is not duplicated for sure
        prev = head
        curr = head.next
        # next = head.next.next
        while curr and curr.next:
            if curr.val == curr.next.val:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return head

    def find_head(self, head):
        while head.val == head.next.val:
            val = head.val
            while head and head.val == val:
                head = head.next


# @lc code=end
