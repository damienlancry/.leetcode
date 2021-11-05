#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    def __init__(self):
        self.size = 2 ** 4
        self.stack = [None] * self.size
        self.front_index = self.size - 1
        self.back_index = self.size - 1

    def push(self, x: int) -> None:
        self.stack[self.back_index] = x
        self.back_index -= 1
        if self.back_index < 0 or self.front_index - self.back_index + 1 > self.size:
            self.stack = [0] * self.size + self.stack[self.back_index : self.front_index]
            self.front_index += self.size
            self.back_index += self.size
            self.size *= 2

    def pop(self) -> int:
        val = self.stack[self.front_index]
        self.front_index -= 1
        return val

    def peek(self) -> int:
        return self.stack[self.front_index]

    def empty(self) -> bool:
        return self.front_index == self.back_index


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
