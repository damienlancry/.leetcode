#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        pow5 = 0
        while 5 ** (pow5 + 1) <= n:
            pow5 += 1
        return sum([n // 5 ** i for i in range(1, pow5 + 1)])


# @lc code=end

# @lc code=end
