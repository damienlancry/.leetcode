#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    # brute force
    # def rob(self, nums: List[int]) -> int:
    #     return self.helper(nums, len(nums) - 1, 0)

    # def helper(self, nums, i, j):
    #     if i < 0:
    #         return j
    #     dorob = self.helper(nums, i - 2, j + nums[i])
    #     dontrob = self.helper(nums, i - 1, j)
    #     return max(dorob, dontrob)

    # dynamic programming: top down - memoization
    # def rob(self, nums: List[int]) -> int:
    #     return self.helper(nums, len(nums) - 1, 0, dict())

    # def helper(self, nums, i, j, dp):
    #     if (i, j) in dp:
    #         return dp[(i, j)]
    #     if i < 0:
    #         return j
    #     dorob = self.helper(nums, i - 2, j + nums[i], dp)
    #     dontrob = self.helper(nums, i - 1, j, dp)
    #     dp[i, j] = max(dorob, dontrob)
    #     return dp[i, j]

    # dynamic programming: bottom up - tabulation
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [0 for _ in range(n + 1)]
    #     dp[0] = 0
    #     dp[1] = nums[0]
    #     for i in range(1, n):
    #         dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
    #     return dp[n]

    # dynamic programming: bottom up - tabulation
    def rob(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, lo, hi) -> int:
        prev = 0
        curr = nums[lo]
        for i in range(1, hi + 1):
            curr, prev = max(prev + nums[i], curr), curr
        return curr


# @lc code=end
