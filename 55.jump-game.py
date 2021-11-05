#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = 0
        for i in range(n):
            if i > dp:
                return False
            dp = max(i + nums[i], dp)
        return True


# @lc code=end
