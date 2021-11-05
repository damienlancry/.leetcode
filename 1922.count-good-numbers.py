#
# @lc app=leetcode id=1922 lang=python3
#
# [1922] Count Good Numbers
#

# @lc code=start
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return pow(20, n // 2, 10 ** 9 + 7) * 5 ** (n % 2) % (10 ** 9 + 7)


# @lc code=end
