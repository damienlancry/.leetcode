#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        if x == 0:
            return 0
        res = 0
        while x > 0:
            x, y = x // 10, x % 10
            res = res * 10 + y
        return res if res < 2 ** 31 - 1 else 0


# @lc code=end
