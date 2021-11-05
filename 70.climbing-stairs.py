#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp_2 = 1
        dp_1 = 1
        for _ in range(2, n + 1):
            dp_2, dp_1 = dp_1, dp_1 + dp_2
        return dp_1


# @lc code=end
