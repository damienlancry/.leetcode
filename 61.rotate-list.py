#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        while node:
            print(node.val, " -> ")
            node = node.next
        print("None")


def pprint(node):
    while node:
        print(node.val, " -> ", end="")
        node = node.next
    print("None")


def getlen(head):
    len = 0
    while head:
        head = head.next
        len += 1
    return len


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        length = getlen(head)
        k = k % length
        return self._rotate(head, k, length)

    def _rotate(self, head, k, length):
        fast = head
        slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        temp = slow.next
        slow.next = None
        return temp


# @lc code=end
