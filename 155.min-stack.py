#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    def __init__(self):
        self.size = 2 ** 4
        self.stack = [None] * self.size
        self.topidx = -1

    def push(self, val: int) -> None:
        prevtop = self.stack[self.topidx]
        if prevtop is not None:
            prevmin = prevtop.min
        else:
            prevmin = None
        if prevmin is None or val < prevmin:
            newmin = val
        else:
            newmin = prevmin
        self.topidx += 1
        if self.topidx >= self.size:
            self.stack += [None] * self.size
            self.size *= 2
        self.stack[self.topidx] = Node(val, newmin)

    def pop(self) -> None:
        self.topidx -= 1

    def top(self) -> int:
        if self.topidx > -1:
            return self.stack[self.topidx].val
        else:
            return None

    def getMin(self) -> int:
        if self.topidx > -1:
            return self.stack[self.topidx].min
        else:
            return None


class Node:
    def __init__(self, val, min):
        self.val = val
        self.min = min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
