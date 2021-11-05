#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        def get_len(head):
            if not head:
                return 0
            return 1 + get_len(head.next)

        def get_middle_and_reverse(head, len):
            middle = head
            prev = None
            curr = head

            for _ in range(n // 2):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            if n % 2 == 1:
                curr = curr.next

            return curr, prev

        n = get_len(head)
        right, left = get_middle_and_reverse(head, n)
        for _ in range(n // 2):
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True


# @lc code=end
