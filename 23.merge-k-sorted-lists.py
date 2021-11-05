#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Heap:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def getMin(self):
        return self.array[0]

    def heapify(self, pos):
        if self.is_leaf(pos):
            return
        if 2 * pos + 2 < self.size:
            if (
                self.array[2 * pos + 1] < self.array[pos]
                or self.array[2 * pos + 2] < self.array[pos]
            ):
                if self.array[2 * pos + 1] < self.array[2 * pos + 2]:
                    self.swap(pos, 2 * pos + 1)
                    self.heapify(2 * pos + 1)
                else:
                    self.swap(pos, 2 * pos + 2)
                    self.heapify(2 * pos + 2)
        else:
            if self.array[2 * pos + 1] < self.array[pos]:
                self.swap(pos, 2 * pos + 1)
                self.heapify(2 * pos + 1)

    def is_leaf(self, pos):
        return pos >= self.size // 2 and pos <= self.size - 1

    def swap(self, lpos, rpos):
        tmp = self.array[lpos]
        self.array[lpos] = self.array[rpos]
        self.array[rpos] = tmp

    def insert(self, val):
        self.array.append(val)
        pos = self.size - 1
        while pos > 0 and self.array[(pos - 1) // 2] > self.array[pos]:
            self.swap((pos - 1) // 2, pos)
            pos = (pos - 1) // 2

    def extract_min(self):
        if self.size == 1:
            return self.array.pop()
        popped = self.array[0]
        self.array[0] = self.array.pop()
        self.heapify(0)
        return popped

    @property
    def size(self):
        return len(self.array)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = Heap()
        dummy = node = ListNode()
        for head in lists:
            while head:
                heap.insert(head.val)
                head = head.next

        while heap.size > 0:
            val = heap.extract_min()
            node.next = ListNode(val)
            node = node.next
        return dummy.next


# @lc code=end
